# -*- coding: utf-8 -*-

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.cruise_engine_performance import cruise_engine_performance
from Source.Engine.engine_performance import  engine_performance


def fly_distance(mach, altitude, distance, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 600.0):
    distance = distance*1000
    num_eng = design_input.loc["Total Number of Engines","Value"]
    sos, rho, mu = standard_atmosphere(altitude)
    x = 0.0
    fuel = 0.0
    time = 0.0
    while x < distance:
        cl = (ac_weight*9.81)/(reference_area*0.5*rho*((mach*sos)**2))
        drag, CD0, K = total_drag_estimation(
                aerodynamic_data,
                cl = cl,
                design_cl = design_input.loc["Design Lift Coefficient","Value"],
                mach = mach,
                altitude = altitude,
                reference_area = reference_area)
        setting = cruise_engine_performance(num_eng, engine_input, altitude,mach,drag)
        FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
        if mach*sos*dt+x > distance: dt = (distance-x)/(mach*sos)
        if mach*sos*dt+x <= x: break
        time += dt
        ac_weight -= FF*dt
        fuel += FF*dt
        x += mach*sos*dt
    return ac_weight, fuel, x/1000.0, time, mach, altitude

