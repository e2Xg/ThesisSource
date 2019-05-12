# -*- coding: utf-8 -*-

from Source.Postprocess.vsp_fuselage import vsp_fuselage
from Source.Postprocess.vsp_flying_surface import vsp_flying_surface

def vsp_aircraft(sfile,geometry_input,designid):
    file = open(sfile+".vspscript","w")
    file.write("void main()\n")
    file.write("{\n")
    vtswitch = 0
    for tag in geometry_input.keys():
        if geometry_input[tag]["Type"] == "Fuselage":
            vsp_fuselage(file,geometry_input[tag]["Xsec"])
        else:
            if geometry_input[tag]["Type"] == "Horizontal Tail":
                vsp_flying_surface(file,geometry_input[tag]["Xsec"],"HT",geometry_input[tag]["Type"])
            elif geometry_input[tag]["Type"] == "Vertical Tail": 
                if vtswitch == 0: 
                    vsp_flying_surface(file,geometry_input[tag]["Xsec"],"VT",geometry_input[tag]["Type"])
                    vtswitch += 1
            elif geometry_input[tag]["Type"] == "Canard":
                vsp_flying_surface(file,geometry_input[tag]["Xsec"],"C",geometry_input[tag]["Type"])
            elif geometry_input[tag]["Type"] == "Wing":
                vsp_flying_surface(file,geometry_input[tag]["Xsec"],"Wing",geometry_input[tag]["Type"])
    file.write("    Update();\n")
    file.write("    string fname = \"{}.vsp3\";\n".format(designid))
    file.write("    WriteVSPFile( fname, SET_ALL );\n")
    file.write("}\n")
    file.close()
    return