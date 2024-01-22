# Number Slider, by Gabriel Coffey, based on a project by Al Swelgart, v0.0

import sys, random, pygame
# sys module provides access to system resources (i.e. Operating system commands)

from pygame.locals import *
# allows us to call functions from pygame using just the function name instead of module.functions
# Example: We can use draw() instead of pygame.draw()

# Constants for the Game Board
BOARDWIDTH = 4 # COLLUMS
BOARDHEIGHT = 4 # ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 # This is a maximum value! Don't make a slow computer run faster.
BLANK = none

# COLOR VALUES in (R, G, B) format.
# 0 = no Value, 255 = Max Value
BLACK = (0, 0, 0)
White = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

