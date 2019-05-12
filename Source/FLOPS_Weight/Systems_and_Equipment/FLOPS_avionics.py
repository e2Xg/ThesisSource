# -*- coding: utf-8 -*-

def FLOPS_avionics(XL,DF,VMAX,CARBAS = 0.0,NFUSE = 1):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.6 Avionics- - Equation 109
    Variables:
        >>> XL : Total fuselage length (m)
        >>> DF : Maximum fuselage depth (m)
        >>> VMAX : Maximum Mach Number
        >>> CARBAS : Carrier based aircraft switch, where 1.0 is for carrier based aircraft and 0.0 is for land-based aircraft
        >>> NFUSE : Number of fuselages
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    XL = XL*m2ft
    DF = DF*m2ft
    return (0.41*((NFUSE*XL*DF)**1.3)*(1.0+0.37*CARBAS)*VMAX)/kg2lb

if __name__ == "__main__":
    XL = 21
    DF = 2.02
    VMAX = 2.0
    WAVONC = FLOPS_avionics(XL,DF,VMAX,CARBAS = 0.0,NFUSE = 1)
    print(WAVONC)

