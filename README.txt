Sunlit_surface V0.1.11
Date: 29.04.2018
Author: Thibaut Voirand

Mercury has an eccentric orbit and an orbital resonance of 3:2. In consequence, the surface is not
evenly sunlit. This phenomena is quite difficult to visualize. The purpose of this script is to
develop an animation showing the temporal evolution of the sunlit areas of Mercury. It can
potentially be used for the case of any other planet orbiting a star.

Added in this version:
 - science_mod doesn't use math module anymore (numpy only, syntax of power differs)
 - science_mod renamed: scmod
 - animation_3D_mod renamed: animod
 - "from ... import *" discarded in main and animod, now "import ..."
 - twilight function now a subfunction of compute sunlight
