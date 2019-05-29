# -*- coding: utf-8 -*-

from Source.engine_input import engine_input

from Source.Main.save import save

engine_input = engine_input("RaymerEngineScaledForF15.csv")

#Save Data
save('F15class_engine_input.pydata', engine_input)