# -*- coding: utf-8 -*-

import numpy as np

def lift_curve_slope_subsonic(A,M,maxt_sweep,Sexp,Sref,d,b):
    F = 1.07*((1.0+d/b)**2)
    B = np.sqrt(1.0-M**2)
    cla = (2.0*np.pi*A*Sexp*F/Sref)/(2.0+np.sqrt(4.0+((A**2)*(B**2))*(1.0+(np.tan(np.deg2rad(maxt_sweep)))/(B**2))))
    return cla

