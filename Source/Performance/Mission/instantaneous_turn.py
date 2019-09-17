# -*- coding: utf-8 -*-

import numpy as np

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def instantaneous_turn(mach, altitude, numpi, clmax, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 5.0):
    num_eng = design_input.loc["Total Number of Engines","Value"]
    x = 0.0
    fuel = 0.0
    time = 0.0
    pi_ = 0.0
    turn_rate = 0.0
    while pi_ < numpi*np.pi:
        sos, rho, mu = standard_atmosphere(altitude)
        dp = 0.5*rho*((mach*sos)**2)
        W = ac_weight*9.81
        n = dp*reference_area*clmax/W
        if n <= 1.0: n = 1.0
        if n >= design_input.loc["Maximum Load Factor","Value"]: n = design_input.loc["Maximum Load Factor","Value"]
        drag, CD0, K = total_drag_estimation(
                aerodynamic_data,
                cl = clmax,
                design_cl = design_input.loc["Design Lift Coefficient","Value"],
                mach = mach,
                altitude = altitude,
                reference_area = reference_area)
        FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
        turn_rate_old = turn_rate
        turn_rate = 9.81*np.sqrt(n**2.0-1.0)/(mach*sos)
        T = NPF - drag
        if pi_ + ((turn_rate+turn_rate_old)/2.0)*dt > numpi*np.pi: dt = (numpi*np.pi - pi_)/((turn_rate+turn_rate_old)/2.0)
        if pi_ + ((turn_rate+turn_rate_old)/2.0)*dt <= pi_: break
        R = ((mach*sos)**2.0)/(9.81*np.sqrt(n**2.0-1.0))
        time += dt
        T_W = T/W
        W_S = W/reference_area
        vv = mach*sos*(T_W - dp*CD0/W_S - n*n*K*W_S/dp)
        if abs(vv) >= mach*sos/2.0: vv = -mach*sos/2.0
        vh = np.sqrt(mach*sos**2.0 - vv**2.0)
        phi = -np.arctan(vv/vh)
        a = (NPF - drag + W*np.sin(phi))/ac_weight
        mach += a*dt/sos
        altitude += vv*dt
        time += dt
        ac_weight -= FF*dt
        fuel += FF*dt
        if pi_ % (2.0 * np.pi) <= np.pi/2.0:
            x += R*np.sin(((turn_rate+turn_rate_old)/2.0)*dt)
        elif pi_ % (2.0 * np.pi) <= np.pi and pi_ % (2.0 * np.pi) > np.pi/2.0:
            x -= R*np.sin(((turn_rate+turn_rate_old)/2.0)*dt)
        elif pi_ % (2.0 * np.pi) >= np.pi and pi_ % (2.0 * np.pi) < 1.5*np.pi:
            x -= R*np.sin(((turn_rate+turn_rate_old)/2.0)*dt)
        else:
            x += R*np.sin(((turn_rate+turn_rate_old)/2.0)*dt)
        pi_ += ((turn_rate+turn_rate_old)/2.0)*dt
    return ac_weight, fuel, x/1000.0, time, mach, altitude