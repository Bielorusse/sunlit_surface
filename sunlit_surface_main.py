'''
----------------------------------------------------------------------------------------------------
Python main script for sunlit_surface
----------------------------------------------------------------------------------------------------
'''

from sunlit_surface_module import *
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import os

# Declaring time variables
NUMBER_OF_ITERATIONS = 59 * 3
DELTA_T = 86400 # in seconds

# Declaring planet surface spatial resolution in degrees
SPATIAL_RESOLUTION = 5

# Declaring planet's orbital parameters
PLANET_SEMI_MAJOR_AXIS = 57909176 # in km
PLANET_ECCENTRICITY = 0.20563069
PLANET_INCLINATION = 0 # in degrees
PLANET_RAAN = 0 # in degrees
PLANET_ARGUMENT_OF_PERIAPSIS = 0 # in degrees

# Declaring planetary constants
MU_SUN = 1.32712440018E11 # in km3/s2
PLANET_RADIUS = 2440 # in km
PLANET_SIDERAL_PERIOD = 59 * 86400 # in seconds
PLANET_ROTATIONAL_VELOCITY = 360 / PLANET_SIDERAL_PERIOD # in degrees per second
PLANET_AXIAL_TILT = 2 # in degrees

# Declaring planet's positions arrays
planet_position_vector = []

# Declaring time, latitude and longitude arrays
time = list(range(0, NUMBER_OF_ITERATIONS * DELTA_T, DELTA_T))
lat = list(range(-90, 91, SPATIAL_RESOLUTION))
lon = list(range(0, 361, SPATIAL_RESOLUTION))

# Declaring array that contains sunlight time over planet's surface
sunlight = np.zeros((len(time) + 1, len(lat), len(lon)))

for j in range(len(time)):

    planet_position_vector.append(
        from_orbital_to_cartesian_coordinates(
            PLANET_SEMI_MAJOR_AXIS,
            PLANET_ECCENTRICITY,
            PLANET_INCLINATION,
            PLANET_RAAN,
            PLANET_ARGUMENT_OF_PERIAPSIS,
            time[j],
            MU_SUN
        )
    )

    for k in range(len(lat)):

        for l in range(len(lon)):

            surface_position_vector = geographic_to_cartesian_coord(lat[k], lon[l], PLANET_RADIUS)

            # planet rotation
            surface_position_vector = rotate_frame_around_z(
                surface_position_vector, PLANET_ROTATIONAL_VELOCITY * time[j]
            )

            sunlight_time = compute_sunlight(
                surface_position_vector, planet_position_vector[j], DELTA_T
            )

            sunlight[j + 1, k, l] = sunlight[j, k, l] + sunlight_time

sunlight = scale_np_array(sunlight)

'''
Plotting 2D map of sunlit surface and writing results in a text file
'''

fig = plt.figure()

im = plt.imshow(sunlight[-1, :, :])

current_date = datetime.datetime.now()

output_directory = "output_directory"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

plt.savefig("{0}/sunlit_surface_plot_{1}.png".format(
    output_directory,
    current_date.strftime("%Y%m%d_%H%M")
))

print(
    '''
    ----------------------------------------------
    Results of sunlit_surface
    Date {0}
    ----------------------------------------------

    Input parameters:
        - simulation time (s)           {1}
        - spatial resolution (degrees)  {2}

    '''.format(
        current_date.strftime("%Y%m%d_%H%M"),
        NUMBER_OF_ITERATIONS * DELTA_T,
        SPATIAL_RESOLUTION
    ),
    file = open(
        "{0}/sunlit_surface_output_{1}.txt".format(
            output_directory,
            current_date.strftime("%Y%m%d_%H%M")
        ),
        "w"
    )
)

plt.show()
