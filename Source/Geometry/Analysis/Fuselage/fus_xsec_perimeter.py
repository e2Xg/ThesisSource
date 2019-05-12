# -*- coding: utf-8 -*-

import numpy as np
from Source.Geometry.Analysis.perimeter import perimeter
	
def fus_xsec_perimeter(sections):
    """Calculate Fuselage Cross Section Perimeter"""
    #calculation
    perim = []
    for section in sections:
        perim.append([section[0],perimeter(section[1],section[2])])
    perim = np.array(perim)
    return perim
	
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
	perim = fus_xsec_perimeter(sections)
	print(perim)
