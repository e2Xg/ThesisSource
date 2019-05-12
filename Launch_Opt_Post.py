# -*- coding: utf-8 -*-

from Source.Optimization.aircraft_objective_function import aircraft_objective_function
from Source.postprocess import postprocess
from Source.Main.load import load

if __name__ == "__main__":
    #Design
    design_input = load('design_input.pydata')
    
    #Geometry
    geometry_input = load('geometry_input.pydata')
    
    #Engine
    engine_input = load('engine_input.pydata')
    
    #Analyze Mission Performance
    mission_input = load('mission_input.pydata')
    
    #Analze Point Performance
    point_performance_input = load('point_performance_input.pydata')

    results = open("optimization_results.csv","r")
    resultslines = results.readlines()
    #Run each case again to save results
    vsppath = "D:\\VSP\\vspscript.exe"
    for i in range(len(resultslines)-1):
        result = resultslines[i+1].split(";")
        variables = [
        float(result[0]),
        float(result[1]),
        float(result[2]),
        float(result[3]) ]
        sized_geometry_input, sized_geometry_data, sized_weight_data, sized_aerodynamic_data, sized_point_performance_data = aircraft_objective_function(variables,
                                                 design_input,
                                                 geometry_input,
                                                 engine_input,
                                                 mission_input,
                                                 point_performance_input,
                                                 onlyobjectives = False,
                                                 plotac = False)
        postprocess("Design"+str(i+1),design_input,sized_geometry_input,engine_input,mission_input,point_performance_input,vsppath)
        print("Design {} Saved.".format(i+1))