# -*- coding: utf-8 -*-

import numpy as np

from Source.Performance.total_drag_estimation import total_drag_estimation
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Engine.engine_performance import  engine_performance

def landing(altitude, cl_max, setting, mu, reference_area, ac_weight, engine_input, aerodynamic_data, design_input, dt = 5.0):

    return x