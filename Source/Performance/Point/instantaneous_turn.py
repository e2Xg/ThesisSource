# -*- coding: utf-8 -*-

import numpy as np

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def instantaneous_turn(mach, altitude, clmax, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input):
    num_eng = design_input.loc["Total Number of Engines","Value"]
    FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
    sos, rho, mu = standard_atmosphere(altitude)
    V = mach*sos
    W = ac_weight*9.81
    n = (clmax*0.5*rho*(V**2)*reference_area)/W
    if n <= 1.0: n = 1.0
    if n >= design_input.loc["Maximum Load Factor","Value"]: n = design_input.loc["Maximum Load Factor","Value"]
    turn_rate = 9.81*(np.sqrt((n**2)-1.0))/V
    drag, CD0, K = total_drag_estimation(
            aerodynamic_data,
            cl = clmax,
            design_cl = design_input.loc["Design Lift Coefficient","Value"],
            mach = mach,
            altitude = altitude,
            reference_area = reference_area)
    return np.rad2deg(turn_rate)
