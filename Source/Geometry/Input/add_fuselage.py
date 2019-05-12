# -*- coding: utf-8 -*-

import pandas as pd

def add_fuselage(
            geometry,
            capture_area_location,
            total_capture_area,
            nozzle_area_location,
            total_nozzle_area,
            tag="Fuselage",
            ):
        """Add Fuselage to Geometry Datablock"""
        #Fuselage
        geometry[tag] = dict()
        geometry[tag]["Type"] = "Fuselage"
        geometry[tag]["Capture Area Location"] = capture_area_location
        geometry[tag]["Total Capture Area"] = total_capture_area
        geometry[tag]["Nozzle Area Location"] = nozzle_area_location
        geometry[tag]["Total Nozzle Area"] = total_nozzle_area
        geometry[tag]["Plug Length"] = 0.0
        geometry[tag]["Type"] = "Fuselage"
        geometry[tag]["Xsec"] = pd.DataFrame(columns = [
                                                    "X-Location",
                                                    "Z-Location",
                                                    "Y-Coordinates",
                                                    "Z-Coordinates",
                                                    "Height",
                                                    "Width",
                                                    "MaxWidthLoc",
                                                    "TopTanAngle",
                                                    "BotTanAngle",
                                                    "TopStr",
                                                    "BotStr",
                                                    "UpStr",
                                                    "LowStr"
                                                    ])
        return geometry