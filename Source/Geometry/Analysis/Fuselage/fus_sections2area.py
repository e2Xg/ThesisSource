# -*- coding: utf-8 -*-

from scipy.spatial import ConvexHull

from Source.Geometry.Analysis.Fuselage.fus_sections2points import fus_sections2points
from Source.Geometry.Analysis.shoelace_area import shoelace_area

def fus_sections2area(sections):
    """Calculate Fuselage Area Using Sections"""
    area = 0.0
    for i in range(1,len(sections)):
        points = fus_sections2points([sections[i-1],sections[i]])
        hull = ConvexHull(points,qhull_options = 'QJ')
        area_1 = shoelace_area(sections[i-1][1],sections[i-1][2])
        area_2 = shoelace_area(sections[i][1],sections[i][2])
        area += hull.area-area_1-area_2
    return area
	
if __name__ == "__main__":
	section0 = [0.0,
		[0.0],
		[0.0]
		]
	section1 = [5.0,
		[0.0,1.0,0.0,-1.0,0.0],
		[1.0,0.0,-1.0,0.0,1.0]
		]
	section2 = [10.0,
		[0.0,1.0,0.0,-1.0,0.0],
		[1.0,0.0,-1.0,0.0,1.0]
		]
	section3 = [10.0,
		[0.0],
		[0.0]
		]
	sections = [section0,section1,section2,section3]
	area = fus_sections2area(sections)
	print(area)