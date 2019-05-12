# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from Source.analyze_geometry import analyze_geometry
from Source.Engine.engine_performance import engine_performance
from Source.analyze_weight import analyze_weight
from Source.analyze_aerodynamics import analyze_aerodynamics
from Source.analyze_point_performance import analyze_point_performance

def analyze(design_input,geometry_input,engine_input,point_performance_input=None,onlyobjectives=False):
    """
    Description:
        Finds geometrical, mass, aerodynamic properties of aircraft using all inputs
    Variables:
        >>> design_input : All design inputs data block.
        >>> geometry_input : All geometry input data block.
     """
    #Analyze geometrical, mass, aerodynamic properties
    # Analyze Geometry
    geometry_data = analyze_geometry(geometry_input)
    
    # Analyze Weight
    # Set parameters to 0.0
    XL = 0.0; TR = 0.0; SPAN = 0.0; SW = 0.0; AR = 0.0
    LE_SWEEP = 0.0; QC_SWEEP = 0.0; TCA = 0.0; ULF = 0.0
    PCTL = 1.0; SFLAP = 0.0; NEW = 0; FNEF = 0; SHT = 0.0
    NVERT = 0; TRVT = 0.0; SVT = 0.0; ARVT = 0.0; SWPVT = 0.0
    SCAN = 0.0; TRCAN = 0.0; WLDPAYLOAD = 0.0; NFIN = 0
    SFIN = 0.0; TRFIN = 0.0; THRUST = 0.0; WF = 0.0
    DF = 0.0; VMAX = 0.0; WPAINT = 0.0; SWTWG = 0.0
    SWTHT = 0.0; SWTVT = 0.0; SWTFU = 0.0; SWTCN = 0.0
    WENG = 0.0; NENG = 0; FPAREA = 0.0; WARM = 0.0
    WMARG = 0.0; WPAYLOAD = 0.0; TOTVOLFUSF = 0.0
    FUELDENSITY = 0.0; NTANK = 0

    # Set values based on design data
    VMAX = design_input.loc["Maximum Mach Number","Value"]
    ULF = design_input.loc["Ultimate Load Factor","Value"]
    NEW = design_input.loc["Number of Engines at Wing","Value"]
    FNEF = design_input.loc["Number of Engines at Fuselage","Value"]
    NENG = design_input.loc["Total Number of Engines","Value"]
    WARM = design_input.loc["Armanent Weight","Value"]
    WPAYLOAD = design_input.loc["Design Payload Weight","Value"]
    WLDPAYLOAD = design_input.loc["Maximum Payload Weight","Value"]
    WPAINT = design_input.loc["Paint Weight per Square Meters","Value"]
    WMARG = design_input.loc["Empty Weight Margin %","Value"]
    FUELDENSITY = design_input.loc["Fuel Density","Value"]
    NTANK = design_input.loc["Total Number of Fuel Tanks","Value"]
    #Set values based on engine data
    WENG = engine_input["Weight"]
    dummy, THRUST_N = engine_performance(
        engine_input = engine_input,
        number_of_engines = NENG,
        altitude = 0.0,
        mach = 0.0,
        setting = 3
        )
    THRUST = THRUST_N/9.81
    # Set values based on geometry data
    for tag in geometry_data.keys():
        #Component is fuselage
        if geometry_data[tag]["Type"] == "Fuselage":
            XL = geometry_data[tag]["Data"].loc["Length","Value"]
            WF = geometry_data[tag]["Data"].loc["Max Width","Value"]
            DF = geometry_data[tag]["Data"].loc["Max Depth","Value"]
            SWTFU = geometry_data[tag]["Data"].loc["Wetted Surface Area","Value"]
            FPAREA = WF*XL
            TOTVOLFUSF = (geometry_data[tag]["Data"].loc["Theoretical Volume","Value"] - design_input.loc["Main Systems Volume","Value"] - geometry_input[tag]["Total Capture Area"]*geometry_input[tag]["Plug Length"] - 0.35*geometry_data[tag]["Data"].loc["Theoretical Volume","Value"])*(design_input.loc["Fuselage Fuel Volume Ratio","Value"]/100.0)
        elif geometry_data[tag]["Type"] == "Wing":
            TR = geometry_data[tag]["Data"].loc["Planform Taper Ratio","Value"]
            SPAN = geometry_data[tag]["Data"].loc["Planform Span","Value"]
            SW = geometry_data[tag]["Data"].loc["Planform Area","Value"]
            ETR = geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
            ESPAN = geometry_data[tag]["Data"].loc["Exposed Planform Span","Value"]
            ESW = geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"]
            AR = (SPAN**2)/SW
            TCA = geometry_data[tag]["Data"].loc["Weighted Average of Exposed Thickness to Chord Ratio","Value"]
            LE_SWEEP = geometry_data[tag]["Data"].loc["Planform Leading-Edge Sweep Angle","Value"]
            QC_SWEEP = np.arctan(np.tan(LE_SWEEP)  - (4.0/AR)*((0.25)*((1.0-TR)/(1.0+TR))))
            SWTWG = geometry_data[tag]["Data"].loc["Wetted Surface Area","Value"]
            SFLAP += geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"]*design_input.loc["Flap Area Factor","Value"]
        elif geometry_data[tag]["Type"] == "Canard":
            SCAN = geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"]
            TRCAN = geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
            SWTCN = geometry_data[tag]["Data"].loc["Wetted Surface Area","Value"]
            SFLAP += SCAN*design_input.loc["Flap Area Factor","Value"]
        elif geometry_data[tag]["Type"] == "Horizontal Tail":
            SHT = geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"]
            SWTHT = geometry_data[tag]["Data"].loc["Wetted Surface Area","Value"]
            SFLAP += SHT*design_input.loc["Flap Area Factor","Value"]
        elif geometry_data[tag]["Type"] == "Vertical Tail":
            NVERT += 1
            TRVT = geometry_data[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
            SVT = geometry_data[tag]["Data"].loc["Exposed Planform Area","Value"]
            ARVT = geometry_data[tag]["Data"].loc["Exposed Planform Aspect Ratio","Value"]
            LE_SWEEPVT = geometry_data[tag]["Data"].loc["Exposed Planform Leading-Edge Sweep Angle","Value"]
            SWPVT = np.arctan(np.tan(LE_SWEEPVT)  - (4.0/ARVT)*((0.25)*((1.0-TRVT)/(1.0+TRVT))))
            SWTVT = geometry_data[tag]["Data"].loc["Wetted Surface Area","Value"]
            SFLAP += SVT*design_input.loc["Flap Area Factor","Value"]

    weight_data = analyze_weight(
            TR,
            SPAN,
            SW,
            ETR,
            ESPAN,
            ESW,
            TCA,
            QC_SWEEP,
            ULF,
            PCTL,
            SFLAP,
            NEW,
            XL,
            FNEF,
            SHT,
            NVERT,
            TRVT,
            SVT,
            ARVT,
            SWPVT,
            SCAN,
            TRCAN,
            WLDPAYLOAD,
            NFIN,
            SFIN,
            TRFIN,
            THRUST,
            WF,
            DF,
            VMAX,
            WPAINT,
            SWTWG,
            SWTHT,
            SWTVT,
            SWTFU,
            SWTCN,
            WENG,
            NENG,
            FPAREA,
            WARM,
            WMARG,
            WPAYLOAD,
            TOTVOLFUSF,
            FUELDENSITY,
            NTANK )

    #Analyze Aerodynamics
    aerodynamic_data = analyze_aerodynamics(
            max_mach = design_input.loc["Maximum Mach Number","Value"],
            max_altitude = design_input.loc["Maximum Altitude","Value"],
            geometry_data = geometry_data,
            cldesign = design_input.loc["Design Lift Coefficient","Value"],
            base_area = design_input.loc["Base Area","Value"],
            EWD = design_input.loc["Wave-Drag Efficiency Factor","Value"],
            )
    
    #Analyze Point Performance
    point_performance_data = None
    if isinstance(point_performance_input, pd.DataFrame):
        point_performance_data = analyze_point_performance(
            point_performance_input,
            design_input,
            engine_input,
            geometry_data,
            weight_data,
            aerodynamic_data,
            onlyobjectives=onlyobjectives)
    
    return geometry_data, weight_data, aerodynamic_data, point_performance_data

