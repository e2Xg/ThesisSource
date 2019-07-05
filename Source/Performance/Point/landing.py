# -*- coding: utf-8 -*-

import numpy as np

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def landing(altitude, cl_max, setting, mu, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 5.0):
    x = 0.0
    mach = 0.0
    #Stall Speed
    sos, rho, mu = standard_atmosphere(altitude)
    stall_speed = np.sqrt((ac_weight*9.81)/(0.5*rho*reference_area*cl_max))
    #Approach
    num_eng = design_input.loc["Total Number of Engines","Value"]
    FF , NPF = engine_performance(engine_input, num_eng, altitude, mach, setting)
    drag, CD0, K = total_drag_estimation(
                aerodynamic_data,
                cl = cl_max,
                design_cl = design_input.loc["Design Lift Coefficient","Value"],
                mach = mach,
                altitude = altitude,
                reference_area = reference_area)
    R = 0.205*stall_speed**2
    climb_grad = (NPF-drag)/(ac_weight*9.81)
    if abs(climb_grad) > 1.0: climb_angle = climb_grad
    else: climb_angle = np.arcsin(climb_grad)
    altitude_flare = R*(1.0-np.cos(climb_angle))
    S_approach = (altitude - altitude_flare)/np.tan(climb_angle)
    x += S_approach
    #Flare
    altitude=altitude_flare
    S_flare = R*np.sin(climb_angle)
    x += S_flare
    #Ground Roll
    altitude = 0.0
    sos, rho, mu = standard_atmosphere(altitude)
    stall_speed = np.sqrt((ac_weight*9.81)/(0.5*rho*reference_area*cl_max))
    mach = 1.15*stall_speed/sos
    FF , NPF = engine_performance(engine_input, num_eng, altitude, mach, setting)
    drag, CD0, K = total_drag_estimation(
                aerodynamic_data,
                cl = cl_max,
                design_cl = design_input.loc["Design Lift Coefficient","Value"],
                mach = mach,
                altitude = altitude,
                reference_area = reference_area)
    while mach > 0.0:
        a = (NPF - drag - mu*(ac_weight*9.81-cl_max*((0.5*rho*((mach*sos)**2)))))/ac_weight
        if (mach*sos + a*dt)/sos < 0.0: dt = (0.0*sos - mach*sos)/a
        if (mach*sos + a*dt)/sos >= mach: break
        mach = (mach*sos + a*dt)/sos
        x += mach*sos*dt
    return x