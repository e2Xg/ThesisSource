# -*- coding: utf-8 -*-

def FLOPS_nlg(WLDG,XL,DFTE = 1.0,CARBAS = 1.0,ACFF=0.95):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.7 Landing Gear - Equation 64
    Variables:
        >>> WLDG : Aircraft Design Landing Weight (kg)
        >>> XL : Total Fuselage Length (m)
        >>> DFTE : Aircraft Type. Equal to 1.0 For Figther/Attack, 0.0 For All Others.
        >>> CARBAS : Carrier Based Aircraft Switch, Where 1.0 is for Carrier-Based Aircraft and 0.0 is For Land-Based Aircraft
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    WLDG = WLDG*kg2lb
    XL = XL*m2ft
    XMLG = 0.75*XL
    XNLG = 0.7*XMLG
    return ((0.048-0.008*DFTE)*(WLDG**0.67)*(XNLG**0.43)*(1.0+0.8*CARBAS))/kg2lb*ACFF

if __name__ == "__main__":
    WLDG = 20000.0+9000.0
    XL = 21.0
    WLGN = FLOPS_nlg(WLDG,XL,DFTE = 1.0,CARBAS = 1.0)
    print(WLGN)

