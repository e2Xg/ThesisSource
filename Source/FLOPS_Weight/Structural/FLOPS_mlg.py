# -*- coding: utf-8 -*-

def FLOPS_mlg(WLDG,XL,DFTE = 1.0,ACFF=0.95):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.7 Landing Gear - Equation 63
    Variables:
        >>> WLDG : Aircraft Design Landing Weight (kg)
        >>> XL : Total Fuselage Length (m)
        >>> DFTE : Aircraft Type. Equal to 1.0 For Figther/Attack, 0.0 For All Others.
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    WLDG = WLDG*kg2lb
    XL = XL*m2ft
    XMLG = 0.75*XL
    return ((0.0117-0.0012*DFTE)*(WLDG**0.95)*(XMLG**0.43))/kg2lb*ACFF

if __name__ == "__main__":
    WLDG = 20000+2000.0
    XL = 17.0
    WLGM = FLOPS_mlg(WLDG,XL,DFTE = 1.0)
    print(WLGM)

