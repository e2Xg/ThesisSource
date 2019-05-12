# -*- coding: utf-8 -*-

from Source.engine_input import engine_input

from Source.Main.save import save

engine_input = engine_input("Raymer_Afterburning_Jet_Engine.csv")

#Save Data
save('engine_input.pydata', engine_input)