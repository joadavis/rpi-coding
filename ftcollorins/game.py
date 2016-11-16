# a simple attempt at a color matching, stack choosing card game
# joadavis Oct 20, 2016

# Another attempt at a game in one .py file
# No AI for this version, just two players taking turns
# objects - cards, buttons [draw, place, take, help], game session (to track turns)
# need to display scores and player labels
# display a "who won" message at the end


import pygame
import random

GAME_WHITE = (250, 250, 250)
GAME_BLACK = (0, 0, 0)
GAME_GREEN = (0,55,0)
GAME_SPLASH = (25, 80, 25)

class GameSession(object):
    pass


class SomeButton(pygame.sprite.Sprite):
    label = ""
    def __init__(self, x, y):
        super().__init__()
        # image setup
        self.image = pygame.Surface([40,20])
        self.init_draw(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def init_draw(self, screen):
        pygame.draw.rect(screen, GAME_BLACK, [0, 0, 50, 50])


class SplashBox(pygame.sprite.Sprite):
    welcome_message = ["Welcome to Fort Collorins.","",
                       "This is a two player card game.",
                       "On your turn, either draw a new card and place it on a pile,", "  or choose a pile to add to your stacks.",
                       "Play until there are less than 15 cards left in deck.",
                       "Only your three largest stacks are scored for you,", "  the rest count against your score.",
                       "", "Click this dialog to begin." ]
    rect = [0,0,1,1]
    def __init__(self, x, y):
        super().__init__()
        print("splash init")

        # image setup
        self.image = pygame.Surface([400,250])
        self.init_draw(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        print("Splash")
        pass
    
    def init_draw(self, screen):
        # now using sprite, so coords relative within sprite image (screen)
        # upper left corner x and y then width and height (downward)
        pygame.draw.rect(screen, GAME_SPLASH, self.rect)
        infont = pygame.font.Font(None, 18)
        for msg_id in range(len(self.welcome_message)):
            text = infont.render(self.welcome_message[msg_id], True, GAME_WHITE)
            screen.blit(text, [30, 30 + msg_id * 18])
        
        
class Card(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.flip = 0 # face down

        # image setup
        self.image = pygame.Surface([50,50])
        self.init_draw(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        print("upd")
        pass
    
    def init_draw(self, screen):
        # now using sprite, so coords relative within sprite image (screen)
        # upper left corner x and y then width and height (downward)
        pygame.draw.rect(screen, GAME_BLACK, [0, 0, 50, 50])
        
        

def draw_finger(screen, x, y):
    pygame.draw.polygon(screen, GAME_WHITE,
                        [ [x,y], [x+2, y], [x+2, y+5],
                          [x+8, y+5], [x+7, y+15],
                          [x+1, y+15], [x, y] ] )

# Setup --------------------------------------
pygame.init()

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ft. Collorins")

# try defining this in constants
afont = pygame.font.Font(None, 18)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)

splash = SplashBox(100, 100)
dialog_group = pygame.sprite.Group()
dialog_group.add(splash)
splash_show = True
 
# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    click_event = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            click_pos = pygame.mouse.get_pos()
            print("Click ", click_pos)
            click_event = True


    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    
    # First, clear the screen to ___. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill( (0,55,0) )

    if splash_show:
        dialog_group.draw(screen)
        if click_event and splash.rect.collidepoint(click_pos[0], click_pos[1]):
            splash_show = False

    draw_finger(screen, x, y)
    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
