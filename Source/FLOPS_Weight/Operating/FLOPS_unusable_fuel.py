# -*- coding: utf-8 -*-

def FLOPS_unusable_fuel(FNENG,FTHRST,SW):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.5.2 Unusable Fuel - Equation 122
    Variables:
        >>> FNENG : Total number of engines
        >>> FTHRST : Rated thrust of each scaled engine (kg)
        >>> SW : Reference wing area (m**2)
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units1
    FTHRST = FTHRST*kg2lb
    SW = SW*m2ft_pw2
    return (11.5*FNENG*(FTHRST**0.2)+0.04*SW)/kg2lb

if __name__ == "__main__":
    FNENG = 2
    FTHRST = 30000.0/2.20462262
    SW = 70.0
    WUF = FLOPS_unusable_fuel(FNENG,FTHRST,SW)
    print(WUF)

