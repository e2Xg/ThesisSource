# -*- coding: utf-8 -*-

def FLOPS_thrust_reversers(THRUST,NENG):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.3.3 Thrust Reversers - Equation 86
    Variables:
        >>> THRUST : Rated Thrust of Each Scaled Engine (kg)
        >>> NENG : Number of Engines
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units
    THRUST = THRUST*kg2lb
    TNAC = NENG+0.5*(NENG-2.0*(NENG/2.0))
    return (0.034*THRUST*TNAC)/kg2lb

if __name__ == "__main__":
    THRUST = 30000.0/2.20462262
    NENG = 2
    WTHR = FLOPS_thrust_reversers(THRUST,NENG)
    print(WTHR)

