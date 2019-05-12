# -*- coding: utf-8 -*-

import pandas as pd

def add_flying_surface(
            geometry,
            bank_angle = 0.0,
            tag = "Wing",
            attached="Fuselage",
            type = "Wing"
            ):
        """Add Flying Surface to Geometry Datablock"""
        #Flying Surface
        if type != "Wing" and type != "Horizontal Tail" and type != "Vertical Tail" and type != "Canard":
            print("Unknown flying surface type: {}".format(type))
            return
        geometry[tag] = dict()
        geometry[tag]["Type"] = type
        geometry[tag]["Attached Component Tag"] = attached
        geometry[tag]["Bank Angle"] = bank_angle
        geometry[tag]["Xsec"] = pd.DataFrame(columns = [
                                        "Airfoil Leading-Edge X Location",
                                        "Airfoil Leading-Edge Y Location",
                                        "Airfoil Leading-Edge Z Location",
                                        "Airfoil X/c-Coordinates",
                                        "Airfoil Z/c-Coordinates",
                                        "Airfoil Camber Function X/c Values",
                                        "Airfoil Camber Function Camber/c Values",
                                        "Airfoil Thickness Function X/c Values",
                                        "Airfoil Thickness Function Thickness/c Values",
                                        "Airfoil Chord Length",
                                        ])
        return geometry