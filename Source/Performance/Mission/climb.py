# -*- coding: utf-8 -*-

import numpy as np

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance
from Source.Performance.Mission.accelerate import accelerate

def climb(mach, altitude0, altitude1, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 180.0):
    fuel = 0.0
    x = 0.0
    time = 0.0
    altitude = altitude0
    num_eng = design_input.loc["Total Number of Engines","Value"]
    #Find highest SEP by changing Mach Number
    SEP_ = []
    mach_list = []
    mach_check = 0.4
    if altitude >= altitude1: return ac_weight, fuel, x/1000.0, time, mach, altitude1
    while mach_check < max(aerodynamic_data["MACH"].unique()):
        sos, rho, mu = standard_atmosphere(altitude)
        FF , NPF = engine_performance(engine_input, num_eng, altitude, mach_check, setting)
        cl = (ac_weight*9.81)/(reference_area*0.5*rho*((mach_check*sos)**2))
        drag, CD0, K = total_drag_estimation(
                    aerodynamic_data,
                    cl = cl,
                    design_cl = design_input.loc["Design Lift Coefficient","Value"],
                    mach = mach_check,
                    altitude = altitude,
                    reference_area = reference_area)
        T = NPF - drag
        W = ac_weight*9.81
        SEP_.append((T/W)*mach_check*sos)
        mach_list.append(mach_check)
        mach_check = mach_check + 0.01
    SEP__ = 0.0
    for i in range(len(SEP_)):
        if SEP_[i] >= SEP__:
            mach_to = mach_list[i]
            SEP__ = SEP_[i]
    if mach_to <= mach: mach = mach_to
    else: 
        ac_weight, accfuel, accx, acctime, mach, altitude = accelerate(mach, altitude, mach_to, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
        x += accx
        fuel += accfuel
        time += acctime
    #Climb
    while altitude < altitude1:
        sos, rho, mu = standard_atmosphere(altitude)
        FF , NPF = engine_performance(engine_input, num_eng, altitude, mach, setting)
        cl = (ac_weight*9.81)/(reference_area*0.5*rho*((mach*sos)**2))
        drag, CD0, K = total_drag_estimation(
                    aerodynamic_data,
                    cl = cl,
                    design_cl = design_input.loc["Design Lift Coefficient","Value"],
                    mach = mach,
                    altitude = altitude,
                    reference_area = reference_area)
        T = NPF - drag
        W = ac_weight*9.81
        SEP_ = (T/W)*mach*sos
        climb_grad = SEP_ / (mach*sos)
        if abs(climb_grad) > 1.0: climb_angle = climb_grad
        else: climb_angle = np.arcsin(climb_grad)
        Vx = mach*sos*np.cos(climb_angle)
        Vy = mach*sos*np.sin(climb_angle)
        if altitude + Vy*dt > altitude1: dt = (altitude1 - altitude)/Vy
        if altitude + Vy*dt <= altitude: break
        time += dt
        ac_weight -= FF*dt
        fuel += FF*dt
        x += Vx*dt
        altitude += Vy*dt
        SEP_ = []
        mach_list = []
        mach_check = 0.4
        while mach_check < max(aerodynamic_data["MACH"].unique()):
            sos, rho, mu = standard_atmosphere(altitude)
            FF , NPF = engine_performance(engine_input, num_eng, altitude, mach_check, setting)
            cl = (ac_weight*9.81)/(reference_area*0.5*rho*((mach_check*sos)**2))
            drag, CD0, K = total_drag_estimation(
                        aerodynamic_data,
                        cl = cl,
                        design_cl = design_input.loc["Design Lift Coefficient","Value"],
                        mach = mach_check,
                        altitude = altitude,
                        reference_area = reference_area)
            T = NPF - drag
            W = ac_weight*9.81
            SEP_.append((T/W)*mach_check*sos)
            mach_list.append(mach_check)
            mach_check = mach_check + 0.1
        SEP__ = 0.0
        for i in range(len(SEP_)):
            if SEP_[i] >= SEP__:
                mach_to = mach_list[i]
                SEP__ = SEP_[i]
        if mach_to <= mach: mach = mach_to
        else: 
            ac_weight, accfuel, accx, acctime, mach, altitude = accelerate(mach, altitude, mach_to, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            x += accx
            fuel += accfuel
            time += acctime
    return ac_weight, fuel, x/1000.0, time, mach, altitude

