# -*- coding: utf-8 -*-

import numpy as np

def vsp_flying_surface(file,fsxsec,tag,fstype):
    file.write("    string {}id = AddGeom( \"{}\", \"\" );\n".format(tag,"WING"))
    file.write("    SetParmVal( {}id, \"X_Rel_Location\", \"XForm\", {} );\n".format(tag,fsxsec.loc[0,"Airfoil Leading-Edge X Location"]))
    file.write("    SetParmVal( {}id, \"Y_Rel_Location\", \"XForm\", {} );\n".format(tag,fsxsec.loc[0,"Airfoil Leading-Edge Y Location"]))
    file.write("    SetParmVal( {}id, \"Z_Rel_Location\", \"XForm\", {} );\n".format(tag,fsxsec.loc[0,"Airfoil Leading-Edge Z Location"]))
    if fstype == "Vertical Tail":
        file.write("    SetParmVal( {}id, \"X_Rel_Rotation\", \"XForm\", {} );\n".format(tag,45.0))
    for i in range(1,len(fsxsec)):
        if i != 1: file.write("    InsertXSec( {}id, {}, XS_SIX_SERIES );\n".format(tag,i-1))
        xdist = fsxsec.loc[i,"Airfoil Leading-Edge X Location"] - fsxsec.loc[i-1,"Airfoil Leading-Edge X Location"]
        span = abs(fsxsec.loc[i,"Airfoil Leading-Edge Y Location"] - fsxsec.loc[i-1,"Airfoil Leading-Edge Y Location"])
        cr = fsxsec.loc[i-1,"Airfoil Chord Length"]
        ct = fsxsec.loc[i,"Airfoil Chord Length"]
        sweep = np.rad2deg(np.arctan(xdist/span))
        file.write("    SetParmVal( {}id, \"Span\", \"XSec_{}\", {} );\n".format(tag,i,span))
        file.write("    SetParmVal( {}id, \"Root_Chord\", \"XSec_{}\", {} );\n".format(tag,i,cr))
        file.write("    SetParmVal( {}id, \"Tip_Chord\", \"XSec_{}\", {} );\n".format(tag,i,ct))
        file.write("    SetParmVal( {}id, \"Sweep\", \"XSec_{}\", {} );\n".format(tag,i,sweep))
        if fstype == "Wing":
            file.write("    string {}xsec_surf{} = GetXSecSurf( {}id, 0 );\n".format(tag,i,tag))
            file.write("    ChangeXSecShape( {}xsec_surf{}, {}, XS_SIX_SERIES );\n".format(tag,i,i-1))
            file.write("    ChangeXSecShape( {}xsec_surf{}, {}, XS_SIX_SERIES );\n".format(tag,i,i))
            file.write("    Update();\n")
            file.write("    SetParmVal( {}id, \"ThickChord\", \"XSecCurve_{}\", {} );\n".format(tag,i-1,0.05))
            file.write("    SetParmVal( {}id, \"ThickChord\", \"XSecCurve_{}\", {} );\n".format(tag,i,0.05))
            file.write("    SetParmVal( {}id, \"IdealCl\", \"XSecCurve_{}\", {} );\n".format(tag,i-1,0.2))
            file.write("    SetParmVal( {}id, \"IdealCl\", \"XSecCurve_{}\", {} );\n".format(tag,i,0.2))
            file.write("    SetParmVal( {}id, \"A\", \"XSecCurve_{}\", {} );\n".format(tag,i-1,1.0))
            file.write("    SetParmVal( {}id, \"A\", \"XSecCurve_{}\", {} );\n".format(tag,i,1.0))
        else:
            file.write("    string {}xsec_surf{} = GetXSecSurf( {}id, 0 );\n".format(tag,i,tag))
            file.write("    ChangeXSecShape( {}xsec_surf{}, {}, XS_BICONVEX );\n".format(tag,i,i-1))
            file.write("    ChangeXSecShape( {}xsec_surf{}, {}, XS_BICONVEX );\n".format(tag,i,i))
            file.write("    Update();\n")
            file.write("    SetParmVal( {}id, \"ThickChord\", \"XSecCurve_{}\", {} );\n".format(tag,i-1,0.05))
            file.write("    SetParmVal( {}id, \"ThickChord\", \"XSecCurve_{}\", {} );\n".format(tag,i,0.05))
    return