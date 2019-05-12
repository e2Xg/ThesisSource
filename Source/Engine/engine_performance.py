# -*- coding: utf-8 -*-

import numpy as np

def engine_performance(engine_input,number_of_engines,altitude,mach,setting):
    """ Interpolate engine data """
    def reduce_data(data,setting,altitude,mach):
        dataframe = data[data.SETTING == setting]
        altitudes = data.ALTITUDE.unique()
        altitude_m = max(altitudes[altitudes <= altitude])
        altitude_p = min(altitudes[altitudes >= altitude])
        dataframe_m = dataframe[dataframe.ALTITUDE == altitude_m]
        dataframe_p = dataframe[dataframe.ALTITUDE == altitude_p]
        FF_m = dataframe_m.FF.item()(mach)
        FF_p = dataframe_p.FF.item()(mach)
        NPF_m = dataframe_m.NPF.item()(mach)
        NPF_p = dataframe_p.NPF.item()(mach)
        FF = np.interp(altitude,[altitude_m,altitude_p],[FF_m,FF_p])
        NPF = np.interp(altitude,[altitude_m,altitude_p],[NPF_m,NPF_p])
        return FF, NPF
    engine_data = engine_input["Data Function"]
    #Get Unique List of Variables
    settings = engine_data.SETTING.unique()
    #Get Mach and Altitudes From List To Interpolate
    setting_m = max(settings[settings <= setting])
    setting_p = min(settings[settings >= setting])
    #Interpolate
    FF_sm, NPF_sm = reduce_data(engine_data,setting_m,altitude,mach)
    FF_sp, NPF_sp = reduce_data(engine_data,setting_p,altitude,mach)
    FF = np.interp(setting,[setting_m,setting_p],[FF_sm,FF_sp])
    NPF = np.interp(setting,[setting_m,setting_p],[NPF_sm,NPF_sp])
    return number_of_engines*FF, number_of_engines*NPF*9.81
