# based on various examples from http://programarcadegames.com/python_examples

# TODO: might be fun to reskin for piggy banks that need feeding. Or plants and fertilizer?

import pygame
import random

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

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5



# draw grid lines
def draw_grid(screen, color):
    pass

def draw_gem(screen, color, x, y):
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    pygame.draw.polygon(screen, color, [[x+10, y], [x, y+10], [x, y+20], [x+10, y+30], [x+20, y+20], [x+20, y+10]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)

def draw_gem_small(screen, color, x, y):
    pygame.draw.polygon(screen, color, [[x+3, y], [x, y+3], [x, y+6], [x+3, y+9], [x+6, y+6], [x+6, y+3]])

class Token_Bank(object):
    color = GEM_DIAM
    def __init__(self, color):
        self.color = color

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, TOKEN2, [x+20, y+20], 22)
        pygame.draw.circle(screen, TOKEN, [x+20, y+20], 20)
        draw_gem(screen, self.color, x+9, y+5)


class Mine(object):
    victory_point_value = 0
    color = GEM_DIAM
    costs = [7,7,7,7,7]
    x = 1
    y = 1
    def __init__(self, color, vp, costs, x, y):
        self.color = color
        self.victory_point_value = vp
        self.costs = costs
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, 60, 15])
        pygame.draw.rect(screen, MINE_BACK, [self.x, self.y + 15, 60, 45])


def pick_two(max=4):
    """ pick a number from 0 to max inclusive, then pick another number from 0 to max inclusive
        default from 0 to 4
        returns tuple with smallest number first
    """
    num1 = random.randint(0, max-1)  # why -1?  to leave room for the second number
    num2 = random.randint(0, max-1)
    print(num1, " ", num2)
    if num2 >= num1:
        num2 = num2 + 1 # add back in the -1 if second number is after first
        return (num1, num2)
    else:
        return (num2, num1) # put the smaller number first


class Noble_Card(object):
    victory_point_value = 3
    wants = [4, 4, 4, 4, 4]  # higher than any expectation
    x = 1
    y = 1
    
    def __init__(self, x, y, wants = []):
        #self.wants = wants
        self.x = x
        self.y = y
        if wants == []:
            num1, num2 = pick_two()
            if random.randint(0,1):
                # two 4s
                self.wants = [0,0,0,0,0]
                self.wants[num1] = 4
                self.wants[num2] = 4
            else:
                # three 3s
                self.wants = [3,3,3,3,3]
                self.wants[num1] = 0
                self.wants[num2] = 0
        else:
            self.wants = wants
        print(self.wants)
        
    def draw(self, screen):
        # upper left corner x and y then width and height (downward)
        pygame.draw.rect(screen, NOBLE_BACK, [self.x, self.y, 50, 50])
        # TODO: print wants > 0
        # TODO: print victory point value (all the same, but good reminder)
        line_offset = 2
        for gem in range(len(self.wants)):
            if self.wants[gem] > 0:
                draw_gem_small(screen, GEM_ORDER[gem], self.x + 2, self.y + line_offset)
                text = font.render(str(self.wants[gem]), True, WHITE)
                screen.blit(text, [self.x + 12, self.y + line_offset - 2])
                line_offset = line_offset + 12
        text = font.render("+" + str(self.victory_point_value), True, WHITE)
        screen.blit(text, [self.x + 30, self.y + 30])


# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Splendiferous")

font = pygame.font.Font(None, 18)

# setup token buttons
diam_token = Token_Bank(GEM_DIAM)
emer_token = Token_Bank(GEM_EMER)
ruby_token = Token_Bank(GEM_RUBY)
onix_token = Token_Bank(GEM_ONIX)
saph_token = Token_Bank(GEM_SAPH)
wild_token = Token_Bank(GEM_WILD)
tokens = [diam_token, emer_token, ruby_token, onix_token, saph_token, wild_token]

#test_noble = Noble_Card(100, 10, [0,0,3,3,3])
#test_noble2 = Noble_Card(180, 10)
nobles = [Noble_Card(100, 10), Noble_Card(180, 10), Noble_Card(260, 10)]

test_mine = Mine(GEM_RUBY, 1, [0, 0, 2, 4, 0], 200, 200)
test_mine2 = Mine(GEM_SAPH, 4, [0, 0, 2, 4, 0], 300, 200)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            click_pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = click_pos[0] // (WIDTH + MARGIN)
            row = click_pos[1] // (HEIGHT + MARGIN)
            # Set that location to zero
            #grid[row][column] = 1
            print("Click ", click_pos, "Grid coordinates: ", row, column)

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BACK_GREEN)
    for row in range(20):
        for column in range(20):
            color = BACK_GREEN_LINES
            #if grid[row][column] == 1:
            #    color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    
    offset = 0
    for token in tokens:
        offset = offset + 50
        token.draw(screen, 10 + offset, 380)

    #pygame.draw.line(screen, green, [0, 0], [50, 30], 5)
 
    # Draw on the screen a green line from (0,0) to (50.75)
    # 5 pixels wide.
    #pygame.draw.lines(screen, black, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
 
    #pygame.draw.aaline(screen, green, [0, 50], [50, 80], True)

    draw_gem(screen, GEM_DIAM, x, y)
    draw_gem(screen, GEM_EMER, x+1, y+1)

    #test_noble.draw(screen)
    #test_noble2.draw(screen)
    for noble in nobles:
        noble.draw(screen)

    test_mine.draw(screen)
    test_mine2.draw(screen)
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
