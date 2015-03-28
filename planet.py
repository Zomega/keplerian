from math import exp

# TODO: Split into multiple files
# TODO: Add Sun class to represent main sequence star? Is Kerbol Main Sequence?

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

class CelestialBody:
    def __init__( self, name, mu, radius, parent = None ):
        self.name = name 
        
        self.mu = mu
        self.radius = radius
        self.parent = parent
    
class Atmosphere:
    def __init__( self, H0, P0, h_atm ):
    	
    	# h_atm : Atmospheric Height (km)
		# H0    : Scale height of atmosphere (km), P falls off by 1/e for each H0
		# P0    : Pressure at zero altitude (atm)
        self.H0 = H0
        self.P0 = P0
        self.h_atm = h_atm

# TODO: alt and inclination should really be part of an orbit about the parent body.    
class Planetoid(CelestialBody): # TODO: T_rot not optional.
    def __init__( self, name, mu, alt, inclination, radius, T_rot, soi, parent, atmosphere = None ):
        
        # mu    : Grav. parameter (km3/s2)
        # alt   : ??? TODO
        # inclination   : ??? TODO
        # radius: Radius at equator (km)
        # T_rot : Sidereal Rotation Period (s)
        # soi   : Sphere of influence (km)
        
        CelestialBody.__init__( self, name, mu, radius, parent )
        
        self.atmosphere = atmosphere
        self.alt = alt # TODO: Wtf is this, semimajor axis?
        self.inclination = inclination
        
        self.T_rot = T_rot
        self.soi = soi
        
    @property
    def has_atmosphere( self ):
        return self.atmosphere != None
        
    @property
    def r_atm( self ):
        assert self.has_atmosphere
        return self.radius + self.atmosphere.h_atm
        
    def pressure( self, r ):
        assert self.has_atmosphere
        
        if r > self.r_atm:
            return atm( 0 )
        if r <= self.radius:
            return self.atmosphere.P0 # TODO: Handle impact differently?
        return self.atmosphere.P0 * exp( ( self.radius - r ) / self.atmosphere.H0 )
