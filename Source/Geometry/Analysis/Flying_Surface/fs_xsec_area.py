# -*- coding: utf-8 -*-

import numpy as np

from Source.Geometry.Analysis.shoelace_area import shoelace_area
	
def fs_xsec_area(sections):
	"""Calculate Flying Surface Cross Section Area"""
	area = []
	for section in sections:
		area.append([section[1],shoelace_area(section[0],section[2])])
	area = np.array(area)
	return area