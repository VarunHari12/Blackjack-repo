import random
from deck import Deck
from player import Player

class Card:

    def __init__ (self, card_name):
        self.card_name = card_name

    def player_display_card(self, card_name):

        print("The card you drew was " + deck.card_picker(deck.cards_in_deck))
        player.player_cards.append(card_name[0])
        deck.cards_in_deck.remove(card_name)

    def computer_display_card(self, card_name):

        print("The card the computer drew was " + deck.card_picker(deck.cards_in_deck))
        deck.cards_in_deck.remove(card_name)

        






deck = Deck()
card = Card()
player = Player()

card.player_display_card(deck.card_picker(deck.cards_in_deck))