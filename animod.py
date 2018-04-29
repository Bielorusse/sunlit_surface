"""
Module for 3D animation based on opengl and pygame.
"""

import numpy as np
import pygame
import sys
import pygame.locals
import OpenGL.GL
import OpenGL.GLU
import scmod

RGB_colorbar_list = [
    [0.,0.,0.],
    [0.01568627450980392,0.,0.011764705882352941],
    [0.03529411764705882,0.,0.027450980392156862],
    [0.050980392156862744,0.,0.0392156862745098],
    [0.07058823529411765,0.,0.054901960784313725],
    [0.08627450980392157,0.,0.07450980392156863],
    [0.10588235294117647,0.,0.09019607843137255],
    [0.12156862745098039,0.,0.10980392156862745],
    [0.1411764705882353,0.,0.12549019607843137],
    [0.1568627450980392,0.,0.14901960784313725],
    [0.1764705882352941,0.,0.16862745098039217],
    [0.19607843137254902,0.,0.18823529411764706],
    [0.21176470588235294,0.,0.20784313725490194],
    [0.22745098039215686,0.,0.23137254901960785],
    [0.2392156862745098,0.,0.24705882352941178],
    [0.25098039215686274,0.,0.26666666666666666],
    [0.26666666666666666,0.,0.2823529411764706],
    [0.27058823529411763,0.,0.30196078431372547],
    [0.2823529411764706,0.,0.3176470588235294],
    [0.2901960784313725,0.,0.33725490196078434],
    [0.30196078431372547,0.,0.3568627450980392],
    [0.30980392156862746,0.,0.37254901960784315],
    [0.3137254901960784,0.,0.39215686274509803],
    [0.32156862745098036,0.,0.40784313725490196],
    [0.3254901960784314,0.,0.42745098039215684],
    [0.3333333333333333,0.,0.44313725490196076],
    [0.32941176470588235,0.,0.4627450980392157],
    [0.33725490196078434,0.,0.4784313725490196],
    [0.3411764705882353,0.,0.4980392156862745],
    [0.34509803921568627,0.,0.5176470588235293],
    [0.33725490196078434,0.,0.5333333333333333],
    [0.3411764705882353,0.,0.5529411764705883],
    [0.3411764705882353,0.,0.5686274509803921],
    [0.3411764705882353,0.,0.5882352941176471],
    [0.3333333333333333,0.,0.6039215686274509],
    [0.32941176470588235,0.,0.6235294117647059],
    [0.32941176470588235,0.,0.6392156862745098],
    [0.32941176470588235,0.,0.6588235294117647],
    [0.3254901960784314,0.,0.6784313725490196],
    [0.30980392156862746,0.,0.6941176470588235],
    [0.3058823529411765,0.,0.7137254901960784],
    [0.30196078431372547,0.,0.7294117647058823],
    [0.2980392156862745,0.,0.7490196078431373],
    [0.2784313725490196,0.,0.7647058823529411],
    [0.27450980392156865,0.,0.7843137254901961],
    [0.26666666666666666,0.,0.8],
    [0.2588235294117647,0.,0.8196078431372549],
    [0.23529411764705882,0.,0.8392156862745098],
    [0.22745098039215686,0.,0.8549019607843137],
    [0.21568627450980393,0.,0.8745098039215686],
    [0.20784313725490194,0.,0.8901960784313725],
    [0.1803921568627451,0.,0.9098039215686274],
    [0.16862745098039217,0.,0.9254901960784314],
    [0.1568627450980392,0.,0.9450980392156862],
    [0.1411764705882353,0.,0.9607843137254902],
    [0.12941176470588234,0.,0.9803921568627451],
    [0.09803921568627451,0.,1.],
    [0.08235294117647059,0.,1.],
    [0.06274509803921569,0.,1.],
    [0.047058823529411764,0.,1.],
    [0.01568627450980392,0.,1.],
    [0.,0.,1.],
    [0.,0.01568627450980392,1.],
    [0.,0.03137254901960784,1.],
    [0.,0.06274509803921569,1.],
    [0.,0.08235294117647059,1.],
    [0.,0.09803921568627451,1.],
    [0.,0.11372549019607843,1.],
    [0.,0.14901960784313725,1.],
    [0.,0.16470588235294117,1.],
    [0.,0.1803921568627451,1.],
    [0.,0.2,1.],
    [0.,0.21568627450980393,1.],
    [0.,0.24705882352941178,1.],
    [0.,0.2627450980392157,1.],
    [0.,0.2823529411764706,1.],
    [0.,0.2980392156862745,1.],
    [0.,0.32941176470588235,1.],
    [0.,0.34901960784313724,1.],
    [0.,0.36470588235294116,1.],
    [0.,0.3803921568627451,1.],
    [0.,0.4156862745098039,1.],
    [0.,0.43137254901960786,1.],
    [0.,0.44705882352941173,1.],
    [0.,0.4666666666666667,1.],
    [0.,0.4980392156862745,1.],
    [0.,0.5137254901960784,1.],
    [0.,0.5294117647058824,1.],
    [0.,0.5490196078431373,1.],
    [0.,0.5647058823529412,1.],
    [0.,0.596078431372549,1.],
    [0.,0.615686274509804,1.],
    [0.,0.6313725490196078,1.],
    [0.,0.6470588235294118,1.],
    [0.,0.6823529411764706,1.],
    [0.,0.6980392156862745,1.],
    [0.,0.7137254901960784,1.],
    [0.,0.7333333333333333,1.],
    [0.,0.7647058823529411,1.],
    [0.,0.7803921568627451,1.],
    [0.,0.796078431372549,1.],
    [0.,0.8156862745098039,1.],
    [0.,0.8470588235294118,1.],
    [0.,0.8627450980392157,1.],
    [0.,0.8823529411764706,1.],
    [0.,0.8980392156862745,1.],
    [0.,0.9137254901960784,1.],
    [0.,0.9490196078431372,1.],
    [0.,0.9647058823529412,1.],
    [0.,0.9803921568627451,1.],
    [0.,1.,1.],
    [0.,1.,0.9647058823529412],
    [0.,1.,0.9490196078431372],
    [0.,1.,0.9333333333333333],
    [0.,1.,0.9137254901960784],
    [0.,1.,0.8823529411764706],
    [0.,1.,0.8627450980392157],
    [0.,1.,0.8470588235294118],
    [0.,1.,0.8313725490196078],
    [0.,1.,0.796078431372549],
    [0.,1.,0.7803921568627451],
    [0.,1.,0.7647058823529411],
    [0.,1.,0.7490196078431373],
    [0.,1.,0.7333333333333333],
    [0.,1.,0.6980392156862745],
    [0.,1.,0.6823529411764706],
    [0.,1.,0.6666666666666666],
    [0.,1.,0.6470588235294118],
    [0.,1.,0.615686274509804],
    [0.,1.,0.596078431372549],
    [0.,1.,0.580392156862745],
    [0.,1.,0.5647058823529412],
    [0.,1.,0.5294117647058824],
    [0.,1.,0.5137254901960784],
    [0.,1.,0.4980392156862745],
    [0.,1.,0.4823529411764706],
    [0.,1.,0.44705882352941173],
    [0.,1.,0.43137254901960786],
    [0.,1.,0.4156862745098039],
    [0.,1.,0.4],
    [0.,1.,0.3803921568627451],
    [0.,1.,0.34901960784313724],
    [0.,1.,0.32941176470588235],
    [0.,1.,0.3137254901960784],
    [0.,1.,0.2980392156862745],
    [0.,1.,0.2627450980392157],
    [0.,1.,0.24705882352941178],
    [0.,1.,0.23137254901960785],
    [0.,1.,0.21568627450980393],
    [0.,1.,0.1803921568627451],
    [0.,1.,0.16470588235294117],
    [0.,1.,0.14901960784313725],
    [0.,1.,0.13333333333333333],
    [0.,1.,0.09803921568627451],
    [0.,1.,0.08235294117647059],
    [0.,1.,0.06274509803921569],
    [0.,1.,0.047058823529411764],
    [0.,1.,0.03137254901960784],
    [0.,1.,0.],
    [0.01568627450980392,1.,0.],
    [0.03137254901960784,1.,0.],
    [0.047058823529411764,1.,0.],
    [0.08235294117647059,1.,0.],
    [0.09803921568627451,1.,0.],
    [0.11372549019607843,1.,0.],
    [0.12941176470588234,1.,0.],
    [0.16470588235294117,1.,0.],
    [0.1803921568627451,1.,0.],
    [0.2,1.,0.],
    [0.21568627450980393,1.,0.],
    [0.24705882352941178,1.,0.],
    [0.2627450980392157,1.,0.],
    [0.2823529411764706,1.,0.],
    [0.2980392156862745,1.,0.],
    [0.3137254901960784,1.,0.],
    [0.34901960784313724,1.,0.],
    [0.36470588235294116,1.,0.],
    [0.3803921568627451,1.,0.],
    [0.396078431372549,1.,0.],
    [0.43137254901960786,1.,0.],
    [0.44705882352941173,1.,0.],
    [0.4666666666666667,1.,0.],
    [0.4823529411764706,1.,0.],
    [0.5137254901960784,1.,0.],
    [0.5294117647058824,1.,0.],
    [0.5490196078431373,1.,0.],
    [0.5647058823529412,1.,0.],
    [0.6,1.,0.],
    [0.615686274509804,1.,0.],
    [0.6313725490196078,1.,0.],
    [0.6470588235294118,1.,0.],
    [0.6627450980392157,1.,0.],
    [0.6980392156862745,1.,0.],
    [0.7137254901960784,1.,0.],
    [0.7333333333333333,1.,0.],
    [0.7490196078431373,1.,0.],
    [0.7803921568627451,1.,0.],
    [0.796078431372549,1.,0.],
    [0.8156862745098039,1.,0.],
    [0.8313725490196078,1.,0.],
    [0.8666666666666667,1.,0.],
    [0.8823529411764706,1.,0.],
    [0.8980392156862745,1.,0.],
    [0.9137254901960784,1.,0.],
    [0.9490196078431372,1.,0.],
    [0.9647058823529412,1.,0.],
    [0.9803921568627451,1.,0.],
    [1.,1.,0.],
    [1.,0.9803921568627451,0.],
    [1.,0.9490196078431372,0.],
    [1.,0.9333333333333333,0.],
    [1.,0.9137254901960784,0.],
    [1.,0.8980392156862745,0.],
    [1.,0.8666666666666667,0.],
    [1.,0.8470588235294118,0.],
    [1.,0.8313725490196078,0.],
    [1.,0.8156862745098039,0.],
    [1.,0.7803921568627451,0.],
    [1.,0.7647058823529411,0.],
    [1.,0.7490196078431373,0.],
    [1.,0.7333333333333333,0.],
    [1.,0.6980392156862745,0.],
    [1.,0.6823529411764706,0.],
    [1.,0.6666666666666666,0.],
    [1.,0.6470588235294118,0.],
    [1.,0.6313725490196078,0.],
    [1.,0.6,0.],
    [1.,0.580392156862745,0.],
    [1.,0.5647058823529412,0.],
    [1.,0.5490196078431373,0.],
    [1.,0.5137254901960784,0.],
    [1.,0.4980392156862745,0.],
    [1.,0.4823529411764706,0.],
    [1.,0.4666666666666667,0.],
    [1.,0.43137254901960786,0.],
    [1.,0.4156862745098039,0.],
    [1.,0.4,0.],
    [1.,0.3803921568627451,0.],
    [1.,0.34901960784313724,0.],
    [1.,0.3333333333333333,0.],
    [1.,0.3137254901960784,0.],
    [1.,0.2980392156862745,0.],
    [1.,0.2823529411764706,0.],
    [1.,0.24705882352941178,0.],
    [1.,0.23137254901960785,0.],
    [1.,0.21568627450980393,0.],
    [1.,0.2,0.],
    [1.,0.16470588235294117,0.],
    [1.,0.14901960784313725,0.],
    [1.,0.13333333333333333,0.],
    [1.,0.11372549019607843,0.],
    [1.,0.08235294117647059,0.],
    [1.,0.06666666666666667,0.],
    [1.,0.047058823529411764,0.],
    [1.,0.03137254901960784,0.]
]

SUN_RESOLUTION = 30 # in degrees
SUN_DISPLAY_RADIUS = 5.0e6 # in km
sun_lat = list(range(-90, 91, SUN_RESOLUTION))
sun_lon = list(range(0, 361, SUN_RESOLUTION))
sun_vertices = []
for i in range(len(sun_lat)):
    for j in range(len(sun_lon)):
        sun_vertices.append(scmod.geographic_to_cartesian_coord(sun_lat[i], sun_lon[j], SUN_DISPLAY_RADIUS))
sun_surfaces = []
for i in range(len(sun_lat) - 1):
    for j in range(len(sun_lon) - 1):
        sun_surfaces.append((
            j + i*len(sun_lon),
            j+1 + i*len(sun_lon),
            j+1 + (i+1)*len(sun_lon),
            j + (i+1)*len(sun_lon)
        ))

def display_sun_direction(planet_position_vector):
    """
    display sun direction
    input:
     - planet_position_vector list
    """

    sun_dir_vertices = [
        (0, 0, 0),
        (- planet_position_vector[0], - planet_position_vector[1], - planet_position_vector[2])
    ]

    OpenGL.GL.glBegin(GL_LINES)

    OpenGL.GL.glColor4fv((1, 1, 1, 0.5))

    for i in range(len(sun_dir_vertices)):

        OpenGL.GL.glVertex3fv(sun_dir_vertices[i])

    OpenGL.GL.glEnd()

def display_sun(sun_vertices, sun_surfaces):
    """
    displays sun
    input:
     - sun_vertices     list
     - sun_surfaces     list
    """

    OpenGL.GL.glBegin(GL_QUADS)

    for i in range(len(sun_surfaces)):

        for j in sun_surfaces[i]:

            OpenGL.GL.glColor3fv((1, 1, 0))

            OpenGL.GL.glVertex3fv(sun_vertices[j])

    OpenGL.GL.glEnd()

def colorbar_relative(index, data_list, color_list):
    """
    returns RGB color triplet corresponding to one value of a list of data relative the whole list
    input:
     - index        integer
     - data_list    list
     - color_list   list of RGB triplets (lists of 3 floats)
    output:
     - RGB          list of 3 floats
    """

    max = np.amax(data_list)

    min = np.amin(data_list)

    if max == min:

        float = 0.0

    else:

        float = (data_list[index] - min) / (max - min)

    index = int(round(float * (len(color_list) - 1)))

    RGB = color_list[index]

    return RGB

def colorbar_abs(float, color_list):
    """
    returns RGB triplet when given float between 0 and 1
    input:
     - float        float between 0 and 1
     - color_list   list of RGB triplets (lists of 3 floats)
    output:
     - RGB          list of 3 floats
    """

    index = int(round(float * (len(color_list) - 1)))

    RGB = color_list[index]

    return RGB

def display_planet(
    time,
    lat,
    lon,
    PLANET_ROTATIONAL_VELOCITY,
    PLANET_RADIUS,
    planet_position_vector,
    sunlight_data_list
):
    """
    displays the planet as polyhedron with sunlight time data in color
    input:
     - time                         float
     - lat                          list
     - lon                          list
     - PLANET_ROTATIONAL_VELOCITY   float
     - planet_radius                float
     - planet_position_vector       list
     - sunlight_data_list           list
    """

    # defining list of the vertices of the polyhedron representing the planet
    planet_vertices = []
    for i in range(len(lat)):
        for j in range(len(lon)):
            vertices_coords = scmod.geographic_to_cartesian_coord(lat[i], lon[j], PLANET_RADIUS)
            vertices_coords = scmod.rotate_frame_around_z(
                vertices_coords,
                PLANET_ROTATIONAL_VELOCITY * time
            )
            vertices_coords = vertices_coords + planet_position_vector
            planet_vertices.append(vertices_coords)

    # defining list of edges connecting vertices of the polyhedron representing the planet
    planet_edges = []
    for i in range(len(lat) - 1):
        for j in range(len(lon) - 1):
            planet_edges.append((j + i*len(lon), j+1 + i*len(lon)))
            planet_edges.append((j+1 + i*len(lon), j+1 + (i+1)*len(lon)))
            planet_edges.append((j+1 + (i+1)*len(lon), j + (i+1)*len(lon)))
            planet_edges.append((j+ (i+1)*len(lon), j + i*len(lon)))

    # defining list of faces connecting vertices of the polyhedron representing the planet
    planet_faces = []
    for i in range(len(lat) - 1):
        for j in range(len(lon) - 1):
            planet_faces.append((
                j + i*len(lon),
                j+1 + i*len(lon),
                j+1 + (i+1)*len(lon),
                j + (i+1)*len(lon)
            ))

    OpenGL.GL.glBegin(GL_QUADS)

    for i in range(len(planet_faces)):

        OpenGL.GL.glColor3fv(colorbar_relative(i, sunlight_data_list, RGB_colorbar_list))

        for vertex in planet_faces[i]:

            OpenGL.GL.glVertex3fv(planet_vertices[vertex])

    OpenGL.GL.glEnd()

    OpenGL.GL.glBegin(GL_LINES)

    OpenGL.GL.glColor4fv((1, 1, 1, 0.5))

    for edge in planet_edges:

        for vertex in edge:

            OpenGL.GL.glVertex3fv(planet_vertices[vertex])

    OpenGL.GL.glEnd()

def display_animation(
    time,
    lat,
    lon,
    PLANET_ROTATIONAL_VELOCITY,
    PLANET_RADIUS,
    planet_position_vectors,
    sunlight_data
):
    """
    displays animation
    input:
     - lat                      list
     - lon                      list
     - PLANET_RADIUS            float
     - planet_position_vectors  list
     - sunlight_data            numpy array of floats
    """

    time_count = 0 # initializing time counter

    # pygame display functions
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.locals.DOUBLEBUF|pygame.locals.OPENGL)
    OpenGL.GLU.gluPerspective(45, (display[0]/display[1]), 0.1, 500.0e6)
    OpenGL.GL.glTranslatef(0.0, 0.0, -250.0e6)
    OpenGL.GL.glRotatef(0, 1, 0, 0)
    OpenGL.GL.glRotatef(90, 0, 0, 1)

    while True:

        # closing animation window at any event
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                quit()

        OpenGL.GL.glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # resetting time counter to zero when reached the end of the animation
        if time_count == len(time):

            time_count = 0

        # storing data from numpy array to a list that has the same shape as "planet_faces"
        sunlight_data_list = []
        for j in range(len(sunlight_data[time_count]) - 1):
            for k in range(len(sunlight_data[time_count][j]) - 1):
                sunlight_data_list.append(sunlight_data[time_count, j, k])

        display_planet(
            time[time_count],
            lat,
            lon,
            PLANET_ROTATIONAL_VELOCITY,
            PLANET_RADIUS,
            planet_position_vectors[time_count],
            sunlight_data_list
        )

        display_sun(sun_vertices, sun_surfaces)

        time_count += 1 # increasing time counter

        pygame.display.flip()

        pygame.time.wait(100)
