# -*- coding: utf-8 -*-

import numpy as np

def fs_form_factor(x_c_m,t_c,mach,max_t_sweep):
    """Estimate the flying surface form factor - Raymer Eq. 12.30"""
    return (1.0+(0.6/x_c_m)*t_c+100.0*(t_c**4))*(1.34*(mach**0.18)*((np.cos(np.deg2rad(max_t_sweep)))**0.28))