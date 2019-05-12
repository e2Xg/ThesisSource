# -*- coding: utf-8 -*-

def FLOPS_hydraulics(FPAREA,SW,FNEW,FNEF,VMAX,HYDPR=3000,VARSWP=0.0):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.4 Hydraulics - Equation 105
    Variables:
        >>> FPAREA : Fuselage planform area (m**2)
        >>> SW : Reference wing area (m**2)
        >>> FNEW : Number of wing mounted engines
        >>> FNEF : Number of fuselage mounted engines
        >>> VMAX : Maximum Mach Number
        >>> HYDPR : Hydraulic system pressure (psi). The default value is 3000 psi.
        >>> VARSWP : Wing variable sweep weight penalty factor ranging from 0.0 for fixed-geometry to 1.0 for full variable-sweep wing.
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    FPAREA = FPAREA*m2ft_pw2
    SW = SW*m2ft_pw2
    return (0.55*(FPAREA + 0.27*SW)*(1.0+0.03*FNEW+0.5*FNEF)*((3000/HYDPR)**0.35)*(1.0+0.04*VARSWP)*(VMAX**0.1))/kg2lb

if __name__ == "__main__":
    FPAREA = 3.4*21 #Roughly estimated by Width x Length of fuselage
    SW = 70.0
    FNEW = 0
    FNEF = 2
    VMAX = 2.0
    WHYD = FLOPS_hydraulics(FPAREA,SW,FNEW,FNEF,VMAX,HYDPR=3000,VARSWP=0.0)
    print(WHYD)

