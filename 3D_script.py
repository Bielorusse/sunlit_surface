"""
3D_script.py

PyOpenGL script

runs with python 2.7
"""

import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from sunlit_surface_module import *

def read_sunlight_data(file_name):
    """
    read sunlight data
    input:
     - file_name    string
    output:
     - sunlight     numpy array of floats (shape len(time), len(lat), len(lon))
     - time         list of strings
     - lat          list of strings
     - lon          list of strings
    """

    with open(file_name, "r") as file:

        file_contents = file.readlines()

    time = file_contents[12][:-1].split(",")

    for i in range(len(time)):

        time[i] = float(time[i])

    lat = file_contents[15][:-1].split(",")

    for i in range(len(lat)):

        lat[i] = float(lat[i])

    lon = file_contents[18][:-1].split(",")

    for i in range(len(lon)):

        lon[i] = float(lon[i])

    sunlight = np.zeros((len(time), len(lat), len(lon)))

    for i in range(len(time)):
        for j in range(len(lat)):
            for k in range(len(lon)):

                sunlight[i, j, k] = file_contents[21 + i * len(lat) + j].split(",")[k]

    return sunlight, time, lat, lon

sunlight, time, lat, lon = read_sunlight_data(
    "output_directory/sunlit_surface_output_20180402_1905.txt"
)

# Declaring planetary constants
PLANET_RADIUS = 2440 # in km

vertices = []
for i in range(len(lat)):
    for j in range(len(lon)):
        vertices.append(geographic_to_cartesian_coord(lat[i], lon[j], PLANET_RADIUS))

edges = []
for i in range(len(lat) - 1):
    for j in range(len(lon) - 1):
        edges.append((j + i*len(lon), j+1 + i*len(lon)))
        edges.append((j+1 + i*len(lon), j+1 + (i+1)*len(lon)))
        edges.append((j+1 + (i+1)*len(lon), j + (i+1)*len(lon)))
        edges.append((j+ (i+1)*len(lon), j + i*len(lon)))

surfaces = []
for i in range(len(lat) - 1):
    for j in range(len(lon) - 1):
        surfaces.append((
            j + i*len(lon),
            j+1 + i*len(lon),
            j+1 + (i+1)*len(lon),
            j + (i+1)*len(lon)
        ))

def globe(sunlight_data, i):

    glBegin(GL_QUADS)

    for i in range(len(surfaces)):

        glColor4fv((sunlight_data[i], 0, 0, 1))

        for vertex in surfaces[i]:

            glVertex3fv(vertices[vertex])

    glEnd()

    glBegin(GL_LINES)

    glColor4fv((1, 1, 1, 0.5))

    for edge in edges:

        for vertex in edge:

            glVertex3fv(vertices[vertex])

    glEnd()

def main(sunlight):

    i = 0

    pygame.init()

    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 500000.0)

    glTranslatef(0.0, 0.0, -10000.0)

    glRotatef(130, 1, 0, 0)

    glRotatef(10, 0, 0, 1)

    while True:

        if i == len(sunlight):

            i = 0

        sunlight_data = []

        for j in range(len(sunlight[i]) - 1):

            for k in range(len(sunlight[i][j]) - 1):

                sunlight_data.append(sunlight[i, j, k])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                quit()

        #glRotatef(1, 1, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        globe(sunlight_data, i)

        pygame.display.flip()

        pygame.time.wait(10)

        i += 1

main(sunlight)
