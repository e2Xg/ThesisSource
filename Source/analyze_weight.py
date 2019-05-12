# -*- coding: utf-8 -*-

from scipy.optimize import minimize_scalar

from Source.FLOPS_Weight.FLOPS_weight import FLOPS_weight

def analyze_weight(
            TR,SPAN,SW,ETR,ESPAN,ESW,TCA,
            QC_SWEEP,ULF,PCTL,SFLAP,NEW,
            XL,FNEF,SHT,NVERT,TRVT,
            SVT,ARVT,SWPVT,SCAN,TRCAN,
            WLDPAYLOAD,NFIN,SFIN,TRFIN,THRUST,
            WF,DF,VMAX,WPAINT,SWTWG,
            SWTHT,SWTVT,SWTFU,SWTCN,WENG,
            NENG,FPAREA,WARM,WMARG,WPAYLOAD,
            TOTVOLFUSF,FUELDENSITY,NTANK,
            LOW_BOUND = 100.0, UP_BOUND = 10**5
            ):
    """
    Description:
        Finds the design weight through minimize_scalar function
    Variables:
        >>> TR : Taper ratio of the wing
        >>> SPAN : Wing span (m)
        >>> SW : Reference wing area (m**2)
        >>> ETR : Exposed taper ratio of the wing
        >>> ESPAN : Exposed wing span (m)
        >>> ESW : Exposed wing area (m**2)
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
        >>> XL : Total Fuselage Length (m)
        >>> FNEF : Number of Fuselage Mounted Engines, Scaled to Account for Distributed Propulsion If Applicable
        >>> SHT :  Horizontal Tail Theoretical Area (m**2)
        >>> NVERT : Number of Vertical Tails
        >>> TRVT : Vertical Tail Theoretical Taper Ratio
        >>> SVT :  Vertical Tail Theoretical Area (m**2)
        >>> ARVT : Vertical Tail Aspect Ratio
        >>> SWPVT : Vertical Tail Sweep Angle At 25% Chord (deg)
        >>> SCAN : Canard Theoretical Area (m**2)
        >>> TRCAN : Canard Theoretical Taper Ratio
        >>> WLDPAYLOAD : Aircraft Maximum Payload Weight (kg)
        >>> NFIN : Number of Fins
        >>> SFIN : Fin Theoretical Area (m**2)
        >>> TRFIN : Fin Theoretical Taper Ratio
        >>> THRUST : Rated Thrust Of Each Scaled Engine (kg)
        >>> WF : Maximum Fuselage Width (m)
        >>> DF : Maximum Fuselage Depth (m)
        >>> VMAX : Maximum Mach Number,
        >>> WPAINT : Area Density of Paint For All Wetted Area kg/(m**2)
        >>> SWTWG : Wetted Area of Wings (m**2)
        >>> SWTHT : Wetted Area of Horizontal Tail (m**2)
        >>> SWTVT : Wetted Area of Vertical Tail (m**2)
        >>> SWTFU : Wetted Area of Fuselage (m**2)
        >>> SWTCN : Wetted Area of Canards (m**2)
        >>> WENG : Weight of each scaled engine (kg)
        >>> NENG : Total number of engines
        >>> FPAREA : Fuselage planform area (m**2)
        >>> WARM : Weight of the armament group (kg) (Includes thermal protection system or armor and fixed weapons)
        >>> WMARG : Empty weight margin (%) (Percentage of empty weight)
        >>> WPAYLOAD : Payload weight (kg)
        >>> TOTVOLFUSF : Total fuselage fuel volume (m**3)
        >>> FUELDENSITY : Fuel density (kg/m**3)
        >>> NTANK : Number of Fuel Tanks
        >>> LOW_BOUND : Lower bound of weight limit
        >>> UP_BOUND : Upper bound of weight limit
     """
    #Find minimum of weight function
    args = (    TR,SPAN,SW,ETR,ESPAN,ESW,TCA,
                QC_SWEEP,ULF,PCTL,SFLAP,NEW,
                XL,FNEF,SHT,NVERT,TRVT,
                SVT,ARVT,SWPVT,SCAN,TRCAN,
                WLDPAYLOAD,NFIN,SFIN,TRFIN,THRUST,
                WF,DF,VMAX,WPAINT,SWTWG,
                SWTHT,SWTVT,SWTFU,SWTCN,WENG,
                NENG,FPAREA,WARM,WMARG,WPAYLOAD,
                TOTVOLFUSF,FUELDENSITY,NTANK
                )
    
    def weight_difference(DG,*args):
        DG_final, weight_data = FLOPS_weight(DG,*args)
        return (DG - DG_final)**2
    
    sol = minimize_scalar(weight_difference, bounds=(LOW_BOUND, UP_BOUND), method='bounded', args=args)
    
    DG, weight_data = FLOPS_weight(sol.x,*args)
    return weight_data

if __name__ == "__main__":
    weight_data = analyze_weight(
            TR = 0.1,
            SPAN = 13.5,
            SW = 70.0,
            TCA = 0.04,
            QC_SWEEP = 20.0,
            ULF = 9.0*1.5,
            PCTL = 1.0,
            SFLAP = 70.0*0.3,
            NEW = 0,
            XL = 21.0,
            FNEF = 2,
            SHT = 26.0,
            NVERT = 2,
            TRVT = 0.11,
            SVT = 17.0,
            ARVT = 2.6,
            SWPVT = 22.0,
            SCAN = 20.0,
            TRCAN = 0.1,
            WLDPAYLOAD = 9000.0,
            NFIN = 2,
            SFIN = 17.0,
            TRFIN = 0.11,
            THRUST = 30000.0/2.20462262,
            WF = 3.4,
            DF = 2.02,
            VMAX = 2.0,
            WPAINT = 2.0,
            SWTWG = 60.0,
            SWTHT = 20.0,
            SWTVT = 20.0,
            SWTFU = 125.0,
            SWTCN = 0.0,
            WENG = 1500.0,
            NENG = 2,
            FPAREA = 3.4*21,
            WARM = 350 + 150,
            WMARG = 10.0,
            WPAYLOAD = 2500.0,
            TOTVOLFUSF = 8.1,
            FUELDENSITY = 800.0,
            NTANK = 5
            )
    print(weight_data)

