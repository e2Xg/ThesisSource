# -*- coding: utf-8 -*-

from scipy.spatial import ConvexHull

from Source.Geometry.Analysis.Fuselage.fus_sections2points import fus_sections2points

def fus_sections2volume(sections):
    """ Calculate Fuselage Volume From The Sections """
    volume = 0.0
    for i in range(1,len(sections)):
        points = fus_sections2points([sections[i-1],sections[i]])
        hull = ConvexHull(points,qhull_options = 'QJ')
        volume += hull.volume
    return volume
	
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
	volume = fus_sections2volume(sections)
	print(volume)