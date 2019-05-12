# -*- coding: utf-8 -*-

def fus_points2width(points):
    """Calculate Maximum Width From Point Cloud"""
    max_y = 0.0
    min_y = 0.0
    for point in points:
        if point[1] > max_y: max_y = point[1]
        if point[1] < min_y: min_y = point[1]
    return abs(max_y-min_y)