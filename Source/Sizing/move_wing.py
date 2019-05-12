# -*- coding: utf-8 -*-

from Source.analyze_geometry import analyze_geometry

def move_wing(modified_geometry_input,design_input):
    modified_geometry_data = analyze_geometry(modified_geometry_input)
    for tag in modified_geometry_input.keys():
        #Component is fuselage
        if modified_geometry_input[tag]["Type"] == "Fuselage":
            fus_length = max(modified_geometry_input[tag]["Xsec"]["X-Location"])
    CGx = (design_input.loc["Aircraft CG Location Ratio","Value"]/100.0)*fus_length
    AC_MAC = design_input.loc["Aircraft Aerodynamic Center Relative Distance","Value"]/100.0
    for tag in modified_geometry_input.keys():
        #Component is wing
        if modified_geometry_input[tag]["Type"] == "Wing":
            MAC_length = modified_geometry_data[tag]["Data"].loc["Planform MAC Length","Value"]
            MAC_location = modified_geometry_data[tag]["Data"].loc["Planform MAC Location","Value"]
            AC = AC_MAC*MAC_length
            deltax = (CGx - MAC_location) - AC
            for i in range(len(modified_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge X Location"])):
                modified_geometry_input[tag]["Xsec"].loc[i,"Airfoil Leading-Edge X Location"] += deltax
    return modified_geometry_input