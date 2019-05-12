# -*- coding: utf-8 -*-

import numpy as np

def fs_sections2points(sections):
    """Calculate Flying Surface Points From Sections"""
    points = []
    for i in range(len(sections)):
        for j in range(len(sections[i][0])):
            points.append([sections[i][0][j],sections[i][1],sections[i][2][j]])
    points = np.array(points)
    return points