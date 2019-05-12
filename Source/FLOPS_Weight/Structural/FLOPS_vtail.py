# -*- coding: utf-8 -*-
import numpy as np
def FLOPS_vtail(DG,NVERT,TRVT,SVT,ARVT,SWPVT,ACFF=0.83):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.3 Vertical Tail - Equation 51
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> NVERT : Number of Vertical Tails
        >>> TRVT : Vertical Tail Theoretical Taper Ratio
        >>> SVT :  Vertical Tail Theoretical Area (m**2)
        >>> ARVT : Vertical Tail Aspect Ratio
        >>> SWPVT : Vertical Tail Sweep Angle At 25% Chord (deg)
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    SVT = SVT*m2ft_pw2
    return (0.212*(DG**0.3)*(TRVT+0.5)*(NVERT**0.7)*(SVT**0.94)*(ARVT**0.5)/((np.cos(np.deg2rad(SWPVT)))**1.5))/kg2lb*ACFF

if __name__ == "__main__":
    DG = 22000.0
    NVERT = 2
    TRVT = 0.11
    SVT = 17.0
    ARVT = 2.6
    SWPVT = 22.0
    WVT = FLOPS_vtail(DG,NVERT,TRVT,SVT,ARVT,SWPVT)
    print(WVT)

