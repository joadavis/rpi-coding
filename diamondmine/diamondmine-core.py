#!/bin/python

# A core implementation of diamondmine
# joadavis Oct 23, 2017; Jan 20, 2018

import random

SUITS = ['diamond', 'spade', 'club', 'heart']

# TODO also include choice of deck
RULE_OPTIONS = { 'linear': { 'description': "Each diamond card is worth its rank",
                             'scoring': [1,2,3,4,5,6,7,8,9,10,11,12,13] },
                 'pinochle': { 'description': "Pinochle styled",
                               'scoring': [11,0,0,0,0,0,0,0,0,10,2,3,4] },
                 'stepped': { 'description': "Stepped value by 5s",
                               'scoring': [5,5,5,5,5,10,10,10,10,10,15,15,15] }
                 'steppedflat': { 'description': "Stepped flatter 5, 7, 9",
                                  'scoring': [5,5,5,5,5,7,7,7,7,7,9,9,9] }
               }


# Player class
# name
# hand
# played cards (tableau)
# score

# subclass humanplayer
# subclass aiplayer


# Game session
# list of players
# deck
# discard
# turn counter
# method for running the game
# method for game setup
# text output methods
# future: generic class access to allow curses or GUI

class GameSession(object):
  players = []
  draw_deck = []
  discard = []
  turn_count = 0

  def __init__(self):
    turn_count = 0
    discard = []

    # TODO: allow users to pick rule set    
    self.create_deck_and_shuffle()
    # players


  def create_deck_and_shuffle(self):
    self.draw_deck = []
    # cards are tuple of suit and rank
    for suit in SUITS:
      for rank in range(1,14):
        self.draw_deck.append((suit, rank))
    random.shuffle(self.draw_deck)


game = GameSession()

print(game.draw_deck)
