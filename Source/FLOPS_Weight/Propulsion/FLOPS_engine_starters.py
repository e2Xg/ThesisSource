# -*- coding: utf-8 -*-

def FLOPS_engine_starters(NENG,THRUST):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.3.4 Miscellaneous Propulsion Systems: Engine Starters - Equation 90
    Variables:
        >>> NENG : Number of Engines
        >>> THRUST : Rated Thrust of Each Scaled Engine (kg)
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units
    THRUST = THRUST*kg2lb
    return (0.0072*THRUST*NENG)/kg2lb

if __name__ == "__main__":
    NENG = 2
    THRUST = 30000.0/2.20462262
    WSTART = FLOPS_engine_starters(NENG,THRUST)
    print(WSTART)

