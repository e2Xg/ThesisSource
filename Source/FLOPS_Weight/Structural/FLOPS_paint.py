# -*- coding: utf-8 -*-

def FLOPS_paint(WPAINT,SWTWG = 0.0,SWTHT = 0.0,SWTVT = 0.0,SWTFU = 0.0, SWTCN = 0.0):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.8 Paint - Equation 68
    Variables:
        >>> WPAINT : Area Density of Paint For All Wetted Area kg/(m**2)
        >>> SWTWG : Wetted Area of Wings (m**2)
        >>> SWTHT : Wetted Area of Horizontal Tail (m**2)
        >>> SWTVT : Wetted Area of Vertical Tail (m**2)
        >>> SWTFU : Wetted Area of Fuselage (m**2)
        >>> SWTCN : Wetted Area of Canards (m**2)
    """
    return WPAINT*(SWTWG+SWTHT+SWTVT+SWTFU+SWTCN)

if __name__ == "__main__":
    WPAINT = 2.0
    SWTWG = 60.0
    SWTHT = 20.0
    SWTVT = 20.0
    SWTFU = 125.0
    SWTCN = 0.0
    WTPNT = FLOPS_paint(WPAINT,SWTWG = SWTWG,SWTHT = SWTHT,SWTVT = SWTVT,SWTFU = SWTFU,SWTCN = SWTCN)
    print(WTPNT)

