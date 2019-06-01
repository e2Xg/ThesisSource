# -*- coding: utf-8 -*-

from Source.engine_input import engine_input

from Source.Main.save import save

engine_input = engine_input("RaymerEngineScaledForF106.csv")

#Save Data
save('F106class_engine_input.pydata', engine_input)