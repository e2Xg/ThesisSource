# -*- coding: utf-8 -*-

def add_point_xsec(
            x_location,
            z_location,
            geometry,
            tag="Fuselage"
            ):
        """Add Point Type Cross Section to Fuselage From Geometry Datablock"""
        #Fuselage
        y_coordinates = [0.0]
        z_coordinates = [0.0]
        for i in range(len(z_coordinates)): z_coordinates[i] += z_location
        geometry[tag]["Xsec"].loc[len(geometry[tag]["Xsec"])] = [x_location, z_location, y_coordinates, z_coordinates, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        return geometry