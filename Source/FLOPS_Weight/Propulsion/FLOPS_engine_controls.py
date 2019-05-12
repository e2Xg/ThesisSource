# -*- coding: utf-8 -*-

def FLOPS_engine_controls(NENG,THRUST,NFLCR = 1):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.3.4 Miscellaneous Propulsion Systems: Engine Controls - Equation 88
    Variables:
        >>> NENG : Number of Engines
        >>> THRUST : Rated Thrust of Each Scaled Engine (kg)
        >>> NFLCR : Number of Flight Crew. For Fighter/Attack Aircraft It is Assumed to Be 1.
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units
    THRUST = THRUST*kg2lb
    return (0.106*((NENG*THRUST*NFLCR)**0.55))/kg2lb

if __name__ == "__main__":
    NENG = 2
    THRUST = 30000.0/2.20462262
    WEC = FLOPS_engine_controls(NENG,THRUST,NFLCR = 1)
    print(WEC)

