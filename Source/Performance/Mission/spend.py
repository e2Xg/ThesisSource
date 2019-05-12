# -*- coding: utf-8 -*-

from Source.Engine.engine_performance import  engine_performance

def spend(mach, altitude, time, setting, ac_weight, engine_input, design_input):
    num_eng = design_input.loc["Total Number of Engines","Value"]
    FF , NPF = engine_performance(engine_input, num_eng, altitude,mach,setting)
    ac_weight -= FF*time*60.0
    fuel = FF*time*60.0
    return ac_weight, fuel, 0.0, time*60.0, 0.0, 0.0