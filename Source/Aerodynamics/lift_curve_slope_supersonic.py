# -*- coding: utf-8 -*-

import numpy as np

def lift_curve_slope_supersonic(M):
    return 4.0/(np.sqrt((M**2)-1.0))

