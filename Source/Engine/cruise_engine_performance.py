# -*- coding: utf-8 -*-

from scipy import optimize

from Source.Engine.engine_performance import engine_performance

def cruise_engine_performance(number_of_engines, engine_input, altitude, mach, drag):
    def cruise_setting(setting,number_of_engines,engine_input,altitude,mach,drag):
        FF , NPF = engine_performance(engine_input,number_of_engines,altitude,mach,setting)
        return abs(drag-NPF)
    settings = engine_input["Data"].SETTING.unique()
    setting = optimize.fminbound(cruise_setting, min(settings), max(settings), args = (number_of_engines,engine_input,altitude,mach,drag))
    return setting