# a simple attempt at a color matching, stack choosing card game
# this version has no graphics, just text output
# joadavis Oct 20, 2016

# Another attempt at a game in one .py file
# No AI for this version, just two players taking turns
# objects - cards, buttons [draw, place, take, help], game session (to track turns)
# need to display scores and player labels
# display a "who won" message at the end

import random

COLORS_2P = ["Orange", "Brown", "Gray", "Blue", "Red"]

# from http://www.gossamer-threads.com/lists/python/dev/760692
# ANSI colors
colours = {
'none' : "",
'default' : "\033[.0m",
'bold' : "\033[.1m",
'underline' : "\033[.4m",
'blink' : "\033[.5m",
'reverse' : "\033[.7m",
'concealed' : "\033[.8m",

'black' : "\033[.30m",
'red' : "\033[.31m",
'green' : "\033[.32m",
'yellow' : "\033[.33m",
'blue' : "\033[.34m",
'magenta' : "\033[.35m",
'cyan' : "\033[.36m",
'white' : "\033[.37m",

'on_black' : "\033[.40m",
'on_red' : "\033[.41m",
'on_green' : "\033[.42m",
'on_yellow' : "\033[.43m",
'on_blue' : "\033[.44m",
'on_magenta' : "\033[.45m",
'on_cyan' : "\033[46m",
'on_white' : "\033[47m",

'beep' : "\007",

# non-standard attributes, supported by some terminals
'dark' : "\033[.2m",
'italic' : "\033[3m",
'rapidblink' : "\033[6m",
'strikethrough': "\033[9m",
} 
# end clip from website

scoring_reminder = "1 card is 1 point, 2 is 3, 6, 10, 15, 21 max."
# alternate is 1 4 8 7 6 5
scoring_lookup = [0, 1, 3, 6, 10, 15, 21, 21, 21, 21] # only 9 cards of each color
card_runout_count = 15 # can increase to shorten game in testing


class Player(object):
    # a list of the colored cards, sorted by number of cards
    # store a tuple of (color, count)
    ordered_stacks = []
    done_for_round = False
    name="Player X"
    num_jokers = 0
    bonus = 0
    score = 0

    def __init__(self):
        # let empty stacks exist
        self.ordered_stacks = []
        self.num_jokers = 0
        self.bonus = 0
        # urgh. want an ordered dictionary sorted by card count
        # maybe I just take the hit on sorting each turn because it will change each turn
        self.done_for_round = False

    def __str__(self):
        return "--> {}\n--> {} and {} jokers with {} bonus".format(self.name, self.ordered_stacks, self.num_jokers, self.bonus)

    def take(self, stack):
        for card in stack:
            if card == "joker":
                self.num_jokers += 1
            elif card == "+2":
                self.bonus += 2
            # if there is an existing ord stack, add it
            # if not, create one
            # thought 1 - if we had populated elements for all colors, could just list comprehension it
            # thought 2 - more 'efficient' to not check all elements to do simple update, so search only til find match (or no match if not pre-populate)
            # its a short list (5 or 7 colors) so not a big deal either way
            # if was a really long list, lookup would be faster with hash or dict, but then also need to track which were non-empty in a second data structure
            else:
                updated = False
                for index, ord_stack in enumerate(self.ordered_stacks):
                    st_color, st_count = ord_stack
                    if st_color == card:
                        st_count += 1
                        self.ordered_stacks[index] = (st_color, st_count)
                        updated = True
                if not updated:
                    # create a new stack
                    self.ordered_stacks.append((card, 1))
            print(card)
        # TODO sort by count
        print("done take {}".format(self.ordered_stacks))

    def print_score(self):
        #print("i dunno, like 0?")
        # this is kinda tricky - dict is not sorted
        # thinking - get a list of all the scores for the colors, 
        # then sort thelist, then first 3 of list + rest -
        # ah, but what about jokers?  if just have score, how do we know what the next score in scoring is?
        color_scores = []
        #for color in self.
        #but using a list of tuples, not dict

        self.score = self.bonus # start with bonus
        jokers_to_use = self.num_jokers
        if len(self.ordered_stacks) > 1:
            to_score_positive = 3
            for stack in self.ordered_stacks:
                #st_color, st_count = self.ordered_stacks[0]
                st_color, st_count = stack
                while jokers_to_use > 0 and st_count < 6:
                    jokers_to_use -= 1
                    st_count += 1
                st_score = scoring_lookup[st_count]
                color_scores.append(st_score)
                if to_score_positive > 0:
                    self.score = self.score + st_score
                    print("{} scored {} for {} cards".format(st_color, st_score, st_count))
                else:
                    self.score = self.score - st_score
                    print("{} scored -{} for {} cards".format(st_color, st_score, st_count))
            to_score_positive -= 1
        # done. sum the color_scores then add bonus, store in self.score
        print("  TOTAL SCORE is {}".format(self.score))


class GameSession(object):
    players = []
    deck = []
    fresh_deck_2p = []
    stacks = []
    stack_limit_2p = [1, 2, 3]

    def __init__(self):
        # future: more players
        if len(self.fresh_deck_2p) < 1:
            self.generate_deck_2p()
        self.stacks = [[] for i in self.stack_limit_2p]
        put_back = []
        for i in range(2):
            pla = Player()
            pla_name = input("What is your name Player {}? ".format(i))
            if len(pla_name) > 1:
                pla.name = pla_name
            else:
                pla.name = "Player " + str(i)
            self.players.append(pla)
            # give each player two non matching color cards
            # put any that match into a list to go back
            start_2 = []
            picked_card = self.deck.pop()
            while picked_card == "joker" or picked_card == "+2":
                put_back.append(picked_card)
                picked_card = self.deck.pop()
            picked_card_2 = self.deck.pop()
            while picked_card_2 == "joker" \
              or picked_card_2 == "+2" \
              or picked_card_2 == picked_card:
                put_back.append(picked_card_2)
                picked_card_2 = self.deck.pop()
            pla.take([picked_card, picked_card_2])
        self.deck = self.deck + put_back

        
    def generate_deck_2p(self):
        self.fresh_deck_2p = ["joker"] * 3
        self.fresh_deck_2p.extend(["+2"] * 10)
        for color in COLORS_2P:
            self.fresh_deck_2p.extend([color] * 9)
        random.shuffle(self.fresh_deck_2p)
        
        print(self.fresh_deck_2p)
        self.deck = self.fresh_deck_2p # thinking I'd just reshuffle later

    def can_draw_and_place(self):
        can_place = []
        # todo refactor into elegant python code
        for index in range(len(self.stack_limit_2p)):
            if not self.stacks[index] == None \
               and len(self.stacks[index]) < self.stack_limit_2p[index]:
                can_place.append(index)
        return can_place

    def can_take(self):
        ''' return a list of stacks that may be taken '''
        # todo: refactor as a list comprehension?
        takeable_stacks = []
        for index in range(len(self.stacks)):
            if self.stacks[index] != None and len(self.stacks[index]) > 0:
                takeable_stacks.append(index)
        return takeable_stacks

    def __str__(self):
        return "\nStack 1 {} limit {}\n" \
               "Stack 2 {} limit {}\n" \
               "Stack 3 {} limit {}".format(
                   self.stacks[0], self.stack_limit_2p[0],
                   self.stacks[1], self.stack_limit_2p[1],
                   self.stacks[2], self.stack_limit_2p[2])

###
# Start playing the game

gs = GameSession()

for pla in gs.players:
    print(pla)

# round loop
game_running = True
#while len(gs.deck) > 15:
while game_running:
    # turn loop
    for pla in gs.players:
        print(gs)
        #print("\n{}=========={}\n{}".format(colours['red'], colours['default'], pla))
        print("\n==========\n{}".format( pla))
        pla.done_for_turn = False
        while not pla.done_for_round and not pla.done_for_turn:
            # Determine what are valid moves for the player
            # TODO: if all stacks full, cant draw
            open_stacks = gs.can_draw_and_place()
            takeable = gs.can_take()
            
            if len(takeable) > 0:
                # TODO incrrment displayed values by one
                print("You can take one of {} stacks " \
                      "by pressing its number.".format(takeable))
            if len(open_stacks) > 0:
                print("You can draw a card by pressing d.")
            act = input("What is your choice? ")
            if act.startswith("d") and len(open_stacks) > 0:
                card = gs.deck.pop()
                while not pla.done_for_turn:
                    print("Can place a card in {}.".format(open_stacks))
                    act2 = input("Card is {}. Put it where? ".format(card))
                    
                    # convert to int
                    # check it was a valid choice, and stack has room
                    # place card
                    if act2.startswith("1") and 0 in open_stacks:
                        gs.stacks[0].append(card)
                        pla.done_for_turn = True
                    if act2.startswith("2") and 1 in open_stacks:
                        gs.stacks[1].append(card)
                        pla.done_for_turn = True
                    if act2.startswith("3") and 2 in open_stacks:
                        gs.stacks[2].append(card)
                        pla.done_for_turn = True
                    else:
                        print(">> Invalid choice, please try again! <<")
                
            elif act.startswith("1") and gs.stacks[0] != None:
                # take first stack
                pla.take(gs.stacks[0])
                gs.stacks[0] = None
                pla.done_for_round = True
                pla.done_for_turn = True
            elif act.startswith("2") and gs.stacks[1] != None:
                # take second stack
                pla.take(gs.stacks[1])
                gs.stacks[1] = None
                pla.done_for_round = True
                pla.done_for_turn = True
            elif act.startswith("3") and gs.stacks[2] != None:
                # take third stack
                pla.take(gs.stacks[2])
                gs.stacks[2] = None
                pla.done_for_round = True
                pla.done_for_turn = True
            else:
                print(">> Invalid choice, try again. <<")
    print("=== End of player turns ===\n")
    #if all players done for round:  or if num stacks taken
        # dump remaining stack
        # reset done flags
    if gs.players[0].done_for_round and gs.players[1].done_for_round:
        print("=== reset round   ...:::::....:::::...")
        #for stack in gs.stacks:
        #    stack = []
        gs.stacks[0] = []
        gs.stacks[1] = []
        gs.stacks[2] = []
        gs.players[0].done_for_round = False
        gs.players[1].done_for_round = False
        # check for game end at end of round
        if len(gs.deck) < card_runout_count:
            game_running = False
            print("=== final round was triggered. time for scoring")
    #else:
    #    print("{} dr = {}".format(gs.players[0].name, gs.players[0].done_for_round))
    # TODO maybe num remaining stacks <= 1 (which is total num stacks - num players)?  

    # test
    #gs.players[0].take(COLORS_2P)

# calculate scores and winner
winning_score = 0
winning_player = "Its a tie!"
for pla in gs.players:
    print(pla.name)
    pla.print_score()
    if pla.score > winning_score:
        winning_score = pla.score
        winning_player = pla.name
    elif pla.score == winning_score:
        winning_player = "Its a tie!"
print("With {} points the winner is... {}".format(winning_score, winning_player))
print("\nGame is done. Hope you enjoyed it.\n")

