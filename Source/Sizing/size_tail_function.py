# -*- coding: utf-8 -*-

import copy
import numpy as np

def size_tail_function(delta_span_t,tag,vol_coeff,modified_geometry_input,reference_area,reference_MAC_loc,reference_length):
    sizing_geometry_input = copy.deepcopy(modified_geometry_input)
    num_sec = len(sizing_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"])
    for i in range(num_sec-1):
        if sizing_geometry_input[tag]["Xsec"].loc[i+1,"Airfoil Leading-Edge Y Location"] >= 0.0:
            sizing_geometry_input[tag]["Xsec"].loc[i+1,"Airfoil Leading-Edge Y Location"] += delta_span_t
        else: sizing_geometry_input[tag]["Xsec"].loc[i+1,"Airfoil Leading-Edge Y Location"] -= delta_span_t
    #Tail Parameters
    cr = sizing_geometry_input[tag]["Xsec"].loc[0,"Airfoil Chord Length"]
    ct = sizing_geometry_input[tag]["Xsec"].loc[num_sec-1,"Airfoil Chord Length"]
    tr = ct/cr
    if sizing_geometry_input[tag]["Type"] == "Vertical Tail":
        semi_b = abs(max(sizing_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"]) - min(sizing_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"]))
        tail_area = (cr+ct)*semi_b/2.0
        ar = ((semi_b)**2)/tail_area
    else:
        semi_b = abs(max(sizing_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"]) - min(sizing_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"]))
        tail_area = (cr+ct)*semi_b
        ar = ((semi_b*2)**2)/tail_area
    mac = (2.0/3.0)*cr*(1.0+tr+tr**2.0)/(1.0+tr)
    root_le_x = sizing_geometry_input[tag]["Xsec"].loc[0,"Airfoil Leading-Edge X Location"]
    tip_le_x = sizing_geometry_input[tag]["Xsec"].loc[num_sec-1,"Airfoil Leading-Edge X Location"]
    sweep = np.arctan((tip_le_x-root_le_x)/semi_b)
    x_1_4 = ((1.0+2.0*tr)/12.0)*ar*np.tan(sweep)*cr+0.25*(mac)
    tail_MAC_loc = sizing_geometry_input[tag]["Xsec"].loc[0,"Airfoil Leading-Edge X Location"] + x_1_4
    #Volume Coefficient Calc
    tail_arm = abs(tail_MAC_loc-reference_MAC_loc)
    vol_coeff_calc = (tail_arm*tail_area)/(reference_length*reference_area)
    return (vol_coeff_calc-vol_coeff)**2