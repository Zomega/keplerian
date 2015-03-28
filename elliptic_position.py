# Elliptic position is governed by Kepler's equation
#
#          M = E - e * sin E
#
# Aux equations for computing position from E assuming an axis aligned orbit.
#
#          x = a * ( cos E - e )
#
#          y = a * sqrt( 1 - e ^ 2 ) * sin E
#
# For computing M from an orbit.
#
#          M = M_0 + ( 2 * pi * t  / T ) 
#
# The solution E( M, e ) is a transcendental function. This means that it cannot
# be expressed in closed form. The function is well behaved, however, and can
# be approximated through multiple means. It also has a number of convenient
# properties worth listing here.
#
# (1) E - M is 2 * pi periodic and odd -- (E - M)( 0 ) = 0
#
# (2) (E - M)( pi ) = 0 and has odd symmetry at this point
#
#     (E - M)( pi + x ) = - (E - M)( pi - x )
#     E( pi + x ) = -E( pi - x ) + ( pi - x ) + ( pi - x )
#     E( x ) = 2*pi - E( 2*pi - x )
#
# (3) The slope of E at pi ranges between 1 and ( 1 / 2 ) monotonically as the
# eccentricity of the orbit ranges from e = 0 to e = 1
#
# (4) E >= M while 0 <= M <= pi

from orbit import Orbit

from planet import Kerbin

from bisect import bisect

from units.umath import sqrt, pi

from math import sin, cos

from pylab import arange, plot, show, xlabel, ylabel, grid, title

from cubic_spline import CubicSpline

from units import unit
from units.predefined import define_units
define_units()

s  = unit('s')
km = unit('km')

_curve_library = {}

# TODO: 2D spline with e too? Don't populate curve library?
def E( M, e ):
    while M < 0:
        M += 2 * pi
    while M >= 2 * pi:
        M -= 2 * pi
    
    # Take advantage of symmetry.    
    if M > pi:
        return 2 * pi - E( 2 * pi - M, e )
    
    # At this point, 0 <= M <= pi
    
    if not e in _curve_library:
        # If we get here, then we need to populate the curve library.
        #
        # We'll do this by generating an cubic spline with evenly spaced
        # points along the E axis.
        #
        # The key observation is that dE / dM = 1 / ( 1 - e * cos E )
        
        
        # Compute the number of spline points needed. As e approaches 1, this
        # becomes infinite, due to the sharp initial derivatives. This formula
        # was pulled out of a hat. It seems to work, and if I reduce it
        # further, it seems to not work so well at the ends, so I'm happy with
        # it as is.
        num_points = int( 1 / sqrt( 1 - e ) + 2 ) 
        
        E_vals = list( arange( 0, pi, pi / num_points) ) + [pi]
        spline_points = [ (E_ - e * sin(E_), E_, 1 / ( 1 - e * cos( E_ ) ) ) for E_ in E_vals ]
        _curve_library[ e ] = CubicSpline( spline_points )
        
    curve = _curve_library[ e ]
    return curve( M )
    
for e in  [ 0.0, 0.1, 0.2, 0.5, 0.75, 0.9, 0.99, 0.999, 0.9999 ]:
    print "Computing for e =", e
    
    mean_anomaly = 0

    M = arange( 0, 2*pi, 0.001)

    E_ = [ E( m, e ) for m in M ]

    plot(M, E_)

xlabel('M')
ylabel('E')
title('Solutions to Kepler\'s Equation')
grid(True)
show()
    
