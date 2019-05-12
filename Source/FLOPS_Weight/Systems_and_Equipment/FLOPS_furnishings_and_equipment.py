# -*- coding: utf-8 -*-

def FLOPS_furnishings_and_equipment(XL,VMAX,NFLCR = 1):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.7 Furnishings and Equipment - Equation 111
    Variables:
        >>> XL : Total fuselage length (m)
        >>> VMAX : Maximum Mach Number
        >>> NFLCR : Number of flight crew
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    XL = XL*m2ft
    return (80*NFLCR*(VMAX**0.38)*(XL**0.25))/kg2lb

if __name__ == "__main__":
    XL = 21
    VMAX = 2.0
    WFURN = FLOPS_furnishings_and_equipment(XL,VMAX,NFLCR = 1)
    print(WFURN)

