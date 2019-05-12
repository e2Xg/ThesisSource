# -*- coding: utf-8 -*-

import numpy as np
	
def perimeter(x,y):
    """Estimate Perimeter of Simple Closed Curve"""
    #calculation
    perimeter = 0.0
    for i in range(len(x)-1): perimeter += np.sqrt((x[i+1]-x[i])**2+(y[i+1]-y[i])**2)
    return perimeter
	
if __name__ == "__main__":
	x = [0.0, 1.0, 1.0, 0.0, 0.0]
	y = [0.0, 0.0, 1.0, 1.0, 0.0]
	peri = perimeter(x,y)
	print(peri)
