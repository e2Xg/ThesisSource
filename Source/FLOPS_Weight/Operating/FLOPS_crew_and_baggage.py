# -*- coding: utf-8 -*-

def FLOPS_crew_and_baggage(CARBAS = 0.0, NFLCR = 1.0):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 5.5.1 Crew and Baggage - Equation 120
    Variables:
        >>> CARBAS : Carrier based aircraft switch, where 1.0 is for carrier-based aircraft and 0.0 is for land-based aircraft
        >>> NFLCR : Number of flight crew
    """
    #Setting unit conversions
    kg2lb = 2.20462262
    #Convert SI to Imperial Units1
    return (NFLCR*(215-35*CARBAS))/kg2lb

if __name__ == "__main__":
    WFLCRB = FLOPS_crew_and_baggage(CARBAS = 0.0, NFLCR = 1.0)
    print(WFLCRB)

