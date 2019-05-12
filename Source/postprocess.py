# -*- coding: utf-8 -*-

import os
import pandas as pd
from matplotlib import pyplot as plt

from Source.analyze import analyze
from Source.analyze_mission_performance import analyze_mission_performance
from Source.draw_ac import draw_ac
from Source.Main.save import save
from Source.Postprocess.vsp_aircraft import vsp_aircraft

def postprocess(designid,design_input,geometry_input,engine_input,mission_input,point_performance_input,vsppath=None):
    if os.path.isdir("POSTPROCESS") == False: os.mkdir("POSTPROCESS")
    if os.path.isdir(os.path.join("POSTPROCESS",designid)) == False: os.mkdir(os.path.join("POSTPROCESS",designid))
    #Analyze
    geometry_data, weight_data, aerodynamic_data, point_performance_data = analyze(design_input,geometry_input,engine_input,point_performance_input)
    #Run Mission
    ac_weight = weight_data.loc["Design Mission Takeoff Weight","Initial Value"]
    fuel_consumed, mission_performance_data = analyze_mission_performance(
            mission_input,
            design_input,
            engine_input,
            geometry_data,
            ac_weight, 
            aerodynamic_data) 
    #Save AC Figure
    fig, ax = draw_ac(geometry_data)
    fig.savefig(os.path.join("POSTPROCESS",designid,designid+".png"))
    fig.clf()
    plt.close(fig)
    #Create Excel Output
    with pd.ExcelWriter(os.path.join("POSTPROCESS",designid,designid+".xlsx")) as writer:
        for tag in geometry_data.keys():
            geometry_data[tag]["Data"].to_excel(writer, sheet_name="Geometry {}".format(tag))
        weight_data.to_excel(writer, sheet_name="Weight")
        aerodynamic_data.to_excel(writer, sheet_name="Aerodynamics")
        mission_performance_data.to_excel(writer, sheet_name="Mission Performance")
        point_performance_data.to_excel(writer, sheet_name="Point Performance")
    save(os.path.join("POSTPROCESS",designid,designid+'_geometry_input.pydata'),geometry_input)
    #Create VSP Script File
    vspscript = os.path.join("POSTPROCESS",designid,designid+'_aircraft')
    for tag in geometry_input.keys():
        if geometry_input[tag]["Type"] == "Fuselage":
            vsp_aircraft(vspscript,geometry_input,designid)
    #Run VSP Script File If VSP.exe Path is Sent
    if vsppath != None:
        curdir = os.getcwd()
        os.chdir(os.path.join("POSTPROCESS",designid))
        os.system(vsppath+" -script "+designid+'_aircraft.vspscript'+" > vspscript_out.txt")
        os.chdir(os.path.join(curdir))
    return