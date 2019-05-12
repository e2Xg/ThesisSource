# -*- coding: utf-8 -*-

from scipy import optimize

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def sustained_turn(mach, altitude, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input):
    def calc_n(n_guess, altitude, mach, W, dp, Sref, NPF):
        cl = n_guess*W/(dp*Sref)
        drag, CD0, K = total_drag_estimation(
                aerodynamic_data,
                cl = cl,
                design_cl = design_input.loc["Design Lift Coefficient","Value"],
                mach = mach,
                altitude = altitude,
                reference_area = Sref)
        cd = CD0 + K*(cl**2)
        L_D = cl/cd
        n_calc = L_D*NPF/W
        return (n_calc-n_guess)**2
    num_eng = design_input.loc["Total Number of Engines","Value"]
    FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
    sos, rho, mu = standard_atmosphere(altitude)
    dp = 0.5*rho*((mach*sos)**2)
    W = ac_weight*9.81
    sol = optimize.minimize_scalar(
    			calc_n,
                bounds = (1.0, 9.0),
                method='bounded',
    			args = (altitude, mach, W, dp, reference_area, NPF)
    			)
    n = sol.x
    return n