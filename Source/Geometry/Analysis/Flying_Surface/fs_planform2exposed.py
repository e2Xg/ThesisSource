# -*- coding: utf-8 -*-

import numpy as np

def fs_planform2exposed(geometry_data,geometry_input,tag):
        """Convert Planform Parameters to Exposed Planform Parameters"""
        geometry_data[tag]["Data"].loc["Exposed Planform Apex X-Coordinate","Value"] = geometry_data[tag]["Data"].loc["Planform Apex X-Coordinate","Value"]+geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"][0]*np.tan(np.deg2rad(geometry_data[tag]["Data"].loc["Planform Leading-Edge Sweep Angle","Value"]))
        geometry_data[tag]["Data"].loc["Exposed Planform Apex Y-Coordinate","Value"] = geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"][0]
        geometry_data[tag]["Data"].loc["Exposed Planform Apex Z-Coordinate","Value"] = geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Z Location"][0]
        x = geometry_data[tag]["Data"].loc["Planform Taper Ratio","Value"]*geometry_data[tag]["Data"].loc["Planform Span","Value"]/(2.0*(1.0-geometry_data[tag]["Data"].loc["Planform Taper Ratio","Value"]))
        geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"] = (1.0-geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"][0]/(x+geometry_data[tag]["Data"].loc["Planform Span","Value"]/2.0))*geometry_data[tag]["Data"].loc["Planform Root Chord Length","Value"]
        geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"] = (geometry_data[tag]["Data"].loc["Planform Taper Ratio","Value"]*geometry_data[tag]["Data"].loc["Planform Root Chord Length","Value"])/geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]
        geometry_data[tag]["Data"].loc["Exposed Planform Span","Value"] = ((geometry_data[tag]["Data"].loc["Planform Span","Value"]/2.0) - geometry_input[tag]["Xsec"]["Airfoil Leading-Edge Y Location"][0])*2.0
        geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"] = (geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]+geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]*geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"])*geometry_data[tag]["Data"].loc["Exposed Planform Span","Value"]/2.0
        geometry_data[tag]["Data"].loc["Exposed Planform Leading-Edge Sweep Angle","Value"] = geometry_data[tag]["Data"].loc["Planform Leading-Edge Sweep Angle","Value"]
        geometry_data[tag]["Data"].loc["Exposed Planform Aspect Ratio","Value"] = (geometry_data[tag]["Data"].loc["Exposed Planform Span","Value"]**2.0)/geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"]
        geometry_data[tag]["Data"].loc["Exposed Planform MAC Length","Value"] = (2.0/3.0)*geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]*(1.0+geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]+geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]**2.0)/(1.0+geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"])
        halfb = geometry_data[tag]["Data"].loc["Exposed Planform Span","Value"] / 2.0
        lesweep = np.deg2rad(geometry_data[tag]["Data"].loc["Exposed Planform Leading-Edge Sweep Angle","Value"])
        exp_apex_x = geometry_data[tag]["Data"].loc["Exposed Planform Apex X-Coordinate","Value"]
        root_te = exp_apex_x + geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]
        tip_te = exp_apex_x + halfb*np.tan(lesweep) + geometry_data[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]*geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
        ar = geometry_data[tag]["Data"].loc["Exposed Planform Aspect Ratio","Value"]
        tr = geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
        geometry_data[tag]["Data"].loc["Exposed Planform Trailing-Edge Sweep Angle","Value"] = np.rad2deg(np.arctan((tip_te-root_te)/halfb))
        geometry_data[tag]["Data"].loc["Exposed Planform Quarter-Chord Sweep Angle","Value"] = np.rad2deg(np.arctan(( np.tan(lesweep)-4.0/ar*(-0.75*((1-tr)/(1+tr)))) ))
        return geometry_data