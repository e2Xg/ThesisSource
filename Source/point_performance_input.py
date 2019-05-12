# -*- coding: utf-8 -*-

import pandas as pd

def point_performance_input(point_performance):
    point_performance_input = pd.DataFrame(index = [], columns = ["Name", "Parameters"])
    for i in range(len(point_performance)):
        point_performance_input.loc[i,"Name"] = point_performance[i][0]
        point_performance_input.loc[i,"Parameters"] = point_performance[i][1]
    return point_performance_input