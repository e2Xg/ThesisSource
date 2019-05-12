# -*- coding: utf-8 -*-

from Source.Postprocess.vsp_general_xsec import vsp_general_xsec

def vsp_fuselage(file,fusxsec):
    fus_length = fusxsec.loc[len(fusxsec)-1,"X-Location"]
    file.write("    string fid = AddGeom( \"FUSELAGE\", \"\" );\n")
    file.write("    SetParmVal( fid, \"Length\", \"Design\", {} );\n".format(fus_length))
    file.write("    string xsec_surf = GetXSecSurf( fid, 0 );\n")
    file.write("    CutXSec( fid, 1 );\n")
    file.write("    CutXSec( fid, 1 );\n")
    file.write("    CutXSec( fid, 1 );\n")
    file.write("    Update();\n")
    file.write("    SetParmVal( fid, \"ZLocPercent\", \"XSec_{}\", {} );\n".format(0,fusxsec.loc[0,"Z-Location"]/fus_length))
    for i in range(1,len(fusxsec)-1):
        xlp = fusxsec.loc[i,"X-Location"]/fus_length
        zlp = fusxsec.loc[i,"Z-Location"]/fus_length
        w = fusxsec.loc[i,"Width"]
        h = fusxsec.loc[i,"Height"]
        mwl = fusxsec.loc[i,"MaxWidthLoc"]
        tta = fusxsec.loc[i,"TopTanAngle"]
        bta = fusxsec.loc[i,"BotTanAngle"]
        ts = fusxsec.loc[i,"TopStr"]
        bs = fusxsec.loc[i,"BotStr"]
        us = fusxsec.loc[i,"UpStr"]
        ls = fusxsec.loc[i,"LowStr"]
        lines = vsp_general_xsec(i,xlp,zlp,w,h,mwl,tta,bta,ts,bs,us,ls)
        for line in lines:
            file.write(line)
    file.write("    Update();\n")
    file.write("    SetParmVal( fid, \"ZLocPercent\", \"XSec_{}\", {} );\n".format(len(fusxsec)-1,fusxsec.loc[len(fusxsec)-1,"Z-Location"]//fus_length))
    return