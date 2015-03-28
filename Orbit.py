from units.umath import sqrt, pi

# TODO: Express dependance on planet....

# redo with periapse distance and speed
# Add inclination plane (normal for periapse)
class Orbit:
    def __init__( self, periapsis, apoapsis, body ):
        assert periapsis <= apoapsis
        self.periapsis = periapsis
        self.apoapsis = apoapsis
        self.body = body
    
    @property
    def eccentricity( self ):
        return ( self.apoapsis - self.periapsis ) / ( self.apoapsis + self.periapsis )
         
    @property
    def semimajor_axis( self ):
        return ( self.apoapsis + self.periapsis ) / 2
        
    @property
    def semiminor_axis( self ):
        return self.semimajor_axis * sqrt( 1 - self.eccentricity ** 2 )
        
    @property
    def period( self ):
        return 2 * pi * sqrt( self.semimajor_axis ** 3 / self.body.mu ) # TODO: Units are FUBAR due to sqrt
    
    @property
    def specific_angular_momentum( self ):
        return sqrt( ( 1 - self.eccentricity ** 2 ) * self.body.mu * self.semimajor_axis ) # TODO: Units are FUBAR due to sqrt
            
    @property
    def specific_orbital_energy( self ):
        return - self.body.mu / ( 2 * self.semimajor_axis )
