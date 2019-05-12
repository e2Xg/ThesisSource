# -*- coding: utf-8 -*-

def fus_sections2length(sections):
    """Calculate Fuselage Length From Sections"""
    return abs(sections[-1][0]-sections[0][0])
	
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
	length = fus_sections2length(sections)
	print(length)