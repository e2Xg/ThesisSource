# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def sustained_turn(mach, altitude, numpi, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 5.0):
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
    x = 0.0
    fuel = 0.0
    time = 0.0
    pi_ = 0.0
    FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
    sos, rho, mu = standard_atmosphere(altitude)
    while pi_ < numpi*np.pi:
        dp = 0.5*rho*((mach*sos)**2)
        W = ac_weight*9.81
        sol = optimize.minimize_scalar(
        			calc_n,
                    bounds = (1.0, 9.0),
                    method='bounded',
        			args = (altitude, mach, W, dp, reference_area, NPF),
                    options = {'maxiter': 10}
        			)
        n = sol.x
        if n >= design_input.loc["Maximum Load Factor","Value"]: n = design_input.loc["Maximum Load Factor","Value"]
        cl = n*W/(dp*reference_area)
        drag, CD0, K = total_drag_estimation(
                aerodynamic_data,
                cl = cl,
                design_cl = design_input.loc["Design Lift Coefficient","Value"],
                mach = mach,
                altitude = altitude,
                reference_area = reference_area)
        turn_rate = 9.81*np.sqrt(n**2.0-1.0)/(mach*sos)
        if pi_ + turn_rate*dt > numpi*np.pi: dt = (numpi*np.pi - pi_)/turn_rate
        if pi_ + turn_rate*dt <= pi_: break
        R = ((mach*sos)**2.0)/(9.81*np.sqrt(n**2.0-1.0))
        time += dt
        ac_weight -= FF*dt
        fuel += FF*dt
        pi_ += turn_rate*dt
        if pi_ % (2.0 * np.pi) <= np.pi/2.0:
            x += R*np.sin(turn_rate*dt)
        elif pi_ % (2.0 * np.pi) <= np.pi and pi_ % (2.0 * np.pi) > np.pi/2.0:
            x -= R*np.sin(turn_rate*dt)
        elif pi_ % (2.0 * np.pi) >= np.pi and pi_ % (2.0 * np.pi) < 1.5*np.pi:
            x -= R*np.sin(turn_rate*dt)
        else:
            x += R*np.sin(turn_rate*dt)
    return ac_weight, fuel, x/1000.0, time, mach, altitude