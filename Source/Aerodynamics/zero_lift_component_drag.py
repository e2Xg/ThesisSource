# -*- coding: utf-8 -*-

from Source.Aerodynamics.component_build_up import component_build_up
from Source.Aerodynamics.flat_plate_skin_friction_coefficient import flat_plate_skin_friction_coefficient
from Source.Aerodynamics.fus_form_factor import fus_form_factor
from Source.Aerodynamics.fs_form_factor import fs_form_factor
from Source.Aerodynamics.reynolds_number import reynolds_number

def zero_lift_component_drag(geometry_data,Sref,mach,mach_DD,rho,sos,mu,cd_component,i):
    """ Estimate Component Drag of the Aircraft - Raymer """
    for tag in geometry_data.keys():
        if geometry_data[tag]["Type"] == "Fuselage":
            R = reynolds_number(rho,mach*sos,geometry_data[tag]["Data"].loc["Length"].item(),mu)
            if R > 0:
                Cf_c = flat_plate_skin_friction_coefficient(R,mach)
                Q_c = 1.0
                if mach < mach_DD: FF_c = fus_form_factor(geometry_data[tag]["Data"].loc["Length"].item(),max(geometry_data[tag]["Data"].loc["Area Distribution"].item()[:,1]))
                else: FF_c = fus_form_factor(geometry_data[tag]["Data"].loc["Length"].item(),max(geometry_data[tag]["Data"].loc["Area Distribution"].item()[:,1]))
                cd_component[i] += component_build_up(Cf_c,geometry_data[tag]["Data"].loc["Wetted Surface Area"].item(),FF_c,Q_c,Sref)
            
        elif geometry_data[tag]["Type"] == "Wing" :
            R = reynolds_number(rho,mach*sos,geometry_data[tag]["Data"].loc["Planform MAC Length"].item(),mu)
            if R > 0:
                Cf_c = flat_plate_skin_friction_coefficient(R,mach)
                if mach < mach_DD: FF_c = fs_form_factor( geometry_data[tag]["Data"].loc["Max t/c Location x/c","Value"], geometry_data[tag]["Data"].loc["Max t/c","Value"],mach,geometry_data[tag]["Data"].loc["Max t/c Sweep","Value"])
                else: FF_c = fs_form_factor( geometry_data[tag]["Data"].loc["Max t/c Location x/c","Value"], geometry_data[tag]["Data"].loc["Max t/c","Value"],mach_DD,geometry_data[tag]["Data"].loc["Max t/c Sweep","Value"])
                Q_c = 1.0
                cd_component[i] += component_build_up(Cf_c,geometry_data[tag]["Data"].loc["Wetted Surface Area"].item(),FF_c,Q_c,Sref)

        elif geometry_data[tag]["Type"] == "Horizontal Tail" or geometry_data[tag]["Type"] == "Canard" or geometry_data[tag]["Type"] == "Vertical Tail":
            R = reynolds_number(rho,mach*sos,geometry_data[tag]["Data"].loc["Exposed Planform MAC Length"].item(),mu)
            if R > 0:
                Cf_c = flat_plate_skin_friction_coefficient(R,mach)
                if mach < mach_DD: FF_c = fs_form_factor( geometry_data[tag]["Data"].loc["Max t/c Location x/c","Value"], geometry_data[tag]["Data"].loc["Max t/c","Value"],mach,geometry_data[tag]["Data"].loc["Max t/c Sweep","Value"])
                else: FF_c = fs_form_factor( geometry_data[tag]["Data"].loc["Max t/c Location x/c","Value"], geometry_data[tag]["Data"].loc["Max t/c","Value"],mach_DD,geometry_data[tag]["Data"].loc["Max t/c Sweep","Value"])
                Q_c = 1.0
                cd_component[i] += component_build_up(Cf_c,geometry_data[tag]["Data"].loc["Wetted Surface Area"].item(),FF_c,Q_c,Sref)
                
    return cd_component

