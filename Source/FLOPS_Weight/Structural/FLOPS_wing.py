# -*- coding: utf-8 -*-
import numpy as np

def FLOPS_wing(DG,TR,SPAN,SW,TCA,QC_SWEEP,ULF,PCTL,SFLAP,NEW,FSTRT = 0.0,FAERT = 1.0,VARSWP = 0.0,FCOMP = 1.0, CAYF = 1.0, ACFF = 0.85):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.2.1 Wing - Equation 10(fixed) to Equation 45
    Variables:
        >>> DG : Design Gross Weight (kg)
        >>> TR : Taper ratio of the wing
        >>> SPAN : Wing span (m)
        >>> SW : Reference wing area (m**2)
        >>> TCA : Weighted average of the wing thickness to chord ratio
        >>> QC_SWEEP : Quarter chord sweep angle of the wing (deg)
        >>> ULF : Structual ultimate load factor
        >>> PCTL : Fraction of load carried by the defined wing
        >>> SFLAP : Total movable wing surface area including flaps elevators, spoilers, etc. (m**2)
        >>> NEW : Number of wing mounted engines
        >>> FSTRT : Wing strut bracing factor ranging from 0.0 for no wing strut to 1.0 for full genefit from strut bracing
        >>> FAERT : Aeroelastic tailoring factor used in the design of the wing raging from 0.0 for no aeroeastic tailoring to 1.0 for maximum aeroelastic tailoring
        >>> VARSWP : Wing variable sweep weight penalty factor ranging from 0.0 for fixed-geometry wing to 1.0 for full variable-sweep wing
        >>> FCOMP : Composite utilization factor for wing structure ranging from 0.0 for no composites to 1.0 for maximum use of composites
        >>> CAYF : Multiple fuselace factor. 1.0 for single fuselage and 0.5 for multiple fuselages.
        >>> ACFF : Advanced composites fudge factor
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    m2ft = 3.2808399
    m2ft_pw2 = m2ft*m2ft
    #Convert SI to Imperial Units
    DG = DG*kg2lb
    SPAN = SPAN*m2ft
    SW = SW*m2ft_pw2
    SFLAP = SFLAP*m2ft_pw2
    #Wing Strut Bracting Factor - Equation 11
    EMS = 1.0-0.25*FSTRT
    #Wing Aspect Ratio
    AR = (SPAN**2)/SW
    #Tangent of the 3/4 Chord Wing Sweep Angle - Equation 14
    TLAM = np.tan(np.deg2rad(QC_SWEEP))-2.0*(1.0-TR)/(AR*(1.0+TR))
    #Sine of the 3/4 Chord Wing Sweep Angle - Equation 13
    SLAM = TLAM/np.sqrt(1.0+(TLAM**2))
    #The Factor C4 - Equation 15
    C4 = 1.0-0.5*FAERT
    #The Factor C6 - Equation 16
    C6 = 0.5*FAERT-0.16*FSTRT
    #The Factor CAYA - Equation 17
    if AR <= 5: CAYA = 0.0
    else: CAYA = AR - 5.0
    #Wing Sweep Factor Including Aeroelastic Tailoring - Equation 12
    CAYL = (1.0-(SLAM**2))*(1.0+C6*(SLAM**2)+0.03*CAYA*C4*SLAM)
    #Wing Equivalent Bending Material Factor - Equation 10
    BT = 0.215*(0.37+0.7*TR)*((SPAN**2/SW)**EMS)/(CAYL*TCA)
    #Wing Weight Equation Constants - Table 1
    A1 = 6.8; A2 = 0.0; A3 = 0.12; A4 = 0.65; A5 = 0.62; A6 = 0.8; A7 = 1.2
    #The factor VFACT - Equation 34
    if VARSWP <= 0.0: VFACT = 1.0
    else: VFACT = 1.0+VARSWP*((0.96/np.cos(np.deg2rad(QC_SWEEP)))-1.0)
    #Wing Bending Material Weight - Equation 33
    W1NIR = A1*BT*(1.0+(np.sqrt(A2/SPAN)))*ULF*SPAN*(1.0-0.4*FCOMP)*(1.0-0.1*FAERT)*CAYF*VFACT*PCTL/(10**6)
    #Total Wing Shear Material and Control Surface Weight - Equation 35
    W2 = A3*(1.0-0.17*FCOMP)*(SFLAP**A4)*(DG**A5)
    #Total Wing Miscellaneous Items Weight - Equation 36
    W3 = A6*(1.0-0.3*FCOMP)*(SW**A7)
    #Propulsion System Pod Inertia Relief Factor - Equation 38
    CAYE = 1.0-0.03*NEW
    #Wing Bending Material Weight Inertia Relief Adjustment - Equation 37
    W1 = ((DG*CAYE*W1NIR+W2+W3)/(1.0+W1NIR)) - W2 - W3
    return (W1+W2+W3)/kg2lb*ACFF

if __name__ == "__main__":
    DG = 22000.0
    TR = 0.1
    SPAN = 13.5
    SW = 70.0
    TCA = 0.04
    QC_SWEEP = 20.0
    ULF = 9.0*1.5
    PCTL = 1.0
    SFLAP = 0.3*SW
    NEW = 0
    WWING = FLOPS_wing(DG,TR,SPAN,SW,TCA,QC_SWEEP,ULF,PCTL,SFLAP,NEW,FSTRT = 0.0,FAERT = 1.0,VARSWP = 0.0,FCOMP = 1.0)
    print(WWING)

