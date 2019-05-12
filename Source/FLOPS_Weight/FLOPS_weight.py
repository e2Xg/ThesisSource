# -*- coding: utf-8 -*-
import pandas as pd

from Source.FLOPS_Weight.Structural.FLOPS_wing import FLOPS_wing
from Source.FLOPS_Weight.Structural.FLOPS_fuselage import FLOPS_fuselage
from Source.FLOPS_Weight.Structural.FLOPS_htail import FLOPS_htail
from Source.FLOPS_Weight.Structural.FLOPS_vtail import FLOPS_vtail
from Source.FLOPS_Weight.Structural.FLOPS_canard import FLOPS_canard
from Source.FLOPS_Weight.Structural.FLOPS_mlg import FLOPS_mlg
from Source.FLOPS_Weight.Structural.FLOPS_nlg import FLOPS_nlg
from Source.FLOPS_Weight.Structural.FLOPS_fin import FLOPS_fin
from Source.FLOPS_Weight.Structural.FLOPS_ais import FLOPS_ais
from Source.FLOPS_Weight.Structural.FLOPS_paint import FLOPS_paint
from Source.FLOPS_Weight.Propulsion.FLOPS_thrust_reversers import FLOPS_thrust_reversers
from Source.FLOPS_Weight.Propulsion.FLOPS_engine_controls import FLOPS_engine_controls
from Source.FLOPS_Weight.Propulsion.FLOPS_engine_starters import FLOPS_engine_starters
from Source.FLOPS_Weight.Propulsion.FLOPS_fuel_system import FLOPS_fuel_system
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_surface_controls import FLOPS_surface_controls
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_instruments import FLOPS_instruments
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_hydraulics import FLOPS_hydraulics
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_electrical import FLOPS_electrical
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_avionics import FLOPS_avionics
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_furnishings_and_equipment import FLOPS_furnishings_and_equipment
from Source.FLOPS_Weight.Systems_and_Equipment.FLOPS_air_conditioning import FLOPS_air_conditioning
from Source.FLOPS_Weight.Operating.FLOPS_crew_and_baggage import FLOPS_crew_and_baggage
from Source.FLOPS_Weight.Operating.FLOPS_unusable_fuel import FLOPS_unusable_fuel
from Source.FLOPS_Weight.Operating.FLOPS_engine_oil import FLOPS_engine_oil
from Source.FLOPS_Weight.Operating.FLOPS_wing_fuel import FLOPS_wing_fuel

def FLOPS_weight(
            DG,TR,SPAN,SW,ETR,ESPAN,ESW,TCA,
            QC_SWEEP,ULF,PCTL,SFLAP,NEW,
            XL,FNEF,SHT,NVERT,TRVT,
            SVT,ARVT,SWPVT,SCAN,TRCAN,
            WLDPAYLOAD,NFIN,SFIN,TRFIN,THRUST,
            WF,DF,VMAX,WPAINT,SWTWG,
            SWTHT,SWTVT,SWTFU,SWTCN,WENG,
            NENG,FPAREA,WARM,WMARG,WPAYLOAD,
            TOTVOLFUSF,FUELDENSITY,NTANK
            ):
    """
    Description:
        Program to calculate fighter aircraft weight based on "The Flight Optimization System Weights Estimation Method" - NASA/TM-2017-219627
        Section 6 Aircraft Weight Build-Up
    Variables:
        >>> DG : Design Gross Weight (kg)
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
        >>> NVERT : Number of Vertical Tails (fin)
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
     """
    #Toal Fuel Weight
    WWINGFUEL = FLOPS_wing_fuel(ESW,TCA,ETR,ESPAN,FULDEN = 1.0, FWMAX = 23.0)
    WFUSFUEL = TOTVOLFUSF*FUELDENSITY
    
    WFUEL = WFUSFUEL + WWINGFUEL
    
    #Structural Weight
    WWING = FLOPS_wing(DG,TR,SPAN,SW,TCA,QC_SWEEP,ULF,PCTL,SFLAP,NEW,FSTRT = 0.0,FAERT = 1.0,VARSWP = 0.0,FCOMP = 1.0)
    WFUSE = FLOPS_fuselage(DG,XL,FNEF,VARSWP = 0.0,NFUSE = 1)
    WHT = FLOPS_htail(DG,SHT,ULF)
    WVT = FLOPS_vtail(DG,NVERT,TRVT,SVT,ARVT,SWPVT)
    WCAN = FLOPS_canard(DG,SCAN,TRCAN)
    WLGM = FLOPS_mlg(DG-WPAYLOAD+WLDPAYLOAD,XL,DFTE = 1.0)
    WLGN = FLOPS_nlg(DG-WPAYLOAD+WLDPAYLOAD,XL,DFTE = 1.0,CARBAS = 1.0)
    WFIN = FLOPS_fin(DG,NFIN,SFIN,TRFIN)
    WAIS = FLOPS_ais(THRUST,FNEF,WF,DF,VMAX)
    WTPNT = FLOPS_paint(WPAINT,SWTWG = SWTWG,SWTHT = SWTHT,SWTVT = SWTVT,SWTFU = SWTFU,SWTCN = SWTCN)
    WSTRCT = WWING + WHT + WVT + WCAN + WFUSE + WLGM + WLGN + WFIN + WAIS + WTPNT
    
    #Propulsion Weight
    WTHR = FLOPS_thrust_reversers(THRUST,NENG)
    WEC = FLOPS_engine_controls(NENG,THRUST,NFLCR = 1)
    WSTART = FLOPS_engine_starters(NENG,THRUST)
    WFSYS = FLOPS_fuel_system(WFUEL,NTANK,NENG)
    
    WPRO = WENG*NENG + WTHR + WEC + WSTART + WFSYS
    
    #Systems and Equipment Weight
    WSC = FLOPS_surface_controls(DG,SFLAP)
    WIN = FLOPS_instruments(XL, DF, NEW, FNEF, NFLCR = 1,NFUSE = 1)
    WHYD = FLOPS_hydraulics(FPAREA,SW,NEW,FNEF,VMAX,HYDPR = 3000,VARSWP = 0.0)
    WELEC = FLOPS_electrical(XL,SPAN,VMAX,NFLCR = 1,NFUSE = 1)
    WAVONC = FLOPS_avionics(XL,DF,VMAX,CARBAS = 0.0,NFUSE = 1)
    WFURN = FLOPS_furnishings_and_equipment(XL,VMAX,NFLCR = 1)
    WAC = FLOPS_air_conditioning(WAVONC,NENG,THRUST,VMAX)
    
    WSYS = WSC + WIN + WHYD + WELEC + WAVONC + WARM + WFURN + WAC
    
    #Empty Weight
    WMARG =  WMARG/100.0*(WSTRCT + WPRO + WSYS)
    WWE = WSTRCT + WPRO + WSYS + WMARG
    
    #Operating Items Weight
    WFLCRB = FLOPS_crew_and_baggage(CARBAS = 0.0, NFLCR = 1.0)
    WUF = FLOPS_unusable_fuel(NENG,THRUST,SW)
    WOIL = FLOPS_engine_oil(NENG,THRUST)
    
    WOPIT = WFLCRB + WUF + WOIL
    
    #Operating Empty Weight
    
    WOWE = WWE + WOPIT
    
    #Zero Fuel Weight
    
    WZF = WOWE + WPAYLOAD

    #Total Design Weight
    
    DG_final = WZF + WFUEL
    
    #Return Dataframe 

    weight_data = pd.DataFrame(index = [], columns = ["Initial Value"])
    weight_data.loc["Wing","Initial Value"] = WWING
    weight_data.loc["Horizontal Tail","Initial Value"] = WHT
    weight_data.loc["Vertical Tail","Initial Value"] = WVT
    weight_data.loc["Canard","Initial Value"] = WCAN
    weight_data.loc["Fuselage","Initial Value"] = WFUSE
    weight_data.loc["Main Landing Gear","Initial Value"] = WLGM
    weight_data.loc["Nose Landing Gear","Initial Value"] = WLGN
    weight_data.loc["Fin","Initial Value"] = WFIN
    weight_data.loc["Air Induction","Initial Value"] = WAIS
    weight_data.loc["Paint","Initial Value"] = WTPNT
    weight_data.loc["Structure Group","Initial Value"] = WSTRCT
    weight_data.loc["Total Engine","Initial Value"] = WENG*NENG
    weight_data.loc["Thrust Reversers","Initial Value"] = WTHR
    weight_data.loc["Engine Controls","Initial Value"] = WEC
    weight_data.loc["Engine Starters","Initial Value"] = WSTART
    weight_data.loc["Fuel System","Initial Value"] = WFSYS
    weight_data.loc["Propulsion Group","Initial Value"] = WPRO
    weight_data.loc["Surface Controls","Initial Value"] = WSC
    weight_data.loc["Instruments","Initial Value"] = WIN
    weight_data.loc["Hydraulics","Initial Value"] = WHYD
    weight_data.loc["Electrical","Initial Value"] = WELEC
    weight_data.loc["Avionics","Initial Value"] = WAVONC
    weight_data.loc["Armaments","Initial Value"] = WARM
    weight_data.loc["Furnishings and Equipments","Initial Value"] = WFURN
    weight_data.loc["Air Conditioning","Initial Value"] = WAC
    weight_data.loc["Systems and Equipments Group","Initial Value"] = WSYS
    weight_data.loc["Margin","Initial Value"] = WMARG
    weight_data.loc["Empty Weight","Initial Value"] = WWE
    weight_data.loc["Crew","Initial Value"] = WFLCRB
    weight_data.loc["Unusable Fuel","Initial Value"] = WUF
    weight_data.loc["Engine Oil","Initial Value"] = WOIL
    weight_data.loc["Operating Group","Initial Value"] = WOPIT
    weight_data.loc["Operating Empty Weight","Initial Value"] = WOWE
    weight_data.loc["Design Mission Payload","Initial Value"] = WPAYLOAD
    weight_data.loc["Maximum Payload","Initial Value"] = WLDPAYLOAD
    weight_data.loc["Zero Fuel Design Mission Weight","Initial Value"] = WZF
    weight_data.loc["Zero Fuel Maximum Weight","Initial Value"] = WZF - WPAYLOAD + WLDPAYLOAD
    weight_data.loc["Wing Usable Fuel","Initial Value"] = WWINGFUEL
    weight_data.loc["Fuselage Usable Fuel","Initial Value"] = WFUSFUEL
    weight_data.loc["Total Usable Fuel","Initial Value"] = WFUEL
    weight_data.loc["Design Mission Takeoff Weight","Initial Value"] = DG_final
    weight_data.loc["Maximum Takeoff Weight","Initial Value"] = DG_final-WPAYLOAD+WLDPAYLOAD
    
    return DG_final, weight_data

if __name__ == "__main__":
    DG, weight_data = FLOPS_weight(
            DG = 22000.0,
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
            TOTVOLWB = 2.0,
            TOTVOLFUSF = 8.1,
            FUELDENSITY = 800.0,
            NTANK = 5
            )
    print(DG)

