'''
----------------------------------------------------------------------------------------------------
Python module for sunlit_surface
----------------------------------------------------------------------------------------------------
'''

import math
import numpy as np

def from_orbital_to_cartesian_coordinates(a, e, i, RAAN, om, t, mu):
    '''
    Converting from orbital parameters to cartesian coordinates
    - Inputs:
            a         semi-major axis (km)
    		e         eccentricity (-)
    		i         inclination (deg)
    		RAAN      right ascension of the ascending node (deg)
    		om        argument of periapsis (deg)
    		t         time spent since passage at periapsis (s)
    		mu	      gravitational parameter of the central body	(km3/s2)
    - Outputs:
    		pos   	  position vector of the orbiting object (km)
    '''

    # converting angles from degrees to radians
    i = i * math.pi / 180
    RAAN = RAAN * math.pi / 180
    om = om * math.pi / 180

    # computing mean anomaly
    n = math.sqrt(mu / math.pow(a, 3))
    M = n * t

    # computing eccentric anomaly
    E = [M]
    for j in range(100):
        E.append(E[j] + (M - E[j] + e * math.sin(E[j])) / (1 - e * math.cos(E[j])))
        if(abs(E[j+1] - E[j]) < 1e-8):
            E = E[j+1]
            break

    # computing true anomaly
    nu = 2 * math.atan2(
            math.sqrt(1 - e) * math.cos(E / 2),
            math.sqrt(1 + e) * math.sin(E / 2)
        ) % (math.pi * 2)

    # computing radius
    r = a * (1 -math.pow(e, 2)) / (1 + e * math.cos(nu))

    # computing position vector
    pos = [
        r *
            (math.cos(om + nu) * math.cos(RAAN) -
                math.sin(om + nu) * math.sin(RAAN) * math.cos(i)),
        r *
            (math.cos(om + nu) * math.sin(RAAN) -
                math.sin(om + nu) * math.cos(RAAN) * math.cos(i)),
        r * (math.sin(om + nu) * math.sin(i))
    ]

    return pos

def geographic_to_cartesian_coord(lat, lon, r):
    '''
    Converts from geographic to cartesian coordinates

    - Inputs:

    - Outputs:
    '''

    lat = lat * math.pi / 180
    lon = lon * math.pi / 180

    position_vector = [
        r * math.cos(lon) * math.cos(lat),
        r * math.sin(lon) * math.cos(lat),
        r * math.sin(lat)
    ]

    return position_vector

def rotate_frame_around_z(input_vector, angle):
    '''
	Converts coordinates from a reference frame to another with a given rotation angle along the
    z-axis

    - Inputs:

    - Outputs:
    '''

    angle = angle * math.pi / 180

    output_vector = [
        math.cos(angle) * input_vector[0] - math.sin(angle) * input_vector[1],
        math.sin(angle) * input_vector[0] + math.cos(angle) * input_vector[1],
        input_vector[2]
    ]

    return output_vector

def rotate_frame_around_x(input_vector, angle):
    '''
	Converts coordinates from a reference frame to another with a given rotation angle along the
    x-axis

    - Inputs:

    - Outputs:
    '''

    angle = angle * math.pi / 180

    output_vector = [
        input_vector[0],
        math.cos(angle) * input_vector[1] - math.sin(angle) * input_vector[1],
        math.sin(angle) * input_vector[2] + math.cos(angle) * input_vector[2],
    ]

    return output_vector

def compute_sunlight(surface_vector, sun_vector, delta_t):
    '''
    Computes sunlight time based on position on the planet and position of the planet with respect
    to the sun
    '''

    surface_vector = surface_vector / np.linalg.norm(surface_vector)

    sun_vector = sun_vector / np.linalg.norm(sun_vector)

    prdct = - np.dot(surface_vector, sun_vector)

    sunlight_time = delta_t * twilight_function(prdct)

    return sunlight_time

def twilight_function(x):
    '''
    Inputs:
        - x     = float
    Outputs:
        - y     = float
    '''

    asymptote_value = 1
    slope = 1e-1
    fact = 1e1

    if (x <= 0):

        y = 0

    elif(x > 0):

        y = asymptote_value * (1 - slope / ( fact * x + 1 ))

    else:

        print(error)

    return y

def normalize_np_array(input_array):
    '''
    Normalize array
    - Inputs:
    - Outputs:
    '''

    max_value = np.amax(input_array)

    if (max_value == 0):

        return input_array

    return input_array / max_value

def normalize_each_time_frame(input_array):
    """
    Normalize each time frame

    - Input:    3D numpy array
    - Output:   3D numpy array
    """

    for i in range(input_array.shape[0]):

        max_value = np.amax(input_array[i, :, :])

        if max_value != 0:

            input_array[i, :, :] = input_array[i, :, :] / max_value

    return input_array
