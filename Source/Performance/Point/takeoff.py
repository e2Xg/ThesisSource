# -*- coding: utf-8 -*-

import numpy as np

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def takeoff(altitude, cl_max, setting, mu, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 5.0):
    x = 0.0
    mach = 0.0
    time = 0.0
    #Stall Speed
    sos, rho, mu = standard_atmosphere(altitude)
    stall_speed = np.sqrt((ac_weight*9.81)/(0.5*rho*reference_area*cl_max))
    #Simplified to GroundRoll
    num_eng = design_input.loc["Total Number of Engines","Value"]
    mach_to = 1.2*stall_speed/sos
    while mach < mach_to:
        FF , NPF = engine_performance(engine_input, num_eng, altitude, mach, setting)
        drag, CD0, K = total_drag_estimation(
                    aerodynamic_data,
                    cl = cl_max,
                    design_cl = design_input.loc["Design Lift Coefficient","Value"],
                    mach = mach_to,
                    altitude = altitude,
                    reference_area = reference_area)
        a = (NPF - drag - mu*(cl_max*((0.5*rho*((mach*sos)**2)))-ac_weight*9.81))/ac_weight
        if (mach*sos + a*dt)/sos > mach_to: dt = (mach_to*sos - mach*sos)/a
        if (mach*sos + a*dt)/sos <= mach: break
        time += dt
        mach = (mach*sos + a*dt)/sos
        ac_weight -= FF*dt
        x += mach*sos*dt
    return x