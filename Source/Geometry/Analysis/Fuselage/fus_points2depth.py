# -*- coding: utf-8 -*-

def fus_points2depth(points):
    """Calculate Maximum Depth From Point Cloud """
    max_z = 0.0
    min_z = 0.0
    for point in points:
        if point[2] > max_z: max_z = point[2]
        if point[2] < min_z: min_z = point[2]
    return abs(max_z-min_z)