# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def engine_input(filename):
    """
    Create Design Data for analysis
    """
    engine_input = dict()
    engine_file = open(filename, 'r')
    lines = engine_file.readlines()
    performance_data = False
    engine_input["Data"] = pd.DataFrame(index = [], columns = ["SETTING","ALTITUDE","MACH","FF","NPF"])
    engine_input["Data Function"] = pd.DataFrame(index = [], columns = ["SETTING","ALTITUDE","FF","NPF"])
    for line in lines:
        elements = line.split(",")
        if elements[0] == "Fan Diameter": engine_input["Diameter"] = float(elements[1])
        elif elements[0] == "Engine Weight": engine_input["Weight"] = float(elements[1])
        elif elements[0] == "Fan Length": engine_input["Length"] = float(elements[1])
        elif elements[0] == "IDLE": engine_input["IDLE"] = float(elements[1])
        elif elements[0] == "MAX DRY": engine_input["MAX DRY"] = float(elements[1])
        elif elements[0] == "MAX RH": engine_input["MAX RH"] = float(elements[1])
        elif elements[0] == "PERFORMANCE DATA": performance_data = True
        
        if elements[0] != "PERFORMANCE DATA" and performance_data == True:
            engine_input["Data"].loc[0] = [float(elements[0]),float(elements[1]),float(elements[2]),float(elements[3]),float(elements[4])]
            engine_input["Data"].index = engine_input["Data"].index + 1
            engine_input["Data"] = engine_input["Data"].sort_index()
            
    #Set polynomials for each setting-altitude combination mach vs npf and mach vs fuel flow
    engine_settings = engine_input["Data"].SETTING.unique()
    for setting in engine_settings:
        temp_df = engine_input["Data"][engine_input["Data"].SETTING == setting]
        altitudes = temp_df.ALTITUDE.unique()
        for altitude in altitudes:
            temp_df2 = temp_df[temp_df.ALTITUDE == altitude]
            deg = 4
            FF_coeff = np.polyfit(temp_df2.MACH,temp_df2.FF,deg)
            NPF_coeff = np.polyfit(temp_df2.MACH,temp_df2.NPF,deg)
            engine_input["Data Function"].loc[0] = [setting,altitude,np.poly1d(FF_coeff),np.poly1d(NPF_coeff)]
            engine_input["Data Function"].index = engine_input["Data Function"].index + 1
            engine_input["Data Function"] = engine_input["Data Function"].sort_index()
    return engine_input