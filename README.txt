Sunlit_surface V0.1.11
Date: 08.04.2018
Author: Thibaut Voirand

Mercury has an eccentric orbit and an orbital resonance of 3:2. In consequence, the surface is not
evenly sunlit. This phenomena is quite difficult to visualize. The purpose of this script is to
develop an animation showing the temporal evolution of the sunlit areas of Mercury. It can
potentially be used for the case of any other planet orbiting a star.

Added in this version:
 - glEnable(GL_DEPTH_TEST) added in animod: surfaces now opaque
 - SCALE_FACTOR added in animod to shorten distances: nothing was displaying when distances above
 1e3 km
