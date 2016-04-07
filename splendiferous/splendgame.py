# Class to contain game logic
# kind of a controlling class that takes charge
# joadavis 21 Mar 2016

import pygame
import random

# import splendiferous
import splendcards
import splendconstants as ants

pass # this is unused now, all back in main class

class GameSession(object):
    players = []
    bank_tokens = []
    noble_gallery = []
    mines_deck_I = []
    mines_deck_II = []
    mines_deck_III = []

    def __init__(self, players):
        for player in players:
            player.newGame()
        self.players = players
        if len(players) == 2:
            self.bank_tokens = [5,5,5,5,5,7]
            self.noble_gallery = [splendcards.Noble_Card(20, 10),
                                  splendcards.Noble_Card(70, 10),
                                  splendcards.Noble_Card(120,10)]
        else:
            print("unsupported number of players")


class GenericPlayer(object):
    name = "generic"
    score = 0

    def __init__(self, name):
        self.name = name

    def newGame(self):
        self.score = 0


class HumanPlayer(GenericPlayer):

    def __init__(self, name):
        self.name = name  # TODO make this a super call
