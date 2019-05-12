# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from Source.Aerodynamics.drag_divergence_mach_number import drag_divergence_mach_number
from Source.Aerodynamics.standard_atmosphere import standard_atmosphere
from Source.Aerodynamics.zero_lift_component_drag import zero_lift_component_drag
from Source.Aerodynamics.lift_curve_slope_subsonic import lift_curve_slope_subsonic
from Source.Aerodynamics.lift_curve_slope_supersonic import lift_curve_slope_supersonic
#from Source.Aerodynamics.emlord import emlord

def analyze_aerodynamics(
        max_mach,
        max_altitude,
        geometry_data,
        cldesign,
        base_area,
        EWD,
        mach_np = 21,
        altitude_np = 5
        ):
    """ Analyze Aerodynamics """
    aerodynamic_data = pd.DataFrame(index = [], columns = ["ALTITUDE", "MACH", "COMPONENT DRAG C.", "BASE DRAG C.", "WAVE DRAG C.", "ZERO-LIFT DRAG C.","LIFT-CURVE SLOPE","K0","K100"])
    for tag in geometry_data.keys():
        if geometry_data[tag]["Type"] == "Wing":
            qcsweep = geometry_data[tag]["Data"].loc["Exposed Planform Quarter-Chord Sweep Angle","Value"]
            tonc = geometry_data[tag]["Data"].loc["Max t/c","Value"]
    mach_DD = drag_divergence_mach_number(qcsweep,tonc,cldesign)
    mach_CR = mach_DD-0.08
    machs = np.linspace(0.0,max_mach,mach_np)
    machs = np.append(machs,[mach_CR,mach_DD,1.0,1.05,1.2])
    machs = np.unique(machs)
    machs = np.sort(machs)
    mach_np = len(machs)
    altitudes = np.linspace(0.0,max_altitude,altitude_np)

    Sref = 0.0; l = 1.0; fus_area_dist = [0.0]; le_sweep = 0.0; d_on_q_emlord = None
    fs_area_dist = []
    for tag in geometry_data.keys():
            if geometry_data[tag]["Type"] == "Wing":
                Sref += geometry_data[tag]["Data"].loc["Planform Area"].item()
                le_sweep = geometry_data[tag]["Data"].loc["Planform Leading-Edge Sweep Angle"].item()
                fs_area_dist.append(geometry_data[tag]["Data"].loc["Chordwise Area Distribution","Value"])
            elif geometry_data[tag]["Type"] == "Fuselage":
                l = geometry_data[tag]["Data"].loc["Length"].item()
                fus_area_dist = geometry_data[tag]["Data"].loc["Area Distribution"].item()
                capture_area_location = geometry_data[tag]["Data"].loc["Capture Area Location"].item()
                total_capture_area = geometry_data[tag]["Data"].loc["Total Capture Area"].item()
                nozzle_area_location = geometry_data[tag]["Data"].loc["Nozzle Area Location"].item()
                total_nozzle_area = geometry_data[tag]["Data"].loc["Total Nozzle Area"].item()
                subtracted_area_x = np.array([0.0,capture_area_location-10**-5,capture_area_location,nozzle_area_location])
                subtracted_area_y = np.array([0.0,0.0,total_capture_area,total_nozzle_area])
            else:
                fs_area_dist.append(geometry_data[tag]["Data"].loc["Chordwise Area Distribution","Value"])
    d = np.sqrt(max(fus_area_dist[:,1])/np.pi)
    
    for altitude in altitudes:
        sos, rho, mu = standard_atmosphere(altitude)  
        cd_component = np.zeros(mach_np)
        cd_base = np.zeros(mach_np)
        cd_wave = np.zeros(mach_np)
        cd_0 = np.zeros(mach_np)
        cla = np.zeros(mach_np)
        K0 = np.zeros(mach_np)
        K100 = np.zeros(mach_np)

        for i in range(len(machs)):
            
            cd_component = zero_lift_component_drag(geometry_data,Sref,machs[i],mach_DD,rho,sos,mu,cd_component,i)
            for tag in geometry_data.keys():
                if geometry_data[tag]["Type"] == "Wing" :
                    #Subsonic Lift Curve Slope
                    if machs[i] < mach_DD: cla[i] += lift_curve_slope_subsonic(geometry_data[tag]["Data"].loc["Planform Aspect Ratio", "Value"],machs[i],geometry_data[tag]["Data"].loc["Max t/c Sweep","Value"],geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"],Sref,d,geometry_data[tag]["Data"].loc["Planform Span","Value"])
                    elif machs[i] >= 1.2: cla[i] += lift_curve_slope_supersonic(machs[i])
                    else:
                        #Transonic Transition of Lift Curve Slope
                        p1 = [mach_DD,lift_curve_slope_subsonic(geometry_data[tag]["Data"].loc["Planform Aspect Ratio", "Value"],mach_DD,geometry_data[tag]["Data"].loc["Max t/c Sweep","Value"],geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"],Sref,d,geometry_data[tag]["Data"].loc["Planform Span","Value"])]
                        p2 = [1.2,lift_curve_slope_supersonic(1.2)]
                        A = [
                             [p1[0]**3  , p1[0]**2  , p1[0] , 1],
                             [3*p1[0]**2, 2*p1[0]   , 1     , 0],
                             [p2[0]**3  , p2[0]**2  , p2[0] , 1],
                             [3*p2[0]**2, 2*p2[0]   , 1     , 0]
                             ]
                        B = [p1[1],0,p2[1],0]
                        pcoeffs = np.linalg.solve(A,B)
                        p = np.poly1d(pcoeffs)
                        cla[i] += p(machs[i])
                    #Estimating K (leading-edge suction)
                    K0[i] = 1.0/cla[i]
                    if machs[i] <= 1.0: 
                        K100[i] = 1.0/(np.pi*geometry_data[tag]["Data"].loc["Planform Aspect Ratio", "Value"])
                    elif machs[i] > 1.0 and machs[i] <= 1.0/np.sin(np.deg2rad(90.0-geometry_data[tag]["Data"].loc["Planform Leading-Edge Sweep Angle", "Value"])): 
                        K100[i] = 1.0/(np.pi*geometry_data[tag]["Data"].loc["Planform Aspect Ratio", "Value"])
                        K100[i] = np.interp(machs[i],[1.0,1.0/np.sin(np.deg2rad(90.0-geometry_data[tag]["Data"].loc["Planform Leading-Edge Sweep Angle", "Value"]))],[1.0/(np.pi*geometry_data[tag]["Data"].loc["Planform Aspect Ratio", "Value"]),1.0/cla[i]])
                    else: 
                        K100[i] = 1.0/cla[i]
                    

            #Base Drag Raymer Eq. 12.38 - 12.39
            if machs[i] < 1.0: cd_base[i] += (0.139 + 0.419*((machs[i]-0.161)**2))*base_area/Sref
            else: cd_base[i] += (0.064 + 0.042*((machs[i]-3.84)**2))*base_area/Sref
            
            #Wave Drag Raymer Eq. 12.46 for fuselage & Suave Eq. 16 for flying Surfaces
            if machs[i] >= 1.2: 
                if d_on_q_emlord == None:
                    #Adding all area distributions together
                    fus_x_stations = fus_area_dist[:,0]
                    fus_areas = fus_area_dist[:,1]
                    all_stations = np.array(fus_x_stations)
                    for fad_i in fs_area_dist:
                        all_stations = np.append(all_stations,fad_i[0])
                    all_stations.sort()
                    all_stations = np.unique(all_stations)
                    total_area = []
                    for j in range(len(all_stations)):
                        area1 = np.interp(all_stations[j],fus_x_stations,fus_areas)
                        area2 = 0.0
                        for fad_i in fs_area_dist:
                            area2 += np.interp(all_stations[j],fad_i[0],fad_i[1])
                        if all_stations[j] < l: total_area.append(area1+area2-np.interp(all_stations[j],subtracted_area_x,subtracted_area_y))
                        else: total_area.append(area1+area2+base_area)
                    total_area = np.array(total_area)
                    #Raymer
                    A_max = max(total_area)
                    D_on_q_sh = 9.0*np.pi/2.0*(A_max/l)**2
                    cd_wave_raymer = ((EWD*(1.0-0.386*((machs[i]-1.2)**0.57)*(1.0-np.pi*(le_sweep**0.77)/100.0))*D_on_q_sh)/Sref)*1.15
#                    #Emlord
#                    d_on_q_emlord = emlord(all_stations,total_area)
#                    cd_wave_emlord = d_on_q_emlord/Sref
                #Select Wave Drag
                cd_wave[i] += cd_wave_raymer
                if machs[i] == 1.2: drag_1_2 = cd_wave[i]
            #Low Mach Number Fix
            if i != 0:
                if cd_component[i-1] == 0.0: 
                    cd_component[i-1] = cd_component[i]
        #Finalize
        for i in range(len(machs)):
            #Estimate Transonic Transitions
            if machs[i] > mach_DD and machs[i] < 1.2:
                if machs[i] == 1.0: cd_wave[i] = drag_1_2/2.0
                elif machs[i] == 1.05: cd_wave[i] = drag_1_2
                elif machs[i] < 1.0: 
                    A = [
                         [mach_CR**3  , mach_CR**2  , mach_CR , 1],
                         [mach_DD**3  , mach_DD**2  , mach_DD , 1],
                         [1.0**3  , 1.0**2  , 1.0 , 1],
                         [3*mach_CR**2, 2*mach_CR   , 1     , 0]
                         ]
                    B = [0.0,0.002,drag_1_2/2.0,0]
                    lowcoeffs = np.linalg.solve(A,B)
                    lowfunc = np.poly1d(lowcoeffs)
                    cd_wave[i] = lowfunc(machs[i])
                elif machs[i] > 1.05 and machs[i] < 1.2: 
                    A = [
                         [1.05**3  , 1.05**2  , 1.05 , 1],
                         [3*1.05**2, 2*1.05   , 1     , 0],
                         [1.2**3  , 1.2**2  , 1.2 , 1],
                         [3*1.2**2, 2*1.2   , 1     , 0]
                         ]
                    B = [drag_1_2,drag_1_2/(1.05-mach_CR),drag_1_2,0]
                    highcoeffs = np.linalg.solve(A,B)
                    highfunc = np.poly1d(highcoeffs)
                    cd_wave[i] = highfunc(machs[i])
            elif machs[i] > mach_CR and machs[i] <= mach_DD:
                cd_wave[i] = np.interp(machs[i],[mach_CR,mach_DD],[0.0,0.002])
            cd_0[i] = cd_component[i] + cd_base[i] + cd_wave[i]
            aerodynamic_data.loc[0] = [altitude, machs[i], cd_component[i], cd_base[i], cd_wave[i], cd_0[i], cla[i], K0[i], K100[i]]
            aerodynamic_data.index = aerodynamic_data.index + 1
            aerodynamic_data.sort_index()
    return aerodynamic_data
