# based on various examples from http://programarcadegames.com/python_examples
# also http://thepythongamebook.com

# TODO: might be fun to reskin for piggy banks that need feeding. Or plants and fertilizer?

import pygame
import random

#import splendgame
#import splendcards as ards
import splendconstants as ants

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5


# some generic drawing functions --------------

def draw_gem(screen, color, x, y):
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    pygame.draw.polygon(screen, color, [[x+10, y], [x, y+10], [x, y+20], [x+10, y+30], [x+20, y+20], [x+20, y+10]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)

def draw_gem_small(screen, color, x, y):
    pygame.draw.polygon(screen, color, [[x+3, y], [x, y+3], [x, y+6], [x+3, y+9], [x+6, y+6], [x+6, y+3]])

# use a 12x20 space
def draw_noble_icon(screen, x, y):
    pygame.draw.polygon(screen, ants.WHITE,
                        [ [x, y], [x+2, y+3], [x + 4, y], [x+6, y+3], [x+8, y],
                          [x+10, y+3], [x+12, y],
                          [x+12, y+8], [x+10, y+10],
                          [x+11, y+12], [x+11, y+20], [x+1, y+20],
                          [x+1, y+12], [x+2, y+10],
                          [x, y+8], [x, y] ])


def draw_finger(screen, x, y):
    pygame.draw.polygon(screen, ants.WHITE,
                        [ [x,y], [x+2, y], [x+2, y+5],
                          [x+8, y+5], [x+8, y+15],
                          [x, y+15], [x, y] ] )
                         

# some classes --------------------------------

class GameSession(object):
    players = []
    bank_tokens = []
    noble_gallery = None
    mines_deck_I = None
    mines_deck_II = None
    mines_deck_III = None
    all_sprites = None

    def __init__(self, players):
        self.all_sprites = pygame.sprite.Group()
        self.noble_gallery = pygame.sprite.Group()
        self.mines_deck_I = pygame.sprite.Group()
        self.mines_deck_II = pygame.sprite.Group()
        self.mines_deck_III = pygame.sprite.Group()
        self.mines_backs = pygame.sprite.Group()
        for player in players:
            player.newGame()
        self.players = players
        if len(players) == 2:
            self.bank_tokens = [5,5,5,5,5,7]
            self.noble_gallery.add(Noble_Card(100, 10))
            self.noble_gallery.add(Noble_Card(180, 10))
            self.noble_gallery.add(Noble_Card(260, 10))
        else:
            print("unsupported number of players")
        # TODO generate mines for each deck
        self.mines_deck_III.add( Mine(ants.GEM_RUBY, 3, [0,0,3,7,0], 3, 10, 10) )
        
        # collect up all sprites
        self.all_sprites.add(self.noble_gallery)
        self.all_sprites.add(self.mines_deck_I)
        self.all_sprites.add(self.mines_deck_II)
        self.all_sprites.add(self.mines_deck_III)

    def generateMines(self, level):
        """ level expressed as an int from 1 to 3 """
        if level > 3 or level < 1:
            # TODO throw an exception
            return None
        


class GenericPlayer(object):
    name = "generic"
    score = 0
    turncount = 0
    tokens = [0,0,0,0,0,0]
    hand = None
    played_sprites = None
    played_vals = [0,0,0,0,0]

    def __init__(self, name):
        self.name = name

    def newGame(self):
        self.score = 0
        self.turncount = 0

    def canBuy(self, wants):
        """ Given a list of wanted tokens (wild gold will be ignored),
            determine if the player has enough tokens.
            return a list of what would be left or None
            """
        remaining_tokens = list(self.tokens)
        for want_token in range(5):
            if wants[want_token] > remaining_tokens[want_token]:
                # are there enough wild gold to cover deficit?
                deficit = wants[want_token] - remaining_tokens[want_token]
                if remaining_tokens[5] >= deficit:
                    remaining_tokens[5] = remaining_tokens[5] - deficit
                    remaining_tokens[want_token] = 0
                else:
                    return None
            else:
                remaining_tokens[want_token] = remaining_tokens[want_token] - wants[want_token]
        return remaining_tokens


class HumanPlayer(GenericPlayer):

    def __init__(self, name):
        self.name = name  # TODO make this a super call


# tODO have a surface class for the background, to make it pretty once


class Token_Bank(pygame.sprite.Sprite):
    color = ants.GEM_DIAM
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color

        self.image = pygame.Surface([ants.TOKEN_SIZE, ants.TOKEN_SIZE])
        pygame.draw.circle(self.image, ants.TOKEN2, [20, 20], 22)
        pygame.draw.circle(self.image, ants.TOKEN, [20, 20], 20)
        draw_gem(self.image, self.color, 9, 5)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    

class Mine(pygame.sprite.Sprite):
    victory_point_value = 0
    color = ants.GEM_DIAM
    costs = [7,7,7,7,7]
    level = 1
    faceup = False

    def __init__(self, color, vp, costs, level, x, y):
        super().__init__()
        self.color = color
        self.victory_point_value = vp
        self.costs = costs
        self.image = pygame.Surface([ants.MINE_SIZE, ants.MINE_SIZE])
        self.localdraw_back(self.image)
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def make_faceup(self):
        if faceup == True:
            self.image = pygame.Surface([ants.MINE_SIZE, ants.MINE_SIZE][60, 60])
            self.image.fill(color)
            self.localdraw(self.image)
            # Fetch the rectangle object that has the dimensions of the image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    
    def update(self):
        pass

    def localdraw_back(self, screen):
        # determine the back color and level
        if self.level == 1:
            b_color = ants.MINE_BACK_I
            b_level = "I"
        elif self.level == 2:
            b_color = ants.MINE_BACK_II
            b_level = "II"
        elif self.level == 3:
            b_color = ants.MINE_BACK_III
            b_level = "III"

        self.image = pygame.Surface([ants.MINE_SIZE, ants.MINE_SIZE])
        lofont = pygame.font.SysFont("serif", 36)
        pygame.draw.rect(self.image, ants.MINE_BACK,
                         [0, 0, ants.MINE_SIZE, ants.MINE_SIZE])
        pygame.draw.polygon(self.image, b_color,
                            [ [0, ants.MINE_SIZE], [ants.MINE_SIZE - 20, 0],
                              [ants.MINE_SIZE, 0], [20, ants.MINE_SIZE] ] )
        b_text = lofont.render(b_level,
                               True, ants.WHITE)
        self.image.blit(b_text, [(ants.MINE_SIZE // 2) - (b_text.get_width() // 2),
                                 (ants.MINE_SIZE // 2) - (b_text.get_height() // 2)])
        
    def localdraw(self, screen):
        lofont = pygame.font.Font(None, 18)
        pygame.draw.rect(screen, self.color, [0, 0, ants.MINE_SIZE, 15])
        pygame.draw.rect(screen, ants.MINE_BACK, [0, 0 + 15, ants.MINE_SIZE, 45])
        draw_gem(screen, self.color, 5, 20)
        if self.victory_point_value > 0:
            text = lofont.render("+" + str(self.victory_point_value),
                               True, ants.WHITE)
            self.image.blit(text, [45, 3])


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


class Noble_Card(pygame.sprite.Sprite):
    victory_point_value = 3
    wants = [4, 4, 4, 4, 4]  # higher than any expectation
    
    def __init__(self, x, y, wants = []):
        super().__init__()  # ommitting this will cause an "object has no attribute '_Sprite__g'" error

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
        pygame.draw.rect(screen, ants.NOBLE_BACK, [0, 0, 50, 50])
        infont = pygame.font.Font(None, 18)
        # TODO: print wants > 0
        # TODO: print victory point value (all the same, but good reminder)
        line_offset = 2
        for gem in range(len(self.wants)):
            if self.wants[gem] > 0:
                draw_gem_small(screen, ants.GEM_ORDER[gem], 2, line_offset)
                text = infont.render(str(self.wants[gem]), True, ants.WHITE)
                screen.blit(text, [12, line_offset - 2])
                line_offset = line_offset + 12
        draw_noble_icon(screen, 29, 5)
        text = infont.render("+" + str(self.victory_point_value),
                           True, ants.WHITE)
        screen.blit(text, [30, 30])


# draw grid lines
def draw_grid(screen, color):
    pass



# Setup --------------------------------------
pygame.init()
players = [ HumanPlayer("Player 1"),
            HumanPlayer("Player 2") ]
gamesession = GameSession(players);
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Splendiferous")

# try defining this in constants
afont = pygame.font.Font(None, 18)

# setup token buttons
diam_token = Token_Bank(ants.GEM_DIAM, 10, 380)
emer_token = Token_Bank(ants.GEM_EMER, 60, 380)
ruby_token = Token_Bank(ants.GEM_RUBY, 110, 380)
onix_token = Token_Bank(ants.GEM_ONIX, 160, 380)
saph_token = Token_Bank(ants.GEM_SAPH, 210, 380)
wild_token = Token_Bank(ants.GEM_WILD, 280, 380)
tokens = [diam_token, emer_token, ruby_token, onix_token, saph_token, wild_token]
token_group = pygame.sprite.Group()
token_group.add(tokens)


test_mine = Mine(ants.GEM_RUBY, 1, [0, 0, 2, 4, 0], 1, 200, 200)
test_mine2 = Mine(ants.GEM_SAPH, 4, [0, 0, 2, 4, 0], 2, 300, 200)
gamesession.mines_deck_I.add(test_mine)
gamesession.mines_deck_II.add(test_mine2)

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
                              WIDTH, HEIGHT])
    
    #offset = 0
    #for token in tokens:
    #    offset = offset + 50
    #    token.draw(screen, 10 + offset, 380)
    token_group.draw(screen)

    #pygame.draw.line(screen, green, [0, 0], [50, 30], 5)
 
    # Draw on the screen a green line from (0,0) to (50.75)
    # 5 pixels wide.
    #pygame.draw.lines(screen, black, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
 
    #pygame.draw.aaline(screen, green, [0, 50], [50, 80], True)

    # mouse follow
    #draw_gem(screen, ants.GEM_DIAM, x, y)
    #draw_gem(screen, ants.GEM_EMER, x+1, y+1)
    draw_finger(screen, x, y)

    # testin' fun
    gamesession.mines_deck_III.sprites()[0].rect.y = gamesession.mines_deck_III.sprites()[0].rect.y + 1
    

    gamesession.all_sprites.draw(screen)

 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
