# -*- coding: utf-8 -*-

from scipy.spatial import ConvexHull

from Source.Geometry.Analysis.Flying_Surface.fs_sections2points import fs_sections2points

def fs_sections2volume(sections):
    """Calculate Flying Surface Volume From Sections"""
    volume = 0.0
    for i in range(1,len(sections)):
        points = fs_sections2points([sections[i-1],sections[i]])
        hull = ConvexHull(points,qhull_options = 'QJ')
        volume += hull.volume
    return volume