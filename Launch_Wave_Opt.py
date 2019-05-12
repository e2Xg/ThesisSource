# -*- coding: utf-8 -*-
import time

from Source.Optimization.wave_drag_optimization import wave_drag_optimization
from Source.Main.load import load

start = time.time()

#Design
design_input = load('design_input.pydata')

#Geometry
geometry_input = load('geometry_input.pydata')

wave_drag_optimization(geometry_input,design_input)

end = time.time()
print("\n|| Execution Time: {:.2f} Minutes ||".format((end-start)/60.0))
del start
del end