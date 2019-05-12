# -*- coding: utf-8 -*-

import numpy as np

def fs_chordwise_area_distribution(flying_surface,type,numpnts = 30):
    """Calculate Flying Surface Chordwise Area Distribution"""
    pt1 = []; pt2 = []; points = []; t_c_x =[] ; t_c = []; c = []
    for i in range(len(flying_surface["Airfoil Leading-Edge X Location"])):
        pt1.append(flying_surface.loc[i,"Airfoil Leading-Edge X Location"])
        pt2.append(pt1[i]+flying_surface.loc[i,"Airfoil Chord Length"])
        t_c_x.append(np.asarray(flying_surface.loc[i,"Airfoil Thickness Function X/c Values"]))
        t_c.append(np.asarray(flying_surface.loc[i,"Airfoil Thickness Function Thickness/c Values"]))
        c.append(np.asarray(flying_surface.loc[i,"Airfoil Chord Length"]))
        points.append(pt1[i])
        points.append(pt2[i])
    points.sort()
    y = max(flying_surface["Airfoil Leading-Edge Y Location"])-min(flying_surface["Airfoil Leading-Edge Y Location"])
    ys = np.linspace(0.0,y,numpnts)
    y_db = []
    all_points = np.linspace(min(points),max(points),numpnts)
    for y_ in ys:
        t_db = []
        for j in range(len(all_points)):
            le_pnt_x = np.interp(y_,[0.0,y],[pt1[0],pt1[-1]])
            te_pnt_x = np.interp(y_,[0.0,y],[pt2[0],pt2[-1]])
            if all_points[j] <= le_pnt_x or all_points[j] >= te_pnt_x: t_db.append(0.0)
            else:
                chord = np.interp(y_,[0.0,y],[c[0],c[1]])
                chord_percentage = (all_points[j]-le_pnt_x)/chord
                t_root = np.interp(chord_percentage,t_c_x[0][::-1],t_c[0][::-1])*c[0]
                t_tip = np.interp(chord_percentage,t_c_x[-1][::-1],t_c[-1][::-1])*c[-1]
                t_db.append(np.interp(y_,[0.0,y],[t_root,t_tip]))
        y_db.append(t_db)
    y_db = np.array(y_db)
    if type == "Vertical Tail": symmetry = 1.0
    else: symmetry = 2.0
    trapz_db = []
    for k in range(len(all_points)):
        trapz_db.append(symmetry*np.trapz(y_db[:,k],ys))
    trapz_db = np.array(trapz_db)
    return [all_points, trapz_db]