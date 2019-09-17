# -*- coding: utf-8 -*-

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def accelerate(mach0, altitude, mach1, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 15.0):
    fuel = 0.0
    x = 0.0
    time = 0.0
    sos, rho, mu = standard_atmosphere(altitude)
    mach = mach0
    num_eng = design_input.loc["Total Number of Engines","Value"]
    while mach < mach1:
        mach_old = mach
        cl = (ac_weight*9.81)/(reference_area*0.5*rho*((mach*sos)**2))
        FF , NPF = engine_performance(engine_input, num_eng, altitude, mach, setting)
        drag, CD0, K = total_drag_estimation(
                    aerodynamic_data,
                    cl = cl,
                    design_cl = design_input.loc["Design Lift Coefficient","Value"],
                    mach = mach,
                    altitude = altitude,
                    reference_area = reference_area)
        a = (NPF - drag)/(ac_weight)
        if (mach*sos + a*dt)/sos > mach1: dt = (mach1*sos - mach*sos)/a
        if (mach*sos + a*dt)/sos <= mach: break
        time += dt
        mach = (mach*sos + a*dt)/sos
        ac_weight -= FF*dt
        fuel += FF*dt
        x += ((mach+mach_old)/2.0)*sos*dt
    if mach > mach1: mach = mach1
    return ac_weight, fuel, x/1000.0, time, mach, altitude