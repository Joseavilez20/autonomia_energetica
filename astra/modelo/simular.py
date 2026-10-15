#!/usr/bin/env python3
"""Modelo ilustrativo 0.1.0. Python >=3.10; solo biblioteca estandar.
No usa datos climaticos reales ni simula transitorios o seguridad electrica.
Uso: python3 simular.py [entradas.json] [carpeta_salida]
"""
import copy
import json
import math
from pathlib import Path
import platform
import sys


def load_profile(c):
    x = c['loads']
    return [(x['fridge_kwh_day'] + x['other_kwh_day']) / 24
            + x['router_kw']
            + (x['computer_kw'] if h in x['computer_hours'] else 0)
            + (x['lights_kw'] if h in x['lights_hours'] else 0)
            + (x['phone_kw'] if h in x['phone_hours'] else 0)
            for h in range(24)]


def hydro_kw(s):
    return 9.81 * s['flow_l_s'] * s['net_head_m'] * s['hydro_efficiency'] / 1000


def simulate(c, s, stress=False, hydro_enabled=True, capacity_factor=1.0):
    loads = load_profile(c)
    shape = [max(0.0, math.sin(math.pi * (h + .5 - 6) / 12)) if 6 <= h < 18 else 0 for h in range(24)]
    shape = [v / sum(shape) for v in shape]
    cap = c['battery_nominal_kwh'] * c['usable_fraction'] * capacity_factor
    stored = 0.0  # energia electroquimica util SOBRE la reserva minima
    trace = []
    start = None
    e = {k: 0.0 for k in ['generation_kwh', 'pv_kwh', 'hydro_kwh', 'requested_ac_kwh',
         'served_ac_kwh', 'unserved_ac_kwh', 'aux_served_kwh', 'aux_unserved_kwh',
         'inverter_loss_kwh', 'battery_loss_kwh', 'curtailed_kwh', 'charge_bus_kwh', 'discharge_bus_kwh']}
    for d in range(-c['warmup_days'], c['days']):
        if d == 0:
            start = stored
        adverse = stress and d >= 0 and (d + 1) in c['stress_days']
        hsp = c['stress_hsp'] if adverse else s['hsp'] * c['solar_daily_factors'][d % 7]
        ph = hydro_kw(s) if hydro_enabled and not adverse else 0.0
        for h in range(24):
            # Un paso = 1 hora; kW medios * 1 h = kWh.
            pv = c['pv_kwp'] * hsp * s['pv_bus_factor'] * shape[h]
            gen = ph + pv
            request = loads[h]
            ac_possible = min(request, c['inverter_continuous_kw'])
            aux = c['inverter_idle_kw'] + (c['hydro_controls_kw'] if hydro_enabled else 0)
            need = ac_possible / c['inverter_efficiency'] + aux
            ci = do = bl = cut = 0.0
            if gen >= need:
                ci = min(gen - need, c['charge_limit_kw'], max(0.0, cap - stored) / c['charge_efficiency'])
                stored += ci * c['charge_efficiency']
                bl = ci * (1 - c['charge_efficiency'])
                cut = gen - need - ci
                supplied_bus = need
            else:
                do = min(need - gen, c['discharge_limit_kw'], stored * c['discharge_efficiency'])
                withdrawn = do / c['discharge_efficiency']
                stored -= withdrawn
                bl = withdrawn - do
                supplied_bus = gen + do
            aux_served = min(aux, supplied_bus)
            served = max(0.0, supplied_bus - aux_served) * c['inverter_efficiency']
            unserved = max(0.0, request - served)
            invloss = served * (1 / c['inverter_efficiency'] - 1)
            assert -1e-9 <= stored <= cap + 1e-9
            if d >= 0:
                vals = dict(generation_kwh=gen, pv_kwh=pv, hydro_kwh=ph,
                            requested_ac_kwh=request, served_ac_kwh=served, unserved_ac_kwh=unserved,
                            aux_served_kwh=aux_served, aux_unserved_kwh=aux-aux_served,
                            inverter_loss_kwh=invloss, battery_loss_kwh=bl, curtailed_kwh=cut,
                            charge_bus_kwh=ci, discharge_bus_kwh=do)
                for k, v in vals.items():
                    e[k] += v
                trace.append({'day':d+1, 'hour':h, 'pv_kw':pv, 'hydro_kw':ph,
                              'load_ac_kw':request, 'unserved_ac_kwh':unserved,
                              'usable_stored_kwh':stored, 'curtailed_kwh':cut})
    residual = (e['generation_kwh'] + start - stored - e['served_ac_kwh']
                - e['aux_served_kwh'] - e['inverter_loss_kwh'] - e['battery_loss_kwh'] - e['curtailed_kwh'])
    assert abs(residual) < 1e-8, residual
    e.update(start_usable_stored_kwh=start, end_usable_stored_kwh=stored,
             storage_delta_kwh=stored-start, balance_residual_kwh=residual,
             energy_served_fraction=e['served_ac_kwh']/e['requested_ac_kwh'],
             deficit_hours=sum(x['unserved_ac_kwh'] > 1e-8 for x in trace),
             deficit_days=len({x['day'] for x in trace if x['unserved_ac_kwh'] > 1e-8}),
             usable_capacity_kwh=cap, max_hourly_average_ac_kw=max(loads),
             hydro_nominal_bus_w=1000*hydro_kw(s) if hydro_enabled else 0,
             pv_kwp=c['pv_kwp'], battery_nominal_kwh=c['battery_nominal_kwh'],
             capacity_factor=capacity_factor, stress=stress)
    return e, trace


def calculations(c):
    demand=sum(load_profile(c))
    bus=demand/c['inverter_efficiency']+24*(c['inverter_idle_kw']+c['hydro_controls_kw'])
    # Darcy-Weisbach: longitud, diametro INTERIOR, caudal y factor de friccion supuestos.
    pipe={}
    for D in [0.032, 0.05, 0.063]:
        v=.002/(math.pi*D*D/4)
        friction=.025*100/D*v*v/(2*9.81)
        minor=3*v*v/(2*9.81)
        head=15-friction-minor
        pipe[str(D)]={'velocity_m_s':v,'friction_m':friction,'minor_m':minor,'net_head_m':head,
                     'power_w':9.81*2*head*.6 if head>0 else None,
                     'feasible_at_assumed_flow':head>0}
    # Thevenin ideal de generador de banco, NO curva real de un panel FV.
    thevenin=[]
    for R in [1,2,5,10,20,50,100]:
        i=6/(10+R)
        thevenin.append({'load_ohm':R,'current_a':i,'voltage_v':i*R,'load_w':i*i*R})
    cost={}
    years=c['costs']['years']; rate=c['costs']['real_discount_rate']
    for name,x in c['costs']['cases'].items():
        # Comparacion CONDICIONAL con igual energia anual; no es una prediccion anual.
        annual=demand*365
        npc=x['capex_usd']+sum((x['annual_om_usd']+x['replacements_usd'].get(str(y),0))/(1+rate)**y for y in range(1,years+1))
        energy_pv=sum(annual/(1+rate)**y for y in range(1,years+1))
        labor_pv=sum(x['annual_hours']*c['costs']['own_work_usd_hour']/(1+rate)**y for y in range(1,years+1))
        cost[name]={'conditional_annual_ac_kwh':annual,'net_present_cost_usd':npc,
                    'discounted_energy_kwh':energy_pv,'conditional_usd_kwh':npc/energy_pv,
                    'own_labor_present_usd':labor_pv,'conditional_usd_kwh_with_labor':(npc+labor_pv)/energy_pv,
                    'undiscounted_cost_usd':x['capex_usd']+years*x['annual_om_usd']+sum(x['replacements_usd'].values())}
    return {'daily_ac_kwh':demand,'daily_bus_kwh_hybrid':bus,
            'hydro_mean_w_needed_before_battery_losses':bus/24*1000,
            'flow_l_s_for_12m_60pct_before_battery_losses':bus/24*1000/(9.81*12*.6),
            'hydro_only_with_20pct_margin_flow_l_s':bus/24*1000/(9.81*12*.6)*1.2,
            'no_generation_autonomy_days_4kwh':4*.8*.96/bus,
            'battery_nominal_kwh_for_two_days':2*bus/(.8*.96),
            'battery_nominal_kwh_for_two_days_at_80pct_health':2*bus/(.8*.96*.8),
            'pv_kwp_hsp25_all_via_battery':bus/(2.5*.75*.96*.96),
            'thermal_20l_15c_kwh':20*4.186*15/3600,
            'tank_1m3_10m_ideal_kwh':1000*9.81*10/3_600_000,
            'pumping_5m3_20m_45pct_kwh':5000*9.81*20/(3_600_000*.45),
            'hydro_bench_20l_1m_ideal_wh':20*9.81/3600,
            'wind_d2_rho11_v5_cp025_eta08_w':.5*1.1*math.pi*5**3*.25*.8,
            'pipes':pipe,'thevenin_model':thevenin,'costs':cost}


def main():
    here=Path(__file__).resolve().parent
    src=Path(sys.argv[1]) if len(sys.argv)>1 else here/'entradas.json'
    out=Path(sys.argv[2]) if len(sys.argv)>2 else here/'salida'
    out.mkdir(parents=True,exist_ok=True)
    c=json.loads(src.read_text(encoding='utf-8'))
    cases={}; traces={}
    for key,s in c['scenarios'].items():
        cases['hibrido_'+key],traces['hibrido_'+key]=simulate(c,s)
    central=c['scenarios']['central']
    cases['hibrido_central_adverso'],traces['hibrido_central_adverso']=simulate(c,central,stress=True)
    cases['hibrido_adverso_bateria_degradada'],traces['hibrido_adverso_bateria_degradada']=simulate(c,central,stress=True,capacity_factor=.8)
    cbig=copy.deepcopy(c); cbig['battery_nominal_kwh']=8
    cases['hibrido_adverso_bateria_8kwh'],traces['hibrido_adverso_bateria_8kwh']=simulate(cbig,central,stress=True)
    for kwp in [.8,2.0]:
        cpv=copy.deepcopy(c); cpv['pv_kwp']=kwp
        for key in ['central','conservador']:
            name=f'solar_{kwp:g}kwp_{key}'
            cases[name],traces[name]=simulate(cpv,c['scenarios'][key],hydro_enabled=False)
    ch=copy.deepcopy(c); ch['pv_kwp']=0
    cases['hidro_central_sola'],traces['hidro_central_sola']=simulate(ch,central)
    # Limites fisicos: sin energia inicial ni generacion no hay energia entregada.
    zero=copy.deepcopy(c); zero['pv_kwp']=0
    z,_=simulate(zero,central,hydro_enabled=False)
    assert z['served_ac_kwh'] < 1e-10
    calc=calculations(c)
    result={'model_version':c['version'],'python_version':platform.python_version(),
            'method':'hora a hora; 30 dias de calentamiento y 30 dias evaluados; series sinteticas',
            'measurements_used':False,'calculations':calc,'cases':cases}
    (out/'resultados.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (out/'series_horarias.json').write_text(json.dumps(traces,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rows=['# Resultados calculados — modelo 0.1.0','',
          'Estimaciones con series sinteticas; no son mediciones ni una garantia de autonomia anual.','',
          '| Caso | Generacion DC kWh | Demanda AC kWh | AC no atendida kWh | Energia atendida % | Horas con deficit | Inicio / fin bateria util kWh |',
          '|---|---:|---:|---:|---:|---:|---:|']
    for name,x in cases.items():
        rows.append(f"| {name} | {x['generation_kwh']:.2f} | {x['requested_ac_kwh']:.2f} | {x['unserved_ac_kwh']:.2f} | {100*x['energy_served_fraction']:.2f} | {x['deficit_hours']} | {x['start_usable_stored_kwh']:.2f} / {x['end_usable_stored_kwh']:.2f} |")
    rows+=['','El porcentaje es cobertura de ENERGIA; no disponibilidad temporal. Se contabiliza la diferencia de almacenamiento.','',
           'Ver entradas.json, resultados.json y series_horarias.json para entradas, perdidas, vertimiento y limites.']
    (out/'resultados.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    print(json.dumps({'cases':len(cases),'daily_ac_kwh':calc['daily_ac_kwh'],
                     'max_balance_residual_kwh':max(abs(x['balance_residual_kwh']) for x in cases.values()),
                     'output':str(out)},ensure_ascii=False))


if __name__=='__main__':
    main()
