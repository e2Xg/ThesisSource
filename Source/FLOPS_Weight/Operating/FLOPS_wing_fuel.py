# -*- coding: utf-8 -*-

def FLOPS_wing_fuel(SW,TCA,TR,SPAN,FULDEN = 1.0, FWMAX = 23.0):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.7 Fuel Capacity - Equation 133
    Variables:
        >>> FULDEN : Fuel density ratio alternate fuels compared to jet fuel (typical density of 6.7 lb/gal). The default value is 1.
        >>> FWMAX : Factor for wing fuel capacity equation. The default value is 23.
        >>> SW : Wing area (m**2)
        >>> TCA : Weighted average of the wing thickness to chord ratio
        >>> TR : Taper ratio of the wing
        >>> SPAN : Wing span (m)
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units1
    SW = SW*m2ft_pw2
    SPAN = SPAN*m2ft
    return (FULDEN*FWMAX*(SW**2)*TCA*(1.0-(TR/((1.0+TR)**2)))/SPAN)/kg2lb

if __name__ == "__main__":
    SW = 34.27
    TCA = 0.05
    TR = 0.25
    SPAN = 9.79
    print(FLOPS_wing_fuel(SW,TCA,TR,SPAN,FULDEN = 1.0, FWMAX = 23.0))

