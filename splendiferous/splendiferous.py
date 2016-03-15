# based on various examples from http://programarcadegames.com/python_examples

import pygame

# Define some color constants
BACK_GREEN = (0,55,0)
BACK_GREEN_LINES = (16, 80, 16)
GEM_RUBY = (125, 16, 16)
GEM_SAPH = (16, 16, 125)
GEM_ONIX = (16, 16, 16)
GEM_DIAM = (240, 240, 240)
GEM_EMER = (16, 125, 16)
TOKEN = (240, 216, 16)
WHITE = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# draw grid lines
def draw_grid(screen, color):
    pass

def draw_gem(screen, color, x, y):
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    pygame.draw.polygon(screen, color, [[x+10, y], [x, y+10], [x, y+20], [x+10, y+30], [x+20, y+20], [x+20, y+10]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)


class Token_Bank(object):
    color = GEM_DIAM
    def __init__(self, color):
        self.color = color

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, TOKEN, [x+20, y+20], 20)
        draw_gem(screen, self.color, x+10, y+5)




# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Splendiferous")

diam_token = Token_Bank(GEM_DIAM)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # Call draw stick figure function
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    diam_token.draw(screen, 10, 20)

    pygame.draw.line(screen, green, [0, 0], [50, 30], 5)
 
    # Draw on the screen a green line from (0,0) to (50.75)
    # 5 pixels wide.
    pygame.draw.lines(screen, black, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
 
    # Draw on the screen a green line from (0,0) to (50.75)
    # 5 pixels wide.
    pygame.draw.aaline(screen, green, [0, 50], [50, 80], True)

    draw_gem(screen, GEM_DIAM, x, y)
    draw_gem(screen, GEM_EMER, x+10, y)
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
