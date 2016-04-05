# based on various examples from http://programarcadegames.com/python_examples

# TODO: might be fun to reskin for piggy banks that need feeding. Or plants and fertilizer?

import pygame
import random

import splendgame
import splendcards as ards
import splendconstants as ants

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5



# draw grid lines
def draw_grid(screen, color):
    pass



# Setup
pygame.init()
players = [ splendgame.HumanPlayer("Player 1"),
            splendgame.HumanPlayer("Player 2") ]
gamesession = splendgame.GameSession(players);
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Splendiferous")

# try defining this in constants
#font = pygame.font.Font(None, 18)

# setup token buttons
diam_token = ards.Token_Bank(ants.GEM_DIAM)
emer_token = ards.Token_Bank(ants.GEM_EMER)
ruby_token = ards.Token_Bank(ants.GEM_RUBY)
onix_token = ards.Token_Bank(ants.GEM_ONIX)
saph_token = ards.Token_Bank(ants.GEM_SAPH)
wild_token = ards.Token_Bank(ants.GEM_WILD)
tokens = [diam_token, emer_token, ruby_token, onix_token, saph_token, wild_token]

#test_noble = Noble_Card(100, 10, [0,0,3,3,3])
#test_noble2 = Noble_Card(180, 10)
nobles = [ards.Noble_Card(100, 10),
          ards.Noble_Card(180, 10),
          ards.Noble_Card(260, 10)]

test_mine = ards.Mine(ants.GEM_RUBY, 1, [0, 0, 2, 4, 0], 200, 200)
test_mine2 = ards.Mine(ants.GEM_SAPH, 4, [0, 0, 2, 4, 0], 300, 200)

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

            gamesession = splendgame.GameSession(2);

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(ants.BACK_GREEN)
    for row in range(20):
        for column in range(20):
            color = ants.BACK_GREEN_LINES
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

    #draw_gem(screen, ants.GEM_DIAM, x, y)
    #draw_gem(screen, ants.GEM_EMER, x+1, y+1)

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
