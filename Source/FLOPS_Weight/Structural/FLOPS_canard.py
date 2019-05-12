# -*- coding: utf-8 -*-

def FLOPS_canard(DG,SCAN,TRCAN,ACFF=0.83):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.5 Canard - Equation 55
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> SCAN : Canard Theoretical Area (m**2)
        >>> TRCAN : Canard Theoretical Taper Ratio
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    SCAN = SCAN*m2ft_pw2
    return (0.53*SCAN*(DG**0.2)*(TRCAN+0.5))/kg2lb*ACFF

if __name__ == "__main__":
    DG = 22000.0
    SCAN = 20.0
    TRCAN = 0.1
    WCAN = FLOPS_canard(DG,SCAN,TRCAN)
    print(WCAN)

