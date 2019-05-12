# -*- coding: utf-8 -*-

import copy
import numpy as np
from Source.Aerodynamics.emlord import emlord
from Source.Aerodynamics.ESDU_Aircraft_02_03_02 import ESDU_Aircraft_02_03_02
from Source.analyze_geometry import analyze_geometry

def wave_drag_optimization(geometry_input,design_input):
    print("THIS MODULE IS INCOMPLETE")
    modified_geometry_input = copy.deepcopy(geometry_input)
    geometry_data = analyze_geometry(geometry_input)
    base_area = design_input.loc["Base Area","Value"]
    fs_area_dist = []
    V =1.0
    Sref = 0.0
    for tag in geometry_data.keys():
        if geometry_data[tag]["Type"] == "Wing":
            Sref += geometry_data[tag]["Data"].loc["Planform Area"].item()
            fs_area_dist.append(geometry_data[tag]["Data"].loc["Chordwise Area Distribution","Value"])
        elif geometry_data[tag]["Type"] == "Fuselage":
            capture_area_location = geometry_data[tag]["Data"].loc["Capture Area Location"].item()
            total_capture_area = geometry_data[tag]["Data"].loc["Total Capture Area"].item()
            nozzle_area_location = geometry_data[tag]["Data"].loc["Nozzle Area Location"].item()
            total_nozzle_area = geometry_data[tag]["Data"].loc["Total Nozzle Area"].item()
            subtracted_area_x = np.array([0.0,capture_area_location-10**-5,capture_area_location,nozzle_area_location])
            subtracted_area_y = np.array([0.0,0.0,total_capture_area,total_nozzle_area])
            fus_area_dist = geometry_data[tag]["Data"].loc["Area Distribution"].item()
            fus_x_stations = fus_area_dist[:,0]
            fus_areas = fus_area_dist[:,1]
        else:
            fs_area_dist.append(geometry_data[tag]["Data"].loc["Chordwise Area Distribution","Value"])
        
    #Creating all area distributions for single set of fuselage stations
    #Combine into one set of fuselage stations
    fus_x_stations = fus_area_dist[:,0]
    fus_areas = fus_area_dist[:,1]
    all_stations = np.array(fus_x_stations)
    for fad_i in fs_area_dist: all_stations = np.append(all_stations,fad_i[0])
    all_stations.sort()
    all_stations = np.unique(all_stations)
    #Calculate fuselage area distribution add to all areas
    all_areas = []
    area = []
    for j in range(len(all_stations)): area.append(np.interp(all_stations[j],fus_x_stations,fus_areas))
    all_areas.append(np.array(area))
    #Calculate rest of flying surfaces to all areas
    for fad_i in fs_area_dist:
        area = []
        for j in range(len(all_stations)): area.append(np.interp(all_stations[j],fad_i[0],fad_i[1]))
        all_areas.append(np.array(area))
    #Estimate a total area array
    total_area = np.zeros(len(all_areas[0]))
    flying_surface_area = np.zeros(len(all_areas[0]))
    for j in range(len(all_areas)): 
        total_area += all_areas[j]
        if j != 0: flying_surface_area += all_areas[j]
    #Estimate flowthrough areas (subtract base area)
    flowthrough_area = np.zeros(len(all_stations))
    for j in range(len(all_stations)): 
        if all_stations[j] < nozzle_area_location: flowthrough_area[j] += np.interp(all_stations[j],subtracted_area_x,subtracted_area_y)
        else: flowthrough_area[j] -= base_area
    #Estimate drag evaluation area
    envelope_area = total_area - flowthrough_area
    #Evaluate actual wave drag coefficient of envelope area dist.
    ea_d_on_q = emlord(all_stations,envelope_area)
    ea_cdw = ea_d_on_q/Sref
    print("ENV EMLORD WAVE DRAG COEFF : ",ea_cdw)
    #Evaluate optimum area distribution keeping the maximum area same
    Smax = max(envelope_area)
    for i in range(len(all_stations)):
        if envelope_area[i] == Smax: 
            A = envelope_area[i]
            k = all_stations[i]
    N = envelope_area[0]
    B = base_area
    ns = (len(all_stations)-1)
    l = abs(max(all_stations)-min(all_stations))
    ea_d_on_q_opt, all_stations_opt, envelope_area_opt = ESDU_Aircraft_02_03_02(l,N,A,k,B,V,ns)
    ea_cdw_opt = ea_d_on_q_opt/Sref
    print("ENV OPT WAVE DRAG COEFF : ",ea_cdw_opt)
    #Calculate fuselage respecting constraints
    fuselage_area = envelope_area - flying_surface_area
    fuselage_area_opt = np.zeros(len(all_stations))
    for j in range(len(all_stations)): fuselage_area_opt[j] += np.interp(all_stations[j],all_stations_opt,envelope_area_opt) - flying_surface_area[j]
    delta_fuselage = fuselage_area_opt - fuselage_area
    delta_fuselage = delta_fuselage.clip(min=0.0)
    fuselage_area_opt_cons = fuselage_area + delta_fuselage
    #Construct optimum envelope with constraints and evaluate with emlord
    envelope_area_opt_cons = fuselage_area_opt_cons + flying_surface_area
    ea_opt_cons_d_on_q = emlord(all_stations,envelope_area_opt_cons)
    ea_opt_cons_cdw = ea_opt_cons_d_on_q/Sref
    print("ENV OPT CONS EMLORD WAVE DRAG COEFF : ",ea_opt_cons_cdw)
    #PLOTS
    from matplotlib import pyplot as plt
#    plt.figure()
#    plt.plot(all_stations,all_areas[0])
#    plt.plot(all_stations,all_areas[1])
#    plt.plot(all_stations,all_areas[2])
#    plt.plot(all_stations,all_areas[3])
#    plt.plot(all_stations,all_areas[4])
    plt.figure()
    plt.plot(all_stations,envelope_area,'b')
    plt.plot(all_stations_opt,envelope_area_opt,'g')
    plt.plot(all_stations,fuselage_area,'bo')
    plt.plot(all_stations,fuselage_area_opt,'go')
    plt.plot(all_stations,fuselage_area_opt_cons,'ro')
    plt.plot(all_stations,envelope_area_opt_cons,'r')
    plt.show()
    return modified_geometry_input
