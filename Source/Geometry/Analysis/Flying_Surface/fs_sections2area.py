# -*- coding: utf-8 -*-

from scipy.spatial import ConvexHull

from Source.Geometry.Analysis.Flying_Surface.fs_sections2points import fs_sections2points
from Source.Geometry.Analysis.shoelace_area import shoelace_area

def fs_sections2area(sections):
    """ Calculate Flying Surface Area From Sections"""
    area = 0.0
    for i in range(1,len(sections)):
        points = fs_sections2points([sections[i-1],sections[i]])
        hull = ConvexHull(points,qhull_options = 'QJ')
        area_1 = shoelace_area(sections[i-1][0],sections[i-1][2])
        area_2 = shoelace_area(sections[i][0],sections[i][2])
        area += hull.area-area_1-area_2
    return area