# -*- coding: utf-8 -*-

def vsp_general_xsec(i,xlp,zlp,w,h,mwl,tta,bta,ts,bs,us,ls):
    lines = []
    lines.append("    InsertXSec( fid, {}, XS_GENERAL_FUSE );\n".format(i-1))
    lines.append("    SetParmVal( fid, \"XLocPercent\", \"XSec_{}\", {} );\n".format(i,xlp))
    lines.append("    SetParmVal( fid, \"ZLocPercent\", \"XSec_{}\", {} );\n".format(i,zlp))
    lines.append("    SetParmVal( fid, \"Width\", \"XSecCurve_{}\", {} );\n".format(i,w))
    lines.append("    SetParmVal( fid, \"Height\", \"XSecCurve_{}\", {} );\n".format(i,h))
    lines.append("    SetParmVal( fid, \"MaxWidthLoc\", \"XSecCurve_{}\", {} );\n".format(i,mwl))
    lines.append("    SetParmVal( fid, \"TopTanAngle\", \"XSecCurve_{}\", {} );\n".format(i,tta))
    lines.append("    SetParmVal( fid, \"BotTanAngle\", \"XSecCurve_{}\", {} );\n".format(i,bta))
    lines.append("    SetParmVal( fid, \"TopStr\", \"XSecCurve_{}\", {} );\n".format(i,ts))
    lines.append("    SetParmVal( fid, \"BotStr\", \"XSecCurve_{}\", {} );\n".format(i,bs))
    lines.append("    SetParmVal( fid, \"UpStr\", \"XSecCurve_{}\", {} );\n".format(i,us))
    lines.append("    SetParmVal( fid, \"LowStr\", \"XSecCurve_{}\", {} );\n".format(i,ls))
    lines.append("    string xsec{} = GetXSec( xsec_surf, {} );\n".format(i,i))
    lines.append("    SetXSecContinuity( xsec{}, 1 );\n".format(i))
    lines.append("    SetParmVal( fid, \"TopLStrength\", \"XSec_{}\", 0.0 );\n".format(i))
    lines.append("    SetParmVal( fid, \"RightLStrength\", \"XSec_{}\", 0.0 );\n".format(i))
    return lines