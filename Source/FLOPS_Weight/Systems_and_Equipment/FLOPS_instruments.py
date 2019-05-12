# -*- coding: utf-8 -*-

def FLOPS_instruments(XL, DF, FNEW, FNEF, NFLCR = 1, NFUSE = 1):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.3 Instruments - Equation 103
    Variables:
        >>> XL : Total Fuselage Length (m)
        >>> DF : Maximum fuselage depth (m)
        >>> FNEW : Number of wing mounted engines
        >>> FNEF : Number of fuselage mounted engines
        >>> NFLCR : Number of flight crew
        >>> NFUSE : Number of fuselages
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    XL = XL*m2ft
    DF = DF*m2ft
    return (0.09*NFUSE*XL*DF*(1.0+2.5*NFLCR+0.1*FNEW+0.15*FNEF))/kg2lb

if __name__ == "__main__":
    XL = 21
    DF = 2.02
    FNEW = 0
    FNEF = 2
    WIN = FLOPS_instruments(XL, DF, FNEW, FNEF, NFLCR = 1, NFUSE = 1)
    print(WIN)

