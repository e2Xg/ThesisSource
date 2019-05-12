# -*- coding: utf-8 -*-

def FLOPS_engine_oil(FNENG,FTHRST):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.5.3 Engine Oil - Equation 123
    Variables:
        >>> FNENG : Total number of engines
        >>> FTHRST : Rated thrust of each scaled engine (kg)
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units1
    FTHRST = FTHRST*kg2lb
    return (0.082*FNENG*(FTHRST**0.65))/kg2lb

if __name__ == "__main__":
    FNENG = 2
    FTHRST = 30000.0/2.20462262
    WOIL = FLOPS_engine_oil(FNENG,FTHRST)
    print(WOIL)

