# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_ac(geometry,fig = None, ax = None):
    """ Visualize Geometry Datablock"""
    if fig == None:
        fig = plt.figure(dpi = 200)
        ax = plt.axes(projection='3d')
    for tag in geometry.keys():
        if geometry[tag]["Type"] == "Fuselage":
            ax.plot(geometry[tag]["Data"].loc["Point Cloud","Value"][:,0],geometry[tag]["Data"].loc["Point Cloud","Value"][:,1],geometry[tag]["Data"].loc["Point Cloud","Value"][:,2])
            length = geometry[tag]["Data"].loc["Length","Value"]
        elif geometry[tag]["Type"] == "Wing":
            ApexX = geometry[tag]["Data"].loc["Planform Apex X-Coordinate","Value"]
            RootChord = geometry[tag]["Data"].loc["Planform Root Chord Length","Value"]
            TipChord = RootChord*geometry[tag]["Data"].loc["Planform Taper Ratio","Value"]
            SemiSpan = geometry[tag]["Data"].loc["Planform Span","Value"]/2.0
            Sweep = geometry[tag]["Data"].loc["Planform Leading-Edge Sweep Angle","Value"]
            TipLE = SemiSpan*np.tan(np.deg2rad(Sweep))
            TipApexX = TipLE + ApexX
            XPoints = [ApexX,TipApexX,TipApexX+TipChord,ApexX+RootChord,TipApexX+TipChord,TipApexX,ApexX]
            YPoints = [0.0,SemiSpan,SemiSpan,0.0,-SemiSpan,-SemiSpan,0.0]
            ZPoints = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]            
            ax.plot(XPoints,YPoints,ZPoints)
        elif geometry[tag]["Type"] == "Horizontal Tail" or geometry[tag]["Type"] == "Canard":
            ApexX = geometry[tag]["Data"].loc["Exposed Planform Apex X-Coordinate","Value"]
            ApexY = geometry[tag]["Data"].loc["Exposed Planform Apex Y-Coordinate","Value"]
            RootChord = geometry[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]
            TipChord = RootChord*geometry[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
            SemiSpan = geometry[tag]["Data"].loc["Exposed Planform Span","Value"]/2.0
            Sweep = geometry[tag]["Data"].loc["Exposed Planform Leading-Edge Sweep Angle","Value"]
            TipLE = SemiSpan*np.tan(np.deg2rad(Sweep))
            TipApexX = TipLE + ApexX
            XPoints = [ApexX,TipApexX,TipApexX+TipChord,ApexX+RootChord,ApexX]
            YPoints = [ApexY,ApexY+SemiSpan,ApexY+SemiSpan,ApexY,ApexY]
            ZPoints = [0.0,0.0,0.0,0.0,0.0]            
            ax.plot(XPoints,YPoints,ZPoints)
        elif geometry[tag]["Type"] == "Vertical Tail":
            ApexX = geometry[tag]["Data"].loc["Exposed Planform Apex X-Coordinate","Value"]
            ApexY = geometry[tag]["Data"].loc["Exposed Planform Apex Y-Coordinate","Value"]
            ApexZ = geometry[tag]["Data"].loc["Exposed Planform Apex Z-Coordinate","Value"]
            RootChord = geometry[tag]["Data"].loc["Exposed Planform Root Chord Length","Value"]
            TipChord = RootChord*geometry[tag]["Data"].loc["Exposed Planform Taper Ratio","Value"]
            SemiSpan = geometry[tag]["Data"].loc["Exposed Planform Span","Value"]/2.0
            Sweep = geometry[tag]["Data"].loc["Exposed Planform Leading-Edge Sweep Angle","Value"]
            TipLE = SemiSpan*np.tan(np.deg2rad(Sweep))
            TipApexX = TipLE + ApexX
            XPoints = [ApexX,TipApexX,TipApexX+TipChord,ApexX+RootChord,ApexX]
            YPoints = [ApexY,ApexY,ApexY,ApexY,ApexY]            
            ZPoints = [ApexZ,ApexZ+SemiSpan,ApexZ+SemiSpan,ApexZ,ApexZ]
            ax.plot(XPoints,YPoints,ZPoints)
    ax.auto_scale_xyz([0.0,length],[-length/2.0,length/2.0],[-length/2.0,length/2.0])	
    return fig, ax