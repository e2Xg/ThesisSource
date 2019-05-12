# -*- coding: utf-8 -*-

def FLOPS_electrical(XL,B,VMAX,NFLCR = 1, NFUSE = 1):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.5 Electrical- - Equation 107
    Variables:
        >>> XL : Total fuselage length (m)
        >>> B : Wing span (m)
        >>> VMAX : Maximum Mach Number
        >>> NFLCR : Number of flight crew
        >>> NFUSE : Number of fuselages
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    XL = XL*m2ft
    B = B*m2ft
    return (10*((XL+B)**0.85)*(NFUSE**0.27)*(VMAX**0.1)*(1.0+0.1*NFLCR))/kg2lb

if __name__ == "__main__":
    XL = 21
    B = 13.5
    VMAX = 2.0
    WELEC = FLOPS_electrical(XL,B,VMAX,NFLCR = 1, NFUSE = 1)
    print(WELEC)

