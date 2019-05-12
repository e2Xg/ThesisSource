# -*- coding: utf-8 -*-

import numpy as np

def general_xsec(h,w,mwl,tta,bta,ts,bs,us,ls,cr=0.0,num_curve_points=5):
	"""Calculate XSec Coordinates Using General Cross Section Parameters"""
	def set_cubic_control_points(cntrl_pts):
		ncp = len(cntrl_pts)
		nseg = int((ncp-1)/3)
		m_Curve = []
		for i in range(nseg):
			c = []
			for j in range(4):
				k = i*3+j
				p = cntrl_pts[k]
				c.append([p, j])
			m_Curve.append(c)
		return m_Curve
	def Bezier_curve(x0,y0,x1,y1,x2,y2,x3,y3,num_curve_points=250):
		t = np.linspace(0.0,1.0,num_curve_points)
		x = (1-t)*((1-t)*((1-t)*x0+t*x1)+t*((1-t)*x1+t*x2))+t*((1-t)*((1-t)*x1+t*x2)+t*((1-t)*x2+t*x3))
		y = (1-t)*((1-t)*((1-t)*y0+t*y1)+t*((1-t)*y1+t*y2))+t*((1-t)*((1-t)*y1+t*y2)+t*((1-t)*y2+t*y3))
		return x, y
	#Top Control Points
	tp0 = np.array([0.0, h/2.0, 0.0])
	tp1 = tp0 + np.array([ts*w/3.0, 0.0, 0.0])
	x = w/2.0
	y = mwl*h/2.0
	tp3 = np.array([x, y, 0.0])
	x = (us*h*np.cos(np.deg2rad(tta)))/3.0
	y = (-us*h*np.sin(np.deg2rad(tta)))/3.0
	tp2 = tp3 - np.array([x, y, 0.0])
	#Bottom Control Points
	x = w/2.0
	y = mwl*h/2.0
	bp0 = np.array([x, y, 0.0])
	x = (-ls*h*np.cos(np.deg2rad(bta)))/3.0
	y = (-ls*h*np.sin(np.deg2rad(bta)))/3.0
	bp1 = bp0 + np.array([x, y, 0.0])
	bp3 = np.array([0.0, -h/2.0, 0.0])
	bp2 = bp3 - np.array([-bs*w/3.0, 0.0, 0.0])
	#Load Bezier Control Points
	bez_pnts = []
	bez_pnts.append( tp0 )
	bez_pnts.append( tp1 )
	bez_pnts.append( tp2 )
	bez_pnts.append( tp3 )
	ite = len(bez_pnts) - 1
	bez_pnts.append( bp1 )
	bez_pnts.append( bp2 )
	bez_pnts.append( bp3 )
	#Reflect
	nrp = len(bez_pnts)
	for i in range(2,nrp,1):
		p = bez_pnts[nrp - i]
		p[0] = -p[0]
		bez_pnts.append( p )
	bez_pnts = np.asarray(bez_pnts)
	#Get Roll Points
	offset = np.array([0.0, 0.0, 0.0])
	roll_pnts = []
	for i in range(ite,len(bez_pnts)-1,1):
		roll_pnts.append(bez_pnts[i] + offset)
	for i in range(1,ite,1):
		roll_pnts.append(bez_pnts[i] + offset)
	m_Curve = set_cubic_control_points(roll_pnts)
	x_all = np.array([])
	y_all = np.array([])
	for i in range(len(m_Curve)):
		C = m_Curve[i]
		if i == len(m_Curve)-1:
			x0 = C[0][0][0]
			y0 = C[0][0][1]
			x1 = C[1][0][0]
			y1 = C[1][0][1]
			x2 = C[2][0][0]
			y2 = C[2][0][1]
			x3 = 0.0
			y3 = h/2.0
		else:
			x0 = C[0][0][0]
			y0 = C[0][0][1]
			x1 = C[1][0][0]
			y1 = C[1][0][1]
			x2 = C[2][0][0]
			y2 = C[2][0][1]
			x3 = C[3][0][0]
			y3 = C[3][0][1]
		x, y = Bezier_curve(
			x0	= x0,
			y0	= y0,
			x1	= x1,
			y1	= y1,
			x2	= x2,
			y2	= y2,
			x3	= x3,
			y3	= y3,
			num_curve_points = num_curve_points
			)
		if i != 1 and i == 0:
			x = x[::-1]
			y = y[::-1]
			x_all = np.append(x_all[:-1],x)
			y_all = np.append(y_all[:-1],y)
		if i != 1 and i == 2:
			x_all = np.append(x_all[:-1],x)
			y_all = np.append(y_all[:-1],y)
	x_all0 = x_all[:-1]
	y_all0 = y_all[:-1]
	x_all = np.append(x_all0,-x_all[::-1])
	y_all = np.append(y_all0,y_all[::-1])
	return x_all, y_all
	
if __name__ == "__main__":
	h	= 5.79
	w	= 5.56818
	mwl	= 0.66364
	cr	= 0.0
	tta	= 22.9
	bta	= 41.72
	ts	= 0.83
	bs	= 1.38
	us	= 1.4
	ls	= 1.4
	x,y = general_xsec(h,w,mwl,tta,bta,ts,bs,us,ls,cr=0.0)
	from matplotlib import pyplot as plt
	plt.figure()
	plt.plot(x,y)
	plt.show()