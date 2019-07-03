# -*- coding: utf-8 -*-

from scipy.optimize import minimize_scalar

from Source.Sizing.size_fuselage import size_fuselage
from Source.Sizing.move_wing import move_wing
from Source.Sizing.size_tails import size_tails
from Source.analyze_mission_performance import analyze_mission_performance
from Source.analyze import analyze

def analyze_sizing(design_input,geometry_input,engine_input,mission_input,skipprint = False):
    def function_size(PL,design_input,geometry_input,engine_input,mission_input):
        if skipprint == False: print("-------------------------------------------------------------")
        if skipprint == False: print("PLUG LENGTH: {:.2f} m".format(PL))
        modified_geometry_input = size_fuselage(PL,geometry_input)
        modified_geometry_input = move_wing(modified_geometry_input,design_input)
        modified_geometry_input = size_tails(PL,modified_geometry_input,design_input)
        #Analyze Geometry, Weight, Aerodynamics Data
        geometry_data, weight_data, aerodynamic_data, point_performance_data = analyze(design_input,modified_geometry_input,engine_input)
        #Run Mission
        fuel_usable = weight_data.loc["Total Usable Fuel","Initial Value"]
        ac_weight = weight_data.loc["Design Mission Takeoff Weight","Initial Value"]
        fuel_consumed, mission_performance_data = analyze_mission_performance(
                mission_input,
                design_input,
                engine_input,
                geometry_data,
                ac_weight, 
                aerodynamic_data)
        if skipprint == False: print("REMAINING FUEL: {:.2f} kg".format(fuel_usable-fuel_consumed))
        return (fuel_usable-fuel_consumed)**2
    for tag in geometry_input.keys():
        if geometry_input[tag]["Type"] == "Fuselage":
            PLxi = int(len(geometry_input[tag]["Xsec"]["X-Location"])/2)
    sol = minimize_scalar(
            function_size,
            bounds=(0.0, 8.0),
            method='bounded',
            args=(design_input,geometry_input,engine_input,mission_input),
            options = {'maxiter': 10}
            )
    modified_geometry_input = size_fuselage(sol.x,geometry_input)
    for tag in geometry_input.keys():
        if geometry_input[tag]["Type"] == "Fuselage":
            modified_geometry_input[tag]["Nozzle Area Location"] += sol.x
    modified_geometry_input = move_wing(modified_geometry_input,design_input)
    modified_geometry_input = size_tails(sol.x,modified_geometry_input,design_input)
    return modified_geometry_input