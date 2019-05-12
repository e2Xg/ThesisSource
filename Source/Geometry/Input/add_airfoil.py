# -*- coding: utf-8 -*-

def add_airfoil(
            x_location,
            y_location,
            z_location,
            x_c_coords,
            z_c_coords,
            xc_c_coords,
            c_c_coords,
            xt_c_coords,
            t_c_coords,
            chord_length,
            geometry,
            tag="Wing"
            ):
        """Add Airfoil to Selected Flying Surface From Geometry Datablock"""
        #Flying Surface
        geometry[tag]["Xsec"].loc[len(geometry[tag]["Xsec"])] = [
                                    x_location,
                                    y_location,
                                    z_location,
                                    x_c_coords,
                                    z_c_coords,
                                    xc_c_coords,
                                    c_c_coords,
                                    xt_c_coords,
                                    t_c_coords,
                                    chord_length
                                    ]
        return geometry