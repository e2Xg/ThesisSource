# -*- coding: utf-8 -*-

import numpy as np

def flat_plate_skin_friction_coefficient(R,mach):
    """Flat plate skin friction coefficient based on Raymer Eq. 12.27"""
    return (0.455/((np.log10(R)**2.58))*((1.0+0.144*(mach**2))**0.65))