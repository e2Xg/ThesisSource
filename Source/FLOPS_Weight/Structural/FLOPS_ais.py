# -*- coding: utf-8 -*-

def FLOPS_ais(THRUST,NEF,WF,DF,VMAX,ACFF=0.85):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.9 Air Induction Systems - Equation 72 - (Wing Mounted Engines = 0.0 So Equation 72 is Modified)
    Variables:
        >>> THRUST : Rated Thrust Of Each Scaled Engine (kg)
        >>> NEF : Number of Fuselage Mounted Engines
        >>> WF : Maximum Fuselage Width (m)
        >>> DF : Maximum Fuselage Depth (m)
        >>> VMAX : Maximum Mach Number
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    #Convert SI to Imperial Units
    THRUST = THRUST*kg2lb
    WF = WF*m2ft
    DF = DF*m2ft
    return (1.06*((THRUST*NEF)**0.23)*((WF+DF)**1.4)*(VMAX**0.83))/kg2lb*ACFF

if __name__ == "__main__":
    THRUST = 30000.0/2.20462262
    NEF = 2.0
    WF = 3.4
    DF = 2.02
    VMAX = 2.0
    WAIS = FLOPS_ais(THRUST,NEF,WF,DF,VMAX)
    print(WAIS)

