# -*- coding: utf-8 -*-

import copy
import pandas as pd

from Source.Performance.Mission.fly_distance import fly_distance
from Source.Performance.Mission.fly_setting import fly_setting
from Source.Performance.Mission.spend import spend
from Source.Performance.Mission.takeoff import takeoff
from Source.Performance.Mission.accelerate import accelerate
from Source.Performance.Mission.climb import climb
from Source.Performance.Mission.instantaneous_turn import instantaneous_turn
from Source.Performance.Mission.sustained_turn import sustained_turn
from Source.Performance.Mission.loiter import loiter

def analyze_mission_performance(mission_input ,design_input, engine_input, geometry_data, ac_weight, aerodynamic_data):
    reference_area = geometry_data["Wing"]["Data"].loc["Planform Area","Value"]
    relative_x_position = 0.0
    mach = 0.0
    altitude = 0.0
    totaltime = 0.0
    totalfuel = 0.0
    mission_performance_data = pd.DataFrame(index = [], columns = ["SEGMENT", "AC_WEIGHT", "SEGMENT_FUEL", "SEGMENT_DISTANCE", "SEGMENT_TIME", "MACH", "ALTITUDE", "TOTAL_DISTANCE", "TOTAL_TIME", "TOTAL_FUEL"])
    mission_performance_data.loc[0] = ["HANGAR", ac_weight, 0.0, 0.0, 0.0, mach, altitude, relative_x_position, totaltime, totalfuel]
    
    for index, row in mission_input.iterrows():
        parameters = copy.deepcopy(mission_input.loc[index,"Parameters"])
        if mission_input.loc[index,"Name"] == "SPEND":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = spend(parameters[0], parameters[1], parameters[2], parameters[3], ac_weight, engine_input, design_input)
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
        elif mission_input.loc[index,"Name"] == "TAKEOFF":
            if parameters[0] < 0.0: parameters[0] = altitude
            ac_weight, fuel, x, time, mach, altitude = takeoff(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
        elif mission_input.loc[index,"Name"] == "ACCELERATE":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = accelerate(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
 
        elif mission_input.loc[index,"Name"] == "CLIMB":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = climb(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
             
            
        elif mission_input.loc[index,"Name"] == "FLY_DISTANCE":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = fly_distance(parameters[0], parameters[1], parameters[2], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
        elif mission_input.loc[index,"Name"] == "FLY_SETTING":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = fly_setting(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
            
        elif mission_input.loc[index,"Name"] == "INSTANTANEOUS_TURN":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = instantaneous_turn(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
        elif mission_input.loc[index,"Name"] == "SUSTAINED_TURN":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = sustained_turn(parameters[0], parameters[1], parameters[2], parameters[3], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
        elif mission_input.loc[index,"Name"] == "LOITER":
            if parameters[0] < 0.0: parameters[0] = mach
            if parameters[1] < 0.0: parameters[1] = altitude
            ac_weight, fuel, x, time, mach, altitude = loiter(parameters[0], parameters[1], parameters[2], reference_area, ac_weight, engine_input, aerodynamic_data, design_input)
            relative_x_position += x
            totaltime += time
            totalfuel += fuel
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, fuel, x, time, mach, altitude, relative_x_position, totaltime, totalfuel]
            
        elif mission_input.loc[index,"Name"] == "DROP":
            ac_weight -= parameters[0]
            mission_performance_data.loc[index+1] = [mission_input.loc[index,"Name"], ac_weight, 0.0, 0.0, 0.0, mach, altitude, relative_x_position, totaltime, totalfuel]
            
    return totalfuel, mission_performance_data