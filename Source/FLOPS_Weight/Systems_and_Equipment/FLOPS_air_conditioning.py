# -*- coding: utf-8 -*-

def FLOPS_air_conditioning(WAVONC,FNENG,FTHRST,VMAX):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.4.8 Air Conditioning - Equation 114
    Variables:
        >>> WAVONC : Weight of the avionics system group (kg)
        >>> FNENG : Total number of engines
        >>> FTHRST : Rated thrust of each scaled engine (lb)
        >>> VMAX : Maximum Mach Number
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units
    WAVONC = WAVONC*kg2lb
    FTHRST = FTHRST*kg2lb
    return (0.075*WAVONC+0.37*FNENG*(FTHRST**0.6)*(VMAX**0.57))/kg2lb

if __name__ == "__main__":
    WAVONC = 1066.3077250126425
    FNENG = 2
    FTHRST = 30000.0/2.20462262
    VMAX = 2.0
    WAC = FLOPS_air_conditioning(WAVONC,FNENG,FTHRST,VMAX)
    print(WAC)

