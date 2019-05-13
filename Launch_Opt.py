#Launcher
import time

from Source.aircraft_optimization import aircraft_optimization
from Source.Optimization.aircraft_objective_function import aircraft_objective_function
from Source.postprocess import postprocess
from Source.Main.load import load

if __name__ == "__main__":
    start = time.time()
    
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
    
    optimization_results = aircraft_optimization(design_input,
                                                 geometry_input,
                                                 engine_input,
                                                 mission_input,
                                                 point_performance_input,
                                                 numcore = 6,
                                                 iterations = 3000)

    end = time.time()
    print("|| Execution Time: {:.2f} Minutes ||".format((end-start)/60.0))
    del start
    del end
    
    file = open("optimization_results.csv","w")
    file.write("EXPOSED SPAN;EXPOSED CR;EXPOSED TR;SWEEP;SUPM;SUSG;TIP CHORD;TE SWEEP;PITCHUP\n")
    for result in optimization_results.result:
        B = result.variables[0]
        CR = result.variables[1]
        TR = result.variables[2]
        SWEEP = result.variables[3]
        SUPM = result.objectives[0]
        SUSG = result.objectives[1]
        CT = result.constraints[0]
        TESWEEP = result.constraints[1]
        AAR = result.constraints[2]
        file.write("{:.3f};{:.3f};{:.3f};{:.3f};{:.3f};{:.3f};{:.3f};{:.3f};{:.3f}\n".format(B,CR,TR,SWEEP,SUPM,SUSG,CT,TESWEEP,AAR))
    file.close()
    
    #PLOT
    import matplotlib.pyplot as plt
    import pandas as pd
    df = pd.read_csv("optimization_results.csv",delimiter=";")
    x = df["SUPM"]
    y = df["SUSG"]
    c = df["SWEEP"]
    plt.figure(dpi=360)
    plt.scatter(x,y,c=c)
    plt.colorbar(label="SWEEP")
    plt.clim(min(c),max(c))
    plt.grid()
    plt.savefig("result.png")
	
    results = open("optimization_results.csv","r")
    resultslines = results.readlines()
    #Run each case again to save results
    vsppath = "D:\VSP\\vspscript.exe"
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

