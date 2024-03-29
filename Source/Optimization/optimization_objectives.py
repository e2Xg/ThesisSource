# -*- coding: utf-8 -*-

from Source.Optimization.aircraft_objective_function import aircraft_objective_function

def optimization_objectives(x, design_input, geometry_input, engine_input, mission_input, point_performance_input):
    modified_geometry_input, modified_geometry_data, modified_weight_data, modified_aerodynamic_data, modified_point_performance_data = aircraft_objective_function(x,
                                             design_input,
                                             geometry_input,
                                             engine_input,
                                             mission_input,
                                             point_performance_input,
                                             onlyobjectives = True,
                                             plotac = False)
    #Constraints
    for tag in modified_geometry_data.keys():
        if modified_geometry_data[tag]["Type"] == "Wing":
            TR = modified_geometry_data[tag]["Data"].loc["Planform Taper Ratio","Value"]
            CT = modified_geometry_data[tag]["Data"].loc["Planform Root Chord Length","Value"]*TR
            TESWEEP = modified_geometry_data[tag]["Data"].loc["Exposed Planform Trailing-Edge Sweep Angle","Value"]
    #Objectives
    SUPM = modified_point_performance_data.loc["SUPERCRUISE_MACH_NUMBER","Value"]
    SUSG = modified_point_performance_data.loc["SUSTAINED_TURN (g)","Value"]
    
    return [SUPM, SUSG], [CT,TESWEEP]