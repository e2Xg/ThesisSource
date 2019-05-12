# -*- coding: utf-8 -*-

import copy

def size_fuselage(PL,geometry_input,PLxi = None):
    modified_geometry_input = copy.deepcopy(geometry_input)
    for tag in modified_geometry_input.keys():
        #Component is fuselage
        if modified_geometry_input[tag]["Type"] == "Fuselage":
            if PLxi == None: PLxi = int(len(modified_geometry_input[tag]["Xsec"]["X-Location"])/2)
            for i in range(len(modified_geometry_input[tag]["Xsec"]["X-Location"])):
                if i >= PLxi: modified_geometry_input[tag]["Xsec"].loc[i,"X-Location"] += PL
            modified_geometry_input[tag]["Plug Length"] = PL
    return modified_geometry_input