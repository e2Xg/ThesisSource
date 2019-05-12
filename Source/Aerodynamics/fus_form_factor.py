# -*- coding: utf-8 -*-

import numpy as np

def fus_form_factor(l,Amax):
    """Estimate the fuselage form factor - Raymer Eq. 12.33 & 12.31"""
    f = l/((4.0/np.pi)*Amax)
    return (1.0+(60.0/(f**3))+(f/300.0))