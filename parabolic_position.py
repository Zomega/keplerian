# Elliptic position is governed by Barker's Equation
#
# Unlike elliptic and hyperbolic orbits, true anomaly can be computed directly.
# 
# t - T = (1 / 2) * sqrt( p^3 / mu ) * ( D - ( D^3 / 3 ) ) 
#
# Where:
#
# D = tan( nu / 2 )
#
# t = time
# T = periapsis time
#
# p = semilatus rectum = h ^ 2 / mu
#
# The closed form solution is as follows:
#
# A = ( 3 / 2 ) sqrt( mu / ( 2 * r_p^3 ) ) ( t - T )
#
# B = cuberoot( A + sqrt( A^2 + 1 ) )
#
# nu = 2 * atan( B - ( 1 / B ) )
#
