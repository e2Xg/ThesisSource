# -*- coding: utf-8 -*-

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def sep(mach, altitude, setting, reference_area, ac_weight, engine_input, aerodynamic_data, design_input):
    num_eng = design_input.loc["Total Number of Engines","Value"]
    FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
    sos, rho, mu = standard_atmosphere(altitude)
    W = ac_weight*9.81
    cl = (ac_weight*9.81)/(reference_area*0.5*rho*((mach*sos)**2))
    drag, CD0, K = total_drag_estimation(
            aerodynamic_data,
            cl = cl,
            design_cl = design_input.loc["Design Lift Coefficient","Value"],
            mach = mach,
            altitude = altitude,
            reference_area = reference_area)
    SEP = ((NPF-drag)/W)*(mach*sos)
    return SEP