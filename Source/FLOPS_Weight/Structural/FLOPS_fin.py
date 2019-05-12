# -*- coding: utf-8 -*-

def FLOPS_fin(DG,NFIN,SFIN,TRFIN):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.4 Fin - Equation 54
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> NFIN : Number of Fins
        >>> SFIN : Fin Theoretical Area (m**2)
        >>> TRFIN : Fin Theoretical Taper Ratio
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    SFIN = SFIN*m2ft_pw2
    return (0.32*(DG**0.3)*(SFIN**0.85)*(TRFIN+0.5)*NFIN)/kg2lb

if __name__ == "__main__":
    DG = 22000.0
    NFIN = 2
    SFIN = 17.0
    TRFIN = 0.11
    WFIN = FLOPS_fin(DG,NFIN,SFIN,TRFIN)
    print(WFIN)

