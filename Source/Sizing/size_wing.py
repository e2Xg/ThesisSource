# -*- coding: utf-8 -*-

import numpy as np

def size_wing(modified_geometry_input,exposed_B,exposed_CR,exposed_TR,SWEEP):
    #Size Wing
    for tag in modified_geometry_input.keys():
        if modified_geometry_input[tag]["Type"] == "Wing":
            i = len(modified_geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"])
            modified_geometry_input[tag]["Xsec"].loc[i-1,"Airfoil Leading-Edge Y Location"] = exposed_B/2.0 + modified_geometry_input[tag]["Xsec"].loc[0,"Airfoil Leading-Edge Y Location"]
            modified_geometry_input[tag]["Xsec"].loc[0,"Airfoil Chord Length"] = exposed_CR
            modified_geometry_input[tag]["Xsec"].loc[i-1,"Airfoil Chord Length"] = exposed_CR*exposed_TR
            modified_geometry_input[tag]["Xsec"].loc[i-1,"Airfoil Leading-Edge X Location"] = modified_geometry_input[tag]["Xsec"].loc[0,"Airfoil Leading-Edge X Location"] + (exposed_B/2.0)*np.tan(np.deg2rad(SWEEP))
    return modified_geometry_input