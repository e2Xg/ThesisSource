# -*- coding: utf-8 -*-

def FLOPS_surface_controls(DG,SFLAP):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.1 Surface Controls - Equation 98
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> SFLAP : Total Movable Wing Surface Area Including Flaps, Elevators, Spoilers, etc. (m**2)
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    SFLAP = SFLAP*m2ft_pw2
    return (2.95*(SFLAP**0.45)*(DG**0.36))/kg2lb

if __name__ == "__main__":
    DG = 22000.0
    SFLAP = 70.0*0.3
    WSC = FLOPS_surface_controls(DG,SFLAP)
    print(WSC)

