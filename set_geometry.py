# -*- coding: utf-8 -*-

from Source.Geometry.Input.create_aircraft import create_aircraft
from Source.Geometry.Input.add_fuselage import add_fuselage
from Source.Geometry.Input.add_flying_surface import add_flying_surface
from Source.Geometry.Input.add_point_xsec import add_point_xsec
from Source.Geometry.Input.add_general_xsec import add_general_xsec
from Source.Geometry.Input.add_airfoil import add_airfoil

from Source.Main.save import save

geometry_input = create_aircraft()
add_fuselage(geometry_input,capture_area_location = 6.35335,total_capture_area = 1.0,nozzle_area_location = 16.99,total_nozzle_area = 1.8,tag="Fuselage")
add_flying_surface(geometry_input,tag="Wing",type="Wing")
add_flying_surface(geometry_input,tag="Horizontal Tail",type="Horizontal Tail")
add_flying_surface(geometry_input,tag="Vertical Tail 1",type="Vertical Tail")
add_flying_surface(geometry_input,tag="Vertical Tail 2",type="Vertical Tail")
#Cross Sections to Fuselage
add_point_xsec(x_location = 0.0, z_location =  -0.47630, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 0.95416, z_location = -0.47630, height = 0.5, width = 0.5, max_width_loc = 0.0, top_tan_angle = 90.0, 
                 bot_tan_angle = 45.0, top_str = 0.83, bot_str = 0.83, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 2.43840, z_location = -0.01902*16.99,height = 1.1, width = 1.2, max_width_loc = -0.15455, top_tan_angle = 45.0,
                 bot_tan_angle = 45.0, top_str = 0.93995, bot_str = 1.13127, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 4.3, z_location = 0.00543*16.99, height = 1.87342, width = 1.66205, max_width_loc = -0.43636, top_tan_angle = 50.31818,
                 bot_tan_angle = 52.77273, top_str = 0.82889, bot_str = 0.56448, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 6.05293, z_location = 0.0, height = 1.67172, width = 2.67569, max_width_loc = -0.01818, top_tan_angle = 26.18182,
                 bot_tan_angle = 11.45455, top_str = 0.82889, bot_str = 0.56448, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 6.35335, z_location = 0.0, height = 1.61456, width = 3.7, max_width_loc = 0.1, top_tan_angle = 17.59091,
                 bot_tan_angle = 72.40909, top_str = 0.62349, bot_str = 0.66135, up_str = 1.83, low_str = 1.65532, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 7.98520, z_location = 0.0, height = 1.52348, width = 3.8, max_width_loc = 0.1, top_tan_angle = 38.45455,
                 bot_tan_angle = 72.0, top_str = 0.70843, bot_str = 0.74761, up_str = 2.0, low_str = 1.2971, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 10.11780, z_location = 0.0, height = 1.51968, width = 3.8, max_width_loc = 0.1, top_tan_angle = 12.68182, 
                 bot_tan_angle = 32.31818, top_str = 0.52405, bot_str = 0.71536, up_str = 0.89836, low_str = 1.29764, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 13.38351, z_location = 0.0, height = 1.36236, width = 3.8, max_width_loc = 0.1, top_tan_angle = 30.0,
                 bot_tan_angle = 30.0, top_str = 0.83, bot_str = 0.83, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 15.94740, z_location = 0.0, height = 1.22932, width = 3.8, max_width_loc = 0.0, top_tan_angle = 90.0,
                 bot_tan_angle = 90.0, top_str = 0.83, bot_str = 0.83, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_general_xsec(x_location = 16.99, z_location = 0.0, height = 0.83391, width = 3.8, max_width_loc = 0.0, top_tan_angle = 90.0,
                 bot_tan_angle = 90.0, top_str = 0.83, bot_str = 0.83, up_str = 0.83, low_str = 0.83, geometry = geometry_input, tag="Fuselage")
add_point_xsec(x_location = 16.99, z_location = 0.0, geometry = geometry_input, tag="Fuselage")
#Add Airfoils to Wing
from Source.Geometry.Input.airfoil_lib import naca64A205, naca64A204, biconvex5005
naca64A205_x, naca64A205_z, naca64A205_xc, naca64A205_c, naca64A205_xt, naca64A205_t = naca64A205() 
add_airfoil(x_location = 6.873, y_location = 1.900, z_location = 0.0, x_c_coords = naca64A205_x, z_c_coords = naca64A205_z, xc_c_coords = naca64A205_xc, 
                           c_c_coords = naca64A205_c, xt_c_coords = naca64A205_xt, t_c_coords = naca64A205_t, chord_length = 5.59767, geometry = geometry_input, tag="Wing")
naca64A204_x, naca64A204_z, naca64A204_xc, naca64A204_c, naca64A204_xt, naca64A204_t = naca64A204() 
add_airfoil(x_location = 10.302588, y_location = 1.900 + 4.89796, z_location = 0.0, x_c_coords = naca64A204_x, z_c_coords = naca64A204_z, xc_c_coords = naca64A204_xc,
            c_c_coords = naca64A204_c, xt_c_coords = naca64A204_xt, t_c_coords = naca64A204_t, chord_length = 1.39942, geometry = geometry_input, tag="Wing")
#Add Airfoils to HTail
biconvex5005_x, biconvex5005_z, biconvex5005_xc, biconvex5005_c, biconvex5005_xt, biconvex5005_t = biconvex5005() 
add_airfoil(x_location = 14.018, y_location = 1.900, z_location = 0.0, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 3.48980, geometry = geometry_input, tag="Horizontal Tail")
add_airfoil(x_location = 15.385159, y_location = 1.900 + 2.5, z_location = 0.0, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 1.0, geometry = geometry_input, tag="Horizontal Tail")
#Add Airfoils to VTail 1
biconvex5005_x, biconvex5005_z, biconvex5005_xc, biconvex5005_c, biconvex5005_xt, biconvex5005_t = biconvex5005()
add_airfoil(x_location = 14.080, y_location = 1.318, z_location = 0.28, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 2.73616, geometry = geometry_input, tag="Vertical Tail 1")
add_airfoil(x_location = 15.1444, y_location = 1.318 + 2.59013, z_location = 0.28, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 1.10492, geometry = geometry_input, tag="Vertical Tail 1")
#Add Airfoils to VTail 2
add_airfoil(x_location = 14.080, y_location = -1.318, z_location = 0.28, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 2.73616, geometry = geometry_input, tag="Vertical Tail 2")
add_airfoil(x_location = 15.1444, y_location = -(1.318 + 2.59013), z_location = 0.28, x_c_coords = biconvex5005_x, z_c_coords = biconvex5005_z, xc_c_coords = biconvex5005_xc,
            c_c_coords = biconvex5005_c, xt_c_coords = biconvex5005_xt, t_c_coords = biconvex5005_t, chord_length = 1.10492, geometry = geometry_input, tag="Vertical Tail 2")
#Save Data
save('geometry_input.pydata', geometry_input)