# -*- coding: utf-8 -*-

from Source.Geometry.Input.general_xsec import general_xsec

def add_general_xsec(
            x_location,
            z_location,
            height,
            width,
            max_width_loc,
            top_tan_angle,
            bot_tan_angle,
            top_str,
            bot_str,
            up_str,
            low_str,
            geometry,
            tag="Fuselage"
            ):
        """Add Cross Section to Fuselage From Geometry Datablock Using General Cross Section Parameters"""
        #Fuselage
        y_coordinates, z_coordinates = general_xsec(
                                                    height,
                                                    width,
                                                    max_width_loc,
                                                    top_tan_angle,
                                                    bot_tan_angle,
                                                    top_str,
                                                    bot_str,
                                                    up_str,
                                                    low_str
                                                    )
        for i in range(len(z_coordinates)): z_coordinates[i] += z_location
        geometry[tag]["Xsec"].loc[len(geometry[tag]["Xsec"])] = [x_location, z_location, y_coordinates, z_coordinates, height, width, max_width_loc, top_tan_angle, bot_tan_angle, top_str, bot_str, up_str, low_str]
        return geometry