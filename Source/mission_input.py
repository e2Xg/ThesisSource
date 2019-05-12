# -*- coding: utf-8 -*-

import pandas as pd

def mission_input(mission):
    mission_input = pd.DataFrame(index = [], columns = ["Name", "Parameters"])
    for i in range(len(mission)):
        mission_input.loc[i,"Name"] = mission[i][0]
        mission_input.loc[i,"Parameters"] = mission[i][1]
    return mission_input