'''
----------------------------------------------------------------------------------------------------
Python module for sunlit_surface
----------------------------------------------------------------------------------------------------
'''

import numpy as np
import sys
import datetime
import os

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
    i = i * np.pi / 180
    RAAN = RAAN * np.pi / 180
    om = om * np.pi / 180

    # computing mean anomaly
    n = np.sqrt(mu / np.power(a, 3.0))
    M = n * t

    # computing eccentric anomaly
    E = [M]
    for j in range(100):
        E.append(E[j] + (M - E[j] + e * np.sin(E[j])) / (1 - e * np.cos(E[j])))
        if(abs(E[j+1] - E[j]) < 1e-8):
            E = E[j+1]
            break

    # computing true anomaly
    nu = 2 * np.arctan2(
            np.sqrt(1 + e) * np.sin(E / 2),
            np.sqrt(1 - e) * np.cos(E / 2)
        ) % (np.pi * 2)

    # computing radius
    r = a * (1 -np.power(e, 2.0)) / (1 + e * np.cos(nu))

    # computing position vector
    pos = [
        r *
            (np.cos(om + nu) * np.cos(RAAN) -
                np.sin(om + nu) * np.sin(RAAN) * np.cos(i)),
        r *
            (np.cos(om + nu) * np.sin(RAAN) -
                np.sin(om + nu) * np.cos(RAAN) * np.cos(i)),
        r * (np.sin(om + nu) * np.sin(i))
    ]

    return pos

def geographic_to_cartesian_coord(lat, lon, r):
    '''
    Converts from geographic to cartesian coordinates

    - Inputs:

    - Outputs:
    '''

    lat = lat * np.pi / 180
    lon = lon * np.pi / 180

    position_vector = [
        r * np.cos(lon) * np.cos(lat),
        r * np.sin(lon) * np.cos(lat),
        r * np.sin(lat)
    ]

    return position_vector

def rotate_frame_around_z(input_vector, angle):
    '''
	Converts coordinates from a reference frame to another with a given rotation angle along the
    z-axis

    - Inputs:

    - Outputs:
    '''

    angle = angle * np.pi / 180

    output_vector = [
        np.cos(angle) * input_vector[0] - np.sin(angle) * input_vector[1],
        np.sin(angle) * input_vector[0] + np.cos(angle) * input_vector[1],
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

    angle = angle * np.pi / 180

    output_vector = [
        input_vector[0],
        np.cos(angle) * input_vector[1] - np.sin(angle) * input_vector[1],
        np.sin(angle) * input_vector[2] + np.cos(angle) * input_vector[2],
    ]

    return output_vector

def compute_sunlight(surface_vector, sun_vector, delta_t):
    '''
    Computes sunlight time of a position on the planet.
    Based on position on the planet and position of the planet with respect to the sun and duration
    delta_t.
    Contains a subfunction "twilight_function" which defines a shadowy zone on the edge of the
    sunlit half of the planet.

    Inputs:
     -
    Outputs:
     -
    '''

    def twilight_function(x):
        '''
        Defines a shadow zone on the edge of the sunlit half of the planet.
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

    surface_vector = surface_vector / np.linalg.norm(surface_vector)

    sun_vector = sun_vector / np.linalg.norm(sun_vector)

    prdct = - np.dot(surface_vector, sun_vector)

    sunlight_time = delta_t * twilight_function(prdct)

    return sunlight_time

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

def prompt_progress(iterations_done, iterations_total):

    progress_percent = iterations_done * 100.0 / iterations_total

    sys.stdout.write("Progress: {0:.2f} % \r".format(progress_percent))
    sys.stdout.flush()

def writing_output_text_file(
    start_date,
    end_date,
    NUMBER_OF_ITERATIONS,
    DELTA_T,
    SPATIAL_RESOLUTION,
    time,
    lat,
    lon,
    sunlight
):
    """
    writing output text file
    input:
     - start_date   datetime.datetime
     - end_date     datetime.datetime
     - NUMBER_OF_ITERATIONS     integer
     - DELTA_T                  float
     - SPATIAL_RESOLUTION       integer
     - time                     list
     - lat                      list
     - lon                      list
     - sunlight                 numpy array of floats (shape len(time)+1, len(lat), len(lon))
    """

    output_directory = "output_directory"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(
        "{0}/sunlit_surface_output_{1}.txt".format(
            output_directory,
            end_date.strftime("%Y%m%d_%H%M")
        ),
        "w"
    ) as file:

        file.write(
            "----------------------------------------------\n"
            + "Results of sunlit_surface \n"
            + "Date {}\n".format(end_date.strftime("%Y%m%d_%H%M"))
            + "----------------------------------------------\n\n"
            + "Input parameters:\n"
            + "    - computation time (h:m:s)      {}\n".format(end_date - start_date)
            + "    - simulation time (s)           {}\n".format(NUMBER_OF_ITERATIONS * DELTA_T)
            + "    - spatial resolution (degrees)  {}\n".format(SPATIAL_RESOLUTION)
            + "----------------------------------------------\n\n"
        )

        file.write(
            "Time array: \n"
        )

        for i in range(len(time) - 1):
            file.write(str(time[i]) + ",")
        file.write(str(time[-1]) + "\n\n")

        file.write(
            "Latitudes array: \n"
        )

        for i in range(len(lat) - 1):
            file.write(str(lat[i]) + ",")
        file.write(str(lat[-1]) + "\n\n")

        file.write(
            "Longitudes array: \n"
        )

        for i in range(len(lon) - 1):
            file.write(str(lon[i]) + ",")
        file.write(str(lon[-1]) + "\n\n")

        file.write(
            "Sunlight data: \n"
        )

        for i in range(len(sunlight)):
            for j in range(len(sunlight[i])):
                for k in range(len(sunlight[i][j]) - 1):
                    file.write(str(sunlight[i][j][k]) + ",")
                file.write(str(sunlight[i][j][-1]) + "\n")
