# -*- coding: utf-8 -*-

import numpy as np

def fus_sections2points(sections):
    """ Convert Fuselage Sections To Points """
    points = []
    for i in range(len(sections)):
        for j in range(len(sections[i][1])):
            points.append([sections[i][0],sections[i][1][j],sections[i][2][j]])
    points = np.array(points)
    return points
	
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
	points = fus_sections2points(sections)
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	for p in points:
		ax.plot([p[0]],[p[1]],[p[2]],'o')
	plt.show()
	