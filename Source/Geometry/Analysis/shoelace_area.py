# -*- coding: utf-8 -*-

def shoelace_area(x, y):
    """Calculate Area of a Simple Closed Section"""
    #calculation
    n = len(x)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += abs(x[i]*y[j]-x[j]*y[i])
    return area/2.0
	
if __name__ == "__main__":
	x = [0.0, 1.0, 1.0, 0.0, 0.0]
	y = [0.0, 0.0, 1.0, 1.0, 0.0]
	area = shoelace_area(x,y)
	print(area)