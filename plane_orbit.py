from units.umath import sqrt, pi

#########
#
# Captures intuitions about orbits without focusing on properties that require time or orientation.
#
# Many equations are derived from http://www.bogan.ca/orbits/kepler/orbteqtn.html and Wikipedia.
#
#########
class TimelessPlanarOrbit:
    def __init__( self, r_periapsis, eccentricity, body ):
        # TODO: Validate
        self.r_periapsis = r_periapsis
        self.eccentricity = eccentricity
        self.body = body
        
    @property
    def semimajor_axis( self ):
         assert self.eccentricity != 1 # TODO: Handle this case with an exception.
         return self.r_periapsis / ( 1 - self.eccentricity )
         
    @property
    def semilatus_rectum( self ):
        return self.r_periapsis * ( 1 + self.eccentricity )       
    
    # Note that this is here defined as a scalar quantity, since it is always
    # oriented in the same direction.    
    @property
    def specific_angular_momentum( self ):
        return sqrt( self.body.mu * self.semilatus_rectum ) # TODO: Units are FUBAR due to sqrt
            
    @property
    def specific_orbital_energy( self ):
        if self.eccentricity == 1:
            return 0 # Parabolic orbits
        return - self.body.mu / ( 2 * self.semimajor_axis )
        
    ########
    #
    # Elliptic orbits only...
    #
    #########
    #
    # All of these methods require e < 1, i.e. the orbit is an ellipse ( or
    # circle, at e = 0 ). Ensure that this is the case before calling them.
    #
    #########
    
    @property
    def r_apoapsis( self ):
        assert self.eccentricity < 1
        return self.r_periapsis * ( 1 + self.eccentricity ) / ( 1 - self.eccentricity )
    
    @property
    def semiminor_axis( self ):
        assert self.eccentricity < 1
        return self.semimajor_axis * sqrt( 1 - self.eccentricity ** 2 )
        
    @property
    def period( self ):
        assert self.eccentricity < 1
        return 2 * pi * sqrt( self.semimajor_axis ** 3 / self.body.mu )

#########
#
# Extends TimelessPlanarOrbit to include timing.
# This importantly allows for
#
#########
class PlanarOrbit:
    def __init__( self, r_periapsis, eccentricity, M_0, body ):
        # TODO: Validate M_0 if eccentricity >= 1
        self.M_0 = M_0
        self.timeless_orbit = TimelessPlanarOrbit( r_periapsis, eccentricity, body )
