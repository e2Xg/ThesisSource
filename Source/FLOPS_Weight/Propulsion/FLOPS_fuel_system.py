# -*- coding: utf-8 -*-

def FLOPS_fuel_system(FMXTOT,NTANK,FNENG):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.3.5 Fuel System, Tanks, Plumbing - Equation 92
    Variables:
        >>> FMXTOT : Aircraft Maximum Fuel Capacity (kg). Includes Wing, Fuselage and Auxiliary Tanks
        >>> NTANK : Number of Fuel Tanks
        >>> FNENG : Total Number of Engines
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units
    return (36.0*(FMXTOT**0.2)*(NTANK**0.5)*(FNENG**0.4))/kg2lb

if __name__ == "__main__":
    FMXTOT = 7000.0
    NTANK = 5
    FNENG = 2
    WFSYS = FLOPS_fuel_system(FMXTOT,NTANK,FNENG)
    print(WFSYS)

