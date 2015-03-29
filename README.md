# Keplerian

NOTE: This document has substantially outpaced implementation. For the time being, it is better read as a design document than as documentation at this point. I'm working hard to bring the code in line with this.

A Simple Orbital Mechanics package for Keplerian Orbits.

## Motivation:

To produce a pythonic package suitable for use in hobby applications, but with sufficient accuracy to serve as a good first approximation for heavier use.

Envisioned applications built on Keplerian include:

* Simple, understandable hobby astronomy aids to track the position of planets, satellites and asteroids in the night sky.

* Kerbal Space Program Calculators such as [Olex's Interplanetary transfer calculator](http://ksp.olex.biz/) or [Peppe's Battery Capacity spreadsheet](https://docs.google.com/spreadsheet/ccc?key=0AkXf-77s6gmFdEdVeGFqX0xobTczYkhEaEVrVTdWV3c&usp=sharing) created with uniform code and interface style and minimal developer effort.

* Integrated Kerbal Space Program Mission Planning, when combined with other packages.

* A quick and dirty way to generate candidate trajectories for detailed multi-body analysis.

## Features:

* Complete features for representing trajectories, simulating impulsive maneuvers, and reverse solving maneuvers between orbits with a common point.

* Intelligent constructors. Describe orbits in the terms an units that are easiest for you.

* Excellent for first approximation trajectory and maneuver planning.

## Stretch / Planned Features

* Produce cubic spline approximations of trajectories over specified time periods.

* SGP4 integration, either through [the python sgp4 package](https://pypi.python.org/pypi/sgp4/) or other means.

## Requirements:

* Requires the units package to ensure consistent units and avoid unit-based errors. The indexed units package is somewhat incomplete; a custom updated version is available [here](https://github.com/Zomega/units).

## Basics

### Orbit Models

Keplerian defines orbits very loosely. Hyperbolic and Parabolic Trajectories are considered orbits.

#### UnorientedTimelessOrbit

The simplest type of orbit. Only defines the shape and period (if any) of the orbit. Mostly a utility class.

#### PlanarTimelessOrbit

Oriented within a plane. For documentation convention the plane is assumed to be equatorial with normal in the z direction.

#### UnorientedOrbit

#### PlanarOrbit

#### TimelessOrbit

#### Orbit

The most complex orbit. It is oriented in 3D space and has timing / position information.

## Constructing Orbits

Internally, Keplerian represents orbital trajectories by periapsis radius (not height!), the body being orbited, and eccentricity. 

This nonstandard choice of basis means that all trajectories (excepting those that intersect the center of the planet -- unlikely to occur in practice; see section on edge cases) can be represented. In addition, it is unambiguous and easy to differentiate between circular, elliptical, parabolic, and hyperbolic orbits.

This is obviously not convenient. As a result, Keplerian includes means to create orbits from almost any sufficient set of parameters.

Give the following a try after importing the appropriate units!

```>>> UnorientedTimelessOrbit( r_periapsis = km(1034), r_apoapsis = km(1201) )```

```>>> UnorientedTimelessOrbit( eccentricity = 0.0, v_periapsis = km_per_s(2) )```

```>>> UnorientedTimelessOrbit( eccentricity = 0.5, v_apoapsis = km_per_s(1) )```

```>>> UnorientedTimelessOrbit( eccentricity = 2.0, v_periapsis = km_per_s(2) )```

If you find a constructor combination that should work but doesn't (i.e. sufficient relevant information to totally fix an orbit is given, but an `InsufficientInformationError` is raised regardless), please submit an bug report with a detailed write-up of how to convert the given quantities into equivalent quantities that do work. I'll do my best to integrate it into the system when I have time.

No effort is made to detect or correct inconsistencies in provided data.

## Edge Cases and Errors

### Insufficient Information for Construction

If Keplerian is unable to create an orbit from the provided information, then it will `raise InsufficientInformationError("Unable to produce XXX")` where XXX is the quantity(s) that couldn't be computed from the provided information.

### Zero Periapsis

If the orbital parameters provided produce an periapsis radius of zero, then Keplerian will `raise OrbitRepresentationError("Zero periapsis radius")`. In these cases, either the orbit will be falling directly toward the center of the planet, or speeding directly away.

Both cases can be handled separately by the `RadialOrbit` class, but this can be complex and is not guaranteed to interoperate.
