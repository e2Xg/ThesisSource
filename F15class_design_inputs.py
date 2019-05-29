# -*- coding: utf-8 -*-

from Source.design_input import design_input
from Source.Main.save import save

design_input = design_input(
        max_mach = 2.0,
        design_cl = 0.2,
        max_altitude = 15000.0,
        max_g = 9.0,
        ult_g = 1.5*9.0,
        flap_area_factor = 0.3,
        neng_wing = 0,
        neng_fuselage = 2,
        Warm = 350 + 150,
        Wpayload = 948.0+180.0,
        Wmaxpayload = 948.0+180.0,
        Wpaint_sqm = 2.0,
        Wempty_margin = 10,
        fuel_density = 802.83,
        N_fuel_tanks = 5,
        fus_fuel_vol_ratio = 85,
        main_sys_vol = 9.291,
        base_area = 0.25,
        EWD = 2.0,
        CGX = 56.0,
        AC = -5.0,
        Vc = 0.0,
        Vht = 0.3,
        Vvt = 0.04
        )

save('F15class_design_input.pydata', design_input)