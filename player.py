from platform import java_ver
from card import Card
from deck import Deck

class Player:

    player_cards = []
    player_sum = 0


    def player_hit (self):

        print("you decided to hit!")
        card.player_display_card(deck.card_picker)


        for i in player.player_cards:
            if i == "j":
                player.player_cards[i] = "10"
            elif i == "q":
                player.player_cards[i] = "10"
            elif i == "k":
                player.player_cards[i] = "10"
            
            player_sum = player.player_sum + int(player.player_cards[i])

            print("The sum of your cards is now " + player_sum)

        return player_sum


    def player_stay (self):

        print("you decided to stay! ")

        player_sum = player.player_sum
        
        print("The final sum of your cards is " + player_sum)


        return player_sum
        






deck = Deck()
card = Card()
player = Player()