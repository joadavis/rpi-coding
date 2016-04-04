import pygame
import random

import splendconstants


def draw_gem(screen, color, x, y):
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    pygame.draw.polygon(screen, color, [[x+10, y], [x, y+10], [x, y+20], [x+10, y+30], [x+20, y+20], [x+20, y+10]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)
    #pygame.draw.polygon(screen, color, [[x+10, y+10], [x, y+20], [x+20, y+20]], 5)

def draw_gem_small(screen, color, x, y):
    pygame.draw.polygon(screen, color, [[x+3, y], [x, y+3], [x, y+6], [x+3, y+9], [x+6, y+6], [x+6, y+3]])

class Token_Bank(object):
    color = splendconstants.GEM_DIAM
    def __init__(self, color):
        self.color = color

    def draw(self, screen, x, y):
        pygame.draw.circle(screen, splendconstants.TOKEN2, [x+20, y+20], 22)
        pygame.draw.circle(screen, splendconstants.TOKEN, [x+20, y+20], 20)
        draw_gem(screen, self.color, x+9, y+5)


class Mine(object):
    victory_point_value = 0
    color = splendconstants.GEM_DIAM
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
        pygame.draw.rect(screen, splendconstants.MINE_BACK, [self.x, self.y + 15, 60, 45])
        draw_gem(screen, self.color, self.x +5, self.y+20)
        if self.victory_point_value > 0:
            text = font.render("+" + str(self.victory_point_value), True, splendconstants.WHITE)
            screen.blit(text, [self.x + 45, self.y + 3])


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
        pygame.draw.rect(screen, splendconstants.NOBLE_BACK, [self.x, self.y, 50, 50])
        # TODO: print wants > 0
        # TODO: print victory point value (all the same, but good reminder)
        line_offset = 2
        for gem in range(len(self.wants)):
            if self.wants[gem] > 0:
                draw_gem_small(screen, splendconstants.GEM_ORDER[gem], self.x + 2, self.y + line_offset)
                text = font.render(str(self.wants[gem]), True, splendconstants.WHITE)
                screen.blit(text, [self.x + 12, self.y + line_offset - 2])
                line_offset = line_offset + 12
        text = font.render("+" + str(self.victory_point_value), True, splendconstants.WHITE)
        screen.blit(text, [self.x + 30, self.y + 30])
