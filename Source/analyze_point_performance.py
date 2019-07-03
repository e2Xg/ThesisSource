# -*- coding: utf-8 -*-

import pandas as pd

from Source.Performance.Point.instantaneous_turn import instantaneous_turn
from Source.Performance.Point.maximum_mach_number import maximum_mach_number
from Source.Performance.Point.sustained_turn import sustained_turn
from Source.Performance.Point.supercruise_mach_number import supercruise_mach_number
from Source.Performance.Point.sep import sep
from Source.Performance.Point.accelerate import accelerate
from Source.Performance.Point.takeoff import takeoff

def analyze_point_performance(point_performance_input,design_input,engine_input,geometry_data,weight_data,aerodynamic_data,onlyobjectives=False):
    reference_area = geometry_data["Wing"]["Data"].loc["Planform Area","Value"]
    fuel_usable = weight_data.loc["Total Usable Fuel","Initial Value"]
    ac_weight = weight_data.loc["Design Mission Takeoff Weight","Initial Value"]
    point_performance_data = pd.DataFrame(index = [], columns = ["Value"])
    for index, row in point_performance_input.iterrows():
        parameters = point_performance_input.loc[index,"Parameters"]
        #Check For Other Point Performance Calculations
        if onlyobjectives == False:
            if point_performance_input.loc[index,"Name"] == "INSTANTANEOUS_TURN":
                point_performance_data.loc["INSTANTANEOUS_TURN (deg/s)","Value"] = instantaneous_turn(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, (ac_weight - fuel_usable*parameters[4]/100.0), engine_input, aerodynamic_data, design_input)
            elif point_performance_input.loc[index,"Name"] == "MAXIMUM_MACH_NUMBER":
                point_performance_data.loc["MAXIMUM_MACH_NUMBER","Value"] = maximum_mach_number(parameters[0], parameters[1], reference_area, (ac_weight - fuel_usable*parameters[2]/100.0), engine_input, aerodynamic_data, design_input)
            elif point_performance_input.loc[index,"Name"] == "SEP":
                point_performance_data.loc["SEP","Value"] = sep(parameters[0], parameters[1], parameters[2], reference_area, (ac_weight - fuel_usable*parameters[3]/100.0), engine_input, aerodynamic_data, design_input)
            elif point_performance_input.loc[index,"Name"] == "ACCELERATE":
                point_performance_data.loc["ACCELERATE","Value"] = accelerate(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, (ac_weight - fuel_usable*parameters[4]/100.0), engine_input, aerodynamic_data, design_input)
            elif point_performance_input.loc[index,"Name"] == "TAKEOFF":
                point_performance_data.loc["TAKEOFF","Value"] = takeoff(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
        #Objectives Calculated    
        if point_performance_input.loc[index,"Name"] == "SUSTAINED_TURN":
            point_performance_data.loc["SUSTAINED_TURN (g)","Value"] = sustained_turn(parameters[0], parameters[1], parameters[2], reference_area, (ac_weight - fuel_usable*parameters[3]/100.0), engine_input, aerodynamic_data, design_input)
        elif point_performance_input.loc[index,"Name"] == "SUPERCRUISE_MACH_NUMBER":
            point_performance_data.loc["SUPERCRUISE_MACH_NUMBER","Value"] = supercruise_mach_number(parameters[0], parameters[1], reference_area, (ac_weight - fuel_usable*parameters[2]/100.0), engine_input, aerodynamic_data, design_input)
    return point_performance_data