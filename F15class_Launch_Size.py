#Launcher
import time

from Source.Optimization.aircraft_objective_function import aircraft_objective_function
from Source.postprocess import postprocess
from Source.Main.load import load

if __name__ == "__main__":
    start = time.time()
    
    #Design
    design_input = load('F15class_design_input.pydata')
    
    #Geometry
    geometry_input = load('F15class_geometry_input.pydata')
    
    #Engine
    engine_input = load('F15class_engine_input.pydata')
    
    #Analyze Mission Performance
    mission_input = load('mission_input.pydata')
    
    #Analze Point Performance
    point_performance_input = load('point_performance_input.pydata')
    
    variables = [
            10.463,
            5.015,
            0.167,
            49.975 ]
    
    sized_geometry_input, sized_geometry_data, sized_weight_data, sized_aerodynamic_data, sized_point_performance_data = aircraft_objective_function(variables,
                                             design_input,
                                             geometry_input,
                                             engine_input,
                                             mission_input,
                                             point_performance_input,
                                             onlyobjectives = False,
                                             plotac = False)
    
    vsppath = "D:\VSP\\vspscript.exe"
    postprocess("F15class_sized",design_input,sized_geometry_input,engine_input,mission_input,point_performance_input,vsppath)
    
    end = time.time()
    print("\n|| Execution Time: {:.2f} Minutes ||".format((end-start)/60.0))
    del start
    del end