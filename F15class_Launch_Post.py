# -*- coding: utf-8 -*-
import time

from Source.postprocess import postprocess
from Source.Main.load import load

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

vsppath = "D:\VSP\\vspscript.exe"
postprocess("F15class_baseline",design_input,geometry_input,engine_input,mission_input,point_performance_input,vsppath)

end = time.time()
print("\n|| Execution Time: {:.2f} Minutes ||".format((end-start)/60.0))
del start
del end