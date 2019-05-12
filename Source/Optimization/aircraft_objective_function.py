# -*- coding: utf-8 -*-

import copy

from Source.Sizing.size_wing import size_wing
from Source.analyze_sizing import analyze_sizing
from Source.analyze import analyze

def aircraft_objective_function(x, design_input, geometry_input, engine_input, mission_input, point_performance_input, onlyobjectives = False, plotac = False):
    exposed_B = x[0]
    exposed_CR = x[1]
    exposed_TR = x[2]
    SWEEP = x[3]
    wingmodified_geometry_input = copy.deepcopy(geometry_input)
    wingmodified_geometry_input = size_wing(wingmodified_geometry_input,exposed_B,exposed_CR,exposed_TR,SWEEP)
    modified_geometry_input = analyze_sizing(design_input,wingmodified_geometry_input,engine_input,mission_input,skipprint = onlyobjectives)
    modified_geometry_data, modified_weight_data, modified_aerodynamic_data, modified_point_performance_data = analyze(design_input,modified_geometry_input,engine_input,point_performance_input,onlyobjectives=onlyobjectives)
    #Plot
    if plotac == True:
        from Source.draw_ac import draw_ac
        fig, ax = draw_ac(modified_geometry_data)
        fig.show()
    return modified_geometry_input, modified_geometry_data, modified_weight_data, modified_aerodynamic_data, modified_point_performance_data