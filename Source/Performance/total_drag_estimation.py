# -*- coding: utf-8 -*-

import numpy as np

from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Aerodynamics.le_suction_factor import le_suction_factor
from Source.Aerodynamics.le_suction_K import le_suction_K

def total_drag_estimation(aerodynamic_data,cl,design_cl,mach,altitude,reference_area):
    def reduce_data(data,altitude,mach):
        dataframe = data[data.MACH == mach]
        altitudes = dataframe["ALTITUDE"].unique()
        altitude_m = max(altitudes[altitudes <= altitude])
        altitude_p = min(altitudes[altitudes >= altitude])
        dataframe_m = dataframe[dataframe.ALTITUDE == altitude_m]
        dataframe_p = dataframe[dataframe.ALTITUDE == altitude_p]
        CD0_m = dataframe_m["ZERO-LIFT DRAG C."].item()
        K0_m = dataframe_m["K0"].item()
        K100_m = dataframe_m["K100"].item()
        CD0_p = dataframe_p["ZERO-LIFT DRAG C."].item()
        K0_p = dataframe_p["K0"].item()
        K100_p = dataframe_p["K100"].item()
        CD0 = np.interp(altitude,[altitude_m,altitude_p],[CD0_m,CD0_p])
        K0 = np.interp(altitude,[altitude_m,altitude_p],[K0_m,K0_p])
        K100 = np.interp(altitude,[altitude_m,altitude_p],[K100_m,K100_p])
        return CD0,K0,K100
    
    S = le_suction_factor(cl,design_cl)
    
    machs = aerodynamic_data["MACH"].unique()
    
    if mach < min(machs): return 0.0, 0.0, 0.0
    mach_m = max(machs[machs <= mach])
    try : mach_p = min(machs[machs >= mach])
    except: mach_p = 2.0
    
    CD0_sm,K0_sm,K100_sm = reduce_data(aerodynamic_data,altitude,mach_m)
    CD0_sp,K0_sp,K100_sp = reduce_data(aerodynamic_data,altitude,mach_p)
    
    CD0 = np.interp(mach,[mach_m,mach_p],[CD0_sm,CD0_sp])
    K0 = np.interp(mach,[mach_m,mach_p],[K0_sm,K0_sp])
    K100 = np.interp(mach,[mach_m,mach_p],[K100_sm,K100_sp])
    K = le_suction_K(S,K0,K100)
    CD = CD0+K*(cl**2)
    sos, rho, mu = standard_atmosphere(altitude)
    q = 0.5*rho*((mach*sos)**2)
    D = CD*reference_area*q
    return D, CD0, K