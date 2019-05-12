# -*- coding: utf-8 -*-

import numpy as np
from Source.Geometry.Analysis.shoelace_area import shoelace_area
	
def fus_xsec_area(sections):
    """ Calculate Fuselage Cross Section Area """
    #calculation
    area = []
    for section in sections:
        area.append([section[0],shoelace_area(section[1],section[2])])
    area = np.array(area)
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
	area = fus_xsec_area(sections)
	print(area)
