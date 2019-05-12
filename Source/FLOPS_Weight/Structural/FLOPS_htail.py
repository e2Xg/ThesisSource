# -*- coding: utf-8 -*-

def FLOPS_htail(DG,SHT,ULF,ACFF=0.83):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.2 Horizontal Tail - Equation 47
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> SHT :  Horizontal Tail Theoretical Area (m**2)
        >>> ULF : Structural Ultimate Load Factor
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    SHT = SHT*m2ft_pw2
    return (0.002*(SHT**0.87)*((ULF*DG)**0.66))/kg2lb*ACFF

if __name__ == "__main__":
    DG = 22000.0
    SHT = 26.0
    ULF = 9*1.5
    WHT = FLOPS_htail(DG,SHT,ULF)
    print(WHT)

