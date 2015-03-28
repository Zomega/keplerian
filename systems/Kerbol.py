from ..planet import CelestialBody, Atmosphere, Planetoid

from units import unit
from units.predefined import define_units
define_units()

kg = unit('kg')
lbs = unit('lbs')
s  = unit('s')
seconds = s
km = unit('km')
m = unit('m')
m_per_s2 = m / ( seconds ** 2 )
km3_per_s2 = ( km ** 3 ) / ( seconds ** 2 ) # TODO: Report composed unit bug. i.e. print km3_per_s2(30)

atm = unit('atm') # TODO: Relate to pressure...

Kerbol =  CelestialBody( "Kerbol",
            mu = km3_per_s2( 1167922000 ),
            radius = km( 65400 ) )
            
Eve_atm = Atmosphere( h_atm = km( 96.708574 ), H0 = km( 7.0 ), P0 = atm(5) )
Kerbin_atm = Atmosphere( h_atm = km( 69.077553 ), H0 = km( 5.0 ), P0 = atm(1) )
Duna_atm = Atmosphere( h_atm = km( 41.446532 ), H0 = km( 3.0 ), P0 = atm(0.2) )
Jool_atm = Atmosphere( h_atm = km( 138.15511 ), H0 = km( 10.0 ), P0 = atm(15) )
Laythe_atm = Atmosphere( h_atm = km( 55.262042 ), H0 = km( 4.0 ), P0 = atm(0.8) )
            
# TODO: Surface gravity            
'''
var PLANETS = [
    {name:"None", gravity:0},
	{name:"Moho", gravity:2.70},
	{name:"Eve", gravity:16.7},
	{name:"Gilly", gravity:0.049},
	{name:"Kerbin", gravity:9.81},
	{name:"Mun", gravity:1.63},
	{name:"Minmus", gravity:0.491},
	{name:"Duna", gravity:2.94},
	{name:"Ike", gravity:1.10},
	{name:"Dres", gravity:1.13},
	{name:"Jool", gravity:7.85},
	{name:"Laythe", gravity:7.85},
	{name:"Vall", gravity:2.31},
	{name:"Tylo", gravity:7.85},
	{name:"Bop", gravity:0.589},
	{name:"Pol", gravity:0.373},
	{name:"Eeloo", gravity:1.69}
];'''

# Planets
Moho = Planetoid( "Moho",
            mu = 245.25, # TODO: Doesn't match wiki...
            alt = 5263138.3,
            radius = km( 250 ),
            inclination = 7,
            T_rot = None, # TODO
            soi = 11206.449,
            parent = Kerbol )
            
Eve = Planetoid( "Eve",
            mu = 8171.73,
            alt = 9832684.544,
            radius = km( 700 ),
            inclination = 2.1,
            T_rot = 80500,
            soi = 85109.364,
            atmosphere = Eve_atm,
            parent = Kerbol )

Gilly = Planetoid( "Gilly",
            mu = 0.008289450,
            alt = km( 31500 ),
            radius = km( 13 ),
            inclination = 12,
            T_rot = None, # TODO
            soi = 126.123,
            parent = Eve )

Kerbin = Planetoid( "Kerbin",
            mu = km3_per_s2( 3531.6 ),
            alt = km( 13599840.256 ),
            radius = km( 600 ),
            inclination = 0,
            T_rot = seconds( 21600 ),
            soi = km( 84159.2865 ),
            atmosphere = Kerbin_atm,
            parent = Kerbol )

Mun = Planetoid("Mun",
            mu = 65.138,
            alt = 12000,
            radius = km( 200 ),
            inclination = 0,
            T_rot = None, # TODO
            soi = 2430,
            parent = Kerbin )
                
Minmus = Planetoid("Minmus",
            mu = 1.7658,
            alt = 47000,
            radius = km( 60 ),
            inclination = 6,
            T_rot = None, # TODO
            soi = 2247.428,
            parent = Kerbin )

Duna = Planetoid("Duna",
            mu = 301.363,
            alt = km( 20726155.264 ),
            radius = km( 320 ),
            inclination = 1.85,
            T_rot = 65517.859,
            soi = 47921.949,
            atmosphere = Duna_atm,
            parent = Kerbol )
            
Ike = Planetoid("Ike",
            mu = 18.56837,
            alt = 3200,
            radius = km( 130 ),
            inclination = 0.2,
            T_rot = None, # TODO
            soi = 1049.599,
            parent = Duna )

Dres = Planetoid("Dres",
            mu = 21.4845,
            alt = 40839348.203,
            radius = km( 138 ),
            inclination = 5,
            T_rot = None, # TODO
            soi = 32832.84,
            parent = Kerbol )

Jool = Planetoid("Jool",
            mu = 282528.0042,
            alt = 68773560.320,
            radius = km( 6000 ),
            inclination = 1.3,
            T_rot = 36000,
            soi = 2455985.185,
            atmosphere = Jool_atm,
            parent = Kerbol )

Laythe = Planetoid("Laythe",
            mu = 1962,
            alt = 27184,
            radius = km( 500 ),
            inclination = 0,
            T_rot = 52980.879,
            soi = 3723.646,
            atmosphere = Laythe_atm,
            parent = Jool )

Vall = Planetoid("Vall",
            mu = 207.4815,
            alt = 43152,
            radius = km( 300 ),
            inclination = 0,
            T_rot = None, # TODO
            soi = 2406.401,
            parent = Jool )

Tylo = Planetoid("Tylo",
            mu = 2825.28,
            alt = 68500,
            radius = km( 600 ),
            inclination = 0.025,
            T_rot = None, # TODO
            soi = 10856.51837,
            parent = Jool )

Bop = Planetoid("Bop",
            mu = 2.486835,
            alt = 104500,
            radius = km( 65 ),
            inclination = 15,
            T_rot = None, # TODO
            soi = 993.0028,
            parent = Jool )

Pol = Planetoid("Pol",
            mu = 0.227,
            alt = 129890,
            radius = km( 44 ),
            inclination = 1.304,
            T_rot = None, # TODO
            soi = 2455985.185,
            parent = Jool )

Eeloo = Planetoid("Eeloo",
            mu = 74.410815,
            alt = 90118858.179,
            radius = km( 210 ),
            inclination = 6.15,
            T_rot = None, # TODO
            soi = 119082.94,
            parent = Kerbol )
