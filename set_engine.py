# -*- coding: utf-8 -*-

from Source.engine_input import engine_input

from Source.Main.save import save

engine_input = engine_input("RaymerEngineScaledForF106.csv")

#Save Data
save('engine_inputF106class.pydata', engine_input)