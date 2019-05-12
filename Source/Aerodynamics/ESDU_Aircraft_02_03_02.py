#Created by Mert TOKEL
#Changes:
# 25.06.2018 : Created

import numpy as np
	
def ESDU_Aircraft_02_03_02(l,N,A,k,B,V,ns):
	r"""Optimum Area Distribution And Associated Theoretical Transonic Drag-Rise For Aircraft At Zero Lift
	
	Parameters
	----------
		l	: Fuselage Length (m)
		N	: Nose Area (m**2)
		k	: Distance k (between 0 and length)
		A	: Area (m**2) at distance k
		B	: Base Area (m**2)
		V	: Aircraft Volume (m**3)
		ns	: Number of Cross-Sections Along Fuselage (integer)
	
	Returns
	-------
		dragcoef_rise : Calculate Optimum Drag Rise (Wave Drag Contribution)
		x_db : X Distribution Along the Fuselage (m) [depends on "ns"]
		S_x_db : Optimum Area Distribution (m**2)
	
	Raises
	------
	
	Notes
	-----
		
	References
	----------
	ESDU Aircraft 02.03.02
		Optimum Area Distribution And Associated Theoretical Transonic Drag-Rise For Aircraft At Zero Lift
		Issued September 1959
		With Amendment A, December 1982 - 9 Pages
		Derivation 1 : LORD, W.T. ARC R&M 3279 1962
	
	Examples
	--------	

	"""   
	#calculations
	N = N / (l**2.0)
	A = A / (l**2.0)
	k = k / l
	B = B / (l**2.0)
	V = V / (l**3.0)
	ns = ns - 1
	switch = 0 # If N<B
	if N > B :
		old_B = B
		B = N
		N = old_B
		k = 1.0 - k
		del old_B
		switch = 1
	V_i = V - 0.5*(N+B) #Equation 2.5
	F = (1.0/np.pi)*(np.arccos(1.0-2.0*k)-2.0*(1.0-2.0*k)*(k**0.5)*((1.0-k)**0.5)) #F(k) Function (REF: Equation 4 of Derivation 1)
	A_i = A - (N+(B-N)*F)
	X_i = 4.0*k*(1.0-k)
	G = 8.0*(k**(3.0/2.0))*(1.0-k)**(3.0/2.0) #G(k) Function (REF: Equation 10 of Derivation 1)
	Sig = 6*V_i*G/(np.pi*A_i)
	if Sig >= 9.0/8.0 :
		alpha = 1.0
		beta = 0.0
	elif Sig <= X_i :
		alpha = 0.0
		beta = 1.0
	elif X_i <= Sig and Sig <= 9.0/8.0 :
		alpha = ((9.0/8.0)*(Sig-X_i))/(Sig*((9.0/8.0)-X_i))
		beta = ((9.0/8.0)-Sig)/((9.0/8.0)-X_i)
	x_db = []; S_x_db = []; area_distribution = []
	for i in range(ns+1) :
		x = (1.0/ns)*i
		F_x = (1.0/np.pi)*(np.arccos(1.0-2.0*x)-2.0*(1.0-2.0*x)*(x**0.5)*((1.0-x)**0.5))
		G_x = 8.0*(x**(3.0/2.0))*(1.0-x)**(3.0/2.0)
		if i != 0 and i != ns :
			H_x_k = 2.0*(k*(1.0-x)+x*(1.0-k))*(k**0.5)*((1.0-k)**0.5)*(x**0.5)*((1.0-x)**0.5)-0.5*((k-x)**2.0)*np.log(abs((k*(1.0-x)+x*(1.0-k)+2.0*(k**0.5)*((1.0-k)**0.5)*(x**0.5)*((1.0-x)**0.5))/(k*(1.0-x)+x*(1.0-k)-2.0*(k**0.5)*((1.0-k)**0.5)*(x**0.5)*((1.0-x)**0.5))))
			H_x_k = H_x_k/(0.25*((4.0*k*(1.0-k))**(3.0/2.0)))
		elif i == 0 :
			H_x_k = 0.0
		elif i == ns :
			H_x_k = 0.0
		S_x_1 = N+(B-N)*F_x
		S_x_2 = (alpha*(16.0/(3.0*np.pi))*V_i)*G_x
		S_x_3 = (beta*A_i/(2.0*((k*(1.0-k))**0.5)))*H_x_k
		S_x = S_x_1 + S_x_2 + S_x_3
		area_distribution.append([x*l,S_x*(l**2.0)])
		S_x_db.append(S_x*(l**2.0))
		x_db.append(x*l)
	if switch == 1 :
		old = area_distribution
		area_distribution = []; S_x_db = []; x_db = []	
		for i in range(ns+1) :
			area_distribution.append([old[i][0],old[ns-i][1]])
			x_db.append(area_distribution[i][0])
			S_x_db.append(area_distribution[i][1])
	dragcoef_rise_1 = (4.0/np.pi)*((B-N)**2.0)
	dragcoef_rise_2 = (128.0/np.pi)*(V_i**2.0)
	dragcoef_rise_3 = (np.pi/4.0)*(A_i**2.0)/((k**2.0)*((1.0-k)**2.0))
	dragcoef_rise = dragcoef_rise_1 + alpha*dragcoef_rise_2 + beta*dragcoef_rise_3
	return dragcoef_rise*(l**2), x_db, S_x_db
	
if __name__ == "__main__":
	l = 10.0
	N = 0.785
	A = 3.142
	k = 3.0
	B = 0.196
	V = 20.0
	ns = 11
	dragcoef_rise, x_db, S_x_db = ESDU_Aircraft_02_03_02(l,N,A,k,B,V,ns)
	print(dragcoef_rise)
	for i in range(len(S_x_db)): print(x_db[i],S_x_db[i])
	from matplotlib import pyplot as plt
	plt.figure()
	plt.plot(x_db,S_x_db)
	plt.show()