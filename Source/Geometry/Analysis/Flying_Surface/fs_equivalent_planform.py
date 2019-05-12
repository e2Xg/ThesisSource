# -*- coding: utf-8 -*-

import numpy as np

def fs_equivalent_planform(sections,comptype):
	r"""Geometric calculations of reference wing section parameters from exposed wing section parameters
	
	Parameters
	----------
	xloc: exposed x location of the wing (from fuselage nose) [default: meter]
	yloc: exposed y location of the wing (from fuselage centerline) [default: meter]
	cr : root chord array (from root section to tip section) [default: meter]
	le_sw : leading edge sweep angle array (from root section to tip section) [default: degree]
	tr : taper ratio array (from root section to tip section)
	b : span array (from root section to tip section) [default: meter]
	a : area array (from root section to tip section) [default: meter**2]
	
	Returns
	-------
	
	Raises
	------
	
	Notes
	-----
		
	References
	----------
	ESDU 76003
		Geometrical Properties of Cranked And Straight Tapered Wing Planforms
		Issued January 1976
		With Amendment A, October 1981
		Reference 1 : YATES, A.H. Notes on the mean aerodynamic chord and the mean aerodynamic centre of a wing.
			J.r. aeronaut. Soc., Vol. 56, p. 461, June 1952
		
	Examples
	--------

	"""
	#Estimate Wing Parameters from Sections
	xloc = min(sections[0][0])
	if comptype == "Wing": 
		yloc = sections[0][1]
		finalyloc = 0.0
	else: 
		yloc = 0.0
		finalyloc = sections[0][1]
	cr = []; b = []; le_sw = []; tr = []; a = []
	for i in range(len(sections)-1):
		cr.append(abs(max((sections[i][0]))-min(sections[i][0])))
		b.append(abs((sections[i][1])-sections[i+1][1]))
		le_sw.append(np.rad2deg(np.arctan((min(sections[i+1][0])-min(sections[i][0]))/b[i])))
		tr.append(abs(max((sections[i+1][0]))-min(sections[i+1][0]))/abs(max((sections[i][0]))-min(sections[i][0])))
		a.append((cr[i]+cr[i]*tr[i])*b[i]/2.0)
	#calculation
	sum_b = sum(b)+yloc
	cr0 = (2.0*sum(a))/(sum_b-yloc)-cr[-1]*tr[-1]
	c0 = (sum_b*cr0-yloc*cr[-1]*tr[-1])/(sum_b-yloc)
	tr0 = cr[-1]*tr[-1]/c0
	smc0 = c0*(1.0+tr0)/2.0
	mac0 = (2.0/3.0)*c0*(1.0+tr0+tr0**2.0)/(1.0+tr0)
	ar0 = 2.0*sum_b/smc0
	area0 = 2.0*sum_b*smc0
	lt = xloc
	m = len(b)
	for i in range(m): lt += b[i]*np.tan(np.deg2rad(le_sw[i]))
	ln = xloc
	for i in range(m-1): ln += (np.tan(np.deg2rad(le_sw[i]))-np.tan(np.deg2rad(le_sw[i+1])))*(b[i]-yloc)*(sum_b-b[i])/(sum_b-yloc)
	sweep0 = np.rad2deg(np.arctan((lt-ln)/(sum_b-yloc)))
	xloc0 = ln - yloc*np.tan(np.deg2rad(sweep0))
	x_1_4 = ((1.0+2.0*tr0)/12.0)*ar0*np.tan(np.deg2rad(sweep0))*c0+0.25*(mac0)
	return [xloc0, finalyloc, c0, tr0, 2.0*sum_b, area0, sweep0, ar0, mac0, x_1_4]
	