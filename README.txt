Sunlit_surface V0.1.15
Date: 20181001
Author: Thibaut Voirand

Mercury has an eccentric orbit and an orbital resonance of 3:2. In consequence, the surface is not
evenly sunlit. This phenomena is quite difficult to visualize. The purpose of this script is to
develop an animation showing the temporal evolution of the sunlit areas of Mercury. It can
potentially be used for the case of any other planet orbiting a star.

Added in this version:
 - writing_output_text_file function moved to main
 - time, lat, lon, sunlight deleted in writing_output_text_file
 - error in scmod function from_orbital_to_cartesian_coordinates corrected (position formula y)
