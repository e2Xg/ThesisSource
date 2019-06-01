# -*- coding: utf-8 -*-

from Source.Geometry.Input.create_aircraft import create_aircraft
from Source.Geometry.Input.add_fuselage import add_fuselage
from Source.Geometry.Input.add_flying_surface import add_flying_surface
from Source.Geometry.Input.add_point_xsec import add_point_xsec
from Source.Geometry.Input.add_general_xsec import add_general_xsec
from Source.Geometry.Input.add_airfoil import add_airfoil

from Source.Main.save import save

geometry_input = create_aircraft()
add_fuselage(geometry_input,capture_area_location =  6.23832,total_capture_area = 1.86,nozzle_area_location = 15.46509,total_nozzle_area = 2.155,tag="Fuselage")
add_flying_surface(geometry_input,tag="Wing",type="Wing")
add_flying_surface(geometry_input,tag="Horizontal Tail",type="Horizontal Tail")
add_flying_surface(geometry_input,tag="Vertical Tail 1",type="Vertical Tail")
add_flying_surface(geometry_input,tag="Vertical Tail 2",type="Vertical Tail")
#Cross Sections to Fuselage
add_point_xsec(x_location = 0.0, z_location =   0.18911, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  1.18828, z_location =  0.26644, height = 0.65547, width = 0.64838, max_width_loc = 0.0, top_tan_angle = 90.0, 
                 bot_tan_angle = 90.0, top_str = 0.83, bot_str = 0.83, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  2.87690, z_location =  0.38789,height = 1.00881, width = 0.96251, max_width_loc = -0.15455, top_tan_angle = 90.0,
                 bot_tan_angle = 90.0, top_str = 0.93995, bot_str = 1.13127, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  4.79981, z_location =  0.83125, height = 1.94292, width = 1.48615, max_width_loc = -0.43636, top_tan_angle = 39.27273,
                 bot_tan_angle = 90.0, top_str = 0.82889, bot_str = 0.56448, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  5.58161, z_location =  0.66315, height = 1.64465, width = 2.24705, max_width_loc = -0.31818, top_tan_angle = 26.18182,
                 bot_tan_angle = 90.0, top_str = 0.82889, bot_str = 0.56448, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  6.23832, z_location =  0.43185, height = 1.20433, width = 3.5, max_width_loc = 0.03636, top_tan_angle = 50.31818,
                 bot_tan_angle = 72.81818, top_str = 0.92135, bot_str = 1.47365, up_str = 0.89836, low_str =1.29764, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  7.0, z_location =  0.49488, height = 1.32415, width = 3.5, max_width_loc = 0.03636, top_tan_angle = 50.31818,
                 bot_tan_angle = 72.81818, top_str = 0.92135, bot_str = 1.47365, up_str = 0.89836, low_str = 1.29764, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  7.4, z_location =  0.49488, height = 1.32415, width = 3.5, max_width_loc = 0.03636, top_tan_angle = 50.31818,
                 bot_tan_angle = 72.81818, top_str = 0.92135, bot_str = 1.47365, up_str = 0.89836, low_str = 1.29764, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  7.72401, z_location =  0.49488, height = 1.32415, width = 3.5, max_width_loc = 0.03636, top_tan_angle = 50.31818,
                 bot_tan_angle = 72.81818, top_str = 0.92135, bot_str = 1.47365, up_str = 0.89836, low_str = 1.29764, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  9.20970, z_location =  0.48059, height = 1.42601, width = 3.5, max_width_loc = 0.03636, top_tan_angle = 61.77273, 
                 bot_tan_angle = 72.81818, top_str = 0.92135, bot_str = 1.47365, up_str = 0.89836, low_str = 1.29764, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location =  15.46509, z_location = 0.41352, height = 1.3, width = 3.5, max_width_loc = 0.1, top_tan_angle = 34.36364,
                 bot_tan_angle = 53.59091, top_str = 0.83, bot_str = 0.83, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_point_xsec(x_location = 15.46509, z_location =  0.38957, geometry = geometry_input, tag="Fuselage")
#Add Airfoils to Wing
from Source.Geometry.Input.airfoil_lib import naca64A205, naca64A204, biconvex5005
naca64A205_x, naca64A205_z, naca64A205_xc, naca64A205_c, naca64A205_xt, naca64A205_t = naca64A205() 
add_airfoil(x_location = 6.873, y_location = 1.500, z_location = 0.4, x_c_coords = naca64A205_x, z_c_coords = naca64A205_z, xc_c_coords = naca64A205_xc, 
                           c_c_coords = naca64A205_c, xt_c_coords = naca64A205_xt, t_c_coords = naca64A205_t, chord_length = 5.59767, geometry = geometry_input, tag="Wing")
naca64A204_x, naca64A204_z, naca64A204_xc, naca64A204_c, naca64A204_xt, naca64A204_t = naca64A204() 
add_airfoil(x_location = 10.302588, y_location = 1.500 + 4.89796, z_location = 0.4, x_c_coords = naca64A204_x, z_c_coords = naca64A204_z, xc_c_coords = naca64A204_xc,
            c_c_coords = naca64A204_c, xt_c_coords = naca64A204_xt, t_c_coords = naca64A204_t, chord_length = 1.39942, geometry = geometry_input, tag="Wing")
#Add Airfoils to HTail
biconvex5005_x, biconvex5005_z, biconvex5005_xc, biconvex5005_c, biconvex5005_xt, biconvex5005_t = biconvex5005() 
add_airfoil(x_location = 13.0, y_location = 1.500, z_location = 0.4, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 3.48980, geometry = geometry_input, tag="Horizontal Tail")
add_airfoil(x_location = 14.5, y_location = 1.500 + 2.5, z_location = 0.4, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 1.0, geometry = geometry_input, tag="Horizontal Tail")
#Add Airfoils to VTail 1
biconvex5005_x, biconvex5005_z, biconvex5005_xc, biconvex5005_c, biconvex5005_xt, biconvex5005_t = biconvex5005()
add_airfoil(x_location = 13.0, y_location = 1.1, z_location = 0.6, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 2.73616, geometry = geometry_input, tag="Vertical Tail 1")
add_airfoil(x_location = 14.5, y_location = 1.1 + 2.59013, z_location = 0.6, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 1.10492, geometry = geometry_input, tag="Vertical Tail 1")
#Add Airfoils to VTail 2
add_airfoil(x_location = 13.0, y_location = -1.1, z_location = 0.4, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 2.73616, geometry = geometry_input, tag="Vertical Tail 2")
add_airfoil(x_location = 14.5, y_location = -(1.1 + 2.59013), z_location = 0.6, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 1.10492, geometry = geometry_input, tag="Vertical Tail 2")
#Save Data
save('F15class_geometry_input.pydata', geometry_input)