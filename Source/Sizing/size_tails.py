# -*- coding: utf-8 -*-

from scipy.optimize import minimize_scalar

from Source.analyze_geometry import analyze_geometry
from Source.Sizing.size_tail_function import size_tail_function

def size_tails(PL,modified_geometry_input,design_input):
    #Tail Apex Moved
    for tag in modified_geometry_input.keys():
        if modified_geometry_input[tag]["Type"] == "Horizontal Tail" or modified_geometry_input[tag]["Type"] == "Vertical Tail":
            for i in range(len(modified_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge X Location"])):
                modified_geometry_input[tag]["Xsec"].loc[i,"Airfoil Leading-Edge X Location"] += PL
    #Size Tail
    for tag in modified_geometry_input.keys():
        if modified_geometry_input[tag]["Type"] == "Wing":
            modified_geometry_data = analyze_geometry(modified_geometry_input)
            #Wing Parameters
            reference_area = modified_geometry_data[tag]["Data"].loc["Planform Area","Value"]
            reference_MAC_loc = modified_geometry_data[tag]["Data"].loc["Planform MAC Location","Value"]
            reference_length_vt = modified_geometry_data[tag]["Data"].loc["Planform Span","Value"]
            reference_length = modified_geometry_data[tag]["Data"].loc["Planform MAC Length","Value"]
    for tag in modified_geometry_input.keys():
        if modified_geometry_input[tag]["Type"] == "Horizontal Tail" or modified_geometry_input[tag]["Type"] == "Vertical Tail" or modified_geometry_input[tag]["Type"] == "Canard":
            if modified_geometry_input[tag]["Type"] == "Horizontal Tail": vol_coeff = design_input.loc["Horizontal Tail Volume Coefficient","Value"]
            elif modified_geometry_input[tag]["Type"] == "Vertical Tail": 
                vol_coeff = design_input.loc["Vertical Tail Volume Coefficient","Value"]
                reference_length = reference_length_vt
            elif modified_geometry_input[tag]["Type"] == "Canard": vol_coeff = design_input.loc["Canard Volume Coefficient","Value"]
            min_bound = -(max(modified_geometry_input[tag]["Xsec"].loc[:,"Airfoil Leading-Edge Y Location"])-min(modified_geometry_input[tag]["Xsec"].loc[:,"Airfoil Leading-Edge Y Location"]))
            sol = minimize_scalar(
                    size_tail_function, 
                    bounds=(min_bound*0.75, 3.0),
                    method='bounded', 
                    args=(tag,vol_coeff,modified_geometry_input,reference_area,reference_MAC_loc,reference_length))
            for i in range(len(modified_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"])-1):
                if modified_geometry_input[tag]["Xsec"].loc[i+1,"Airfoil Leading-Edge Y Location"] >= 0.0:
                    modified_geometry_input[tag]["Xsec"].loc[i+1,"Airfoil Leading-Edge Y Location"] += sol.x
                else: modified_geometry_input[tag]["Xsec"].loc[i+1,"Airfoil Leading-Edge Y Location"] -= sol.x
    return modified_geometry_input