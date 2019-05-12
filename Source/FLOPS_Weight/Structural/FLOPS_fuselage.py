# -*- coding: utf-8 -*-

def FLOPS_fuselage(DG,XL,FNEF,VARSWP = 0.0,NFUSE = 1,ACFF=0.9):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.6 Fuselage - Equation 59
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> XL : Total Fuselage Length (m)
        >>> FNEF : Number of Fuselage Mounted Engines, Scaled to Account for Distributed Propulsion If Applicable
        >>> VARSWP : Wing Variable Sweep Weight Penalty Factor Ranging From 0.0 for Fixed-Geometry Wing to 1.0 for Full Variable-Sweep Wing
        >>> NFUSE : Number of Fuselages
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    XL = XL*m2ft
    return (0.15*(XL**0.9)*(DG**0.61)*(1.0+0.3*FNEF)*(1.0+0.33*VARSWP)*(NFUSE**0.3))/kg2lb*ACFF

if __name__ == "__main__":
    DG = 22000.0
    XL = 21.0
    FNEF = 2
    WFUSE = FLOPS_fuselage(DG,XL,FNEF,VARSWP = 0.0,NFUSE = 1)
    print(WFUSE)

