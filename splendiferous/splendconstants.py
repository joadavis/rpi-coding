# define some constant values to share between the modules

import pygame

# Define some color constants
BACK_GREEN = (0,55,0)
BACK_GREEN_LINES = (16, 80, 16)
GEM_DIAM = (240, 240, 240)
GEM_RUBY = (125, 16, 16)
GEM_SAPH = (16, 16, 180)
GEM_EMER = (16, 125, 16)
GEM_ONIX = (16, 16, 16)
TOKEN = (240, 216, 16)
TOKEN2 = (216, 200, 8)
GEM_WILD = TOKEN2
NOBLE_BACK = (216, 200, 125)
MINE_BACK = (190, 125, 0)
WHITE = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
# define arbitrary color order with wild (gold) last
GEM_ORDER=[GEM_DIAM, GEM_RUBY, GEM_SAPH, GEM_EMER, GEM_ONIX, GEM_WILD]

font = pygame.font.Font(None, 18)
