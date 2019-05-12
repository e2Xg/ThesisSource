# -*- coding: utf-8 -*-

import pandas as pd

def design_input(
        max_mach,
        design_cl,
        max_altitude,
        max_g,
        ult_g,
        flap_area_factor,
        neng_wing,
        neng_fuselage,
        Warm,
        Wpayload,
        Wmaxpayload,
        Wpaint_sqm,
        Wempty_margin,
        fuel_density,
        N_fuel_tanks,
        fus_fuel_vol_ratio,
        main_sys_vol,
        base_area,
        EWD,
        CGX,
        AC,
        Vc,
        Vht,
        Vvt
        ):
    """
    Create Design Data for analysis
    """
    design_input = pd.DataFrame(index = [], columns = ["Value"])
    design_input.loc["Maximum Mach Number","Value"] = max_mach
    design_input.loc["Design Lift Coefficient","Value"] = design_cl
    design_input.loc["Maximum Altitude","Value"] = max_altitude
    design_input.loc["Maximum Load Factor","Value"] = max_g
    design_input.loc["Ultimate Load Factor","Value"] = ult_g
    design_input.loc["Flap Area Factor","Value"] = flap_area_factor
    design_input.loc["Number of Engines at Wing","Value"] = neng_wing
    design_input.loc["Number of Engines at Fuselage","Value"] = neng_fuselage
    design_input.loc["Total Number of Engines","Value"] = neng_wing + neng_fuselage
    design_input.loc["Armanent Weight","Value"] = Warm
    design_input.loc["Design Payload Weight","Value"] = Wpayload
    design_input.loc["Maximum Payload Weight","Value"] = Wmaxpayload
    design_input.loc["Paint Weight per Square Meters","Value"] = Wpaint_sqm
    design_input.loc["Empty Weight Margin %","Value"] = Wempty_margin
    design_input.loc["Fuel Density","Value"] = fuel_density
    design_input.loc["Total Number of Fuel Tanks","Value"] = N_fuel_tanks
    design_input.loc["Fuselage Fuel Volume Ratio","Value"] = fus_fuel_vol_ratio
    design_input.loc["Main Systems Volume","Value"] = main_sys_vol
    design_input.loc["Base Area","Value"] = base_area
    design_input.loc["Wave-Drag Efficiency Factor","Value"] = EWD
    design_input.loc["Aircraft CG Location Ratio","Value"] = CGX
    design_input.loc["Aircraft Aerodynamic Center Relative Distance","Value"] = AC
    design_input.loc["Canard Volume Coefficient","Value"] = Vc
    design_input.loc["Horizontal Tail Volume Coefficient","Value"] = Vht
    design_input.loc["Vertical Tail Volume Coefficient","Value"] = Vvt
        
    return design_input