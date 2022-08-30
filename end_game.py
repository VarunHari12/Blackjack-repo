from blackjack import Blackjack
from card import Card
from player import  Player
from computer import Computer 
from game import Game
from deck import Deck

class End_Game:

    
    

    def check_if_game_end(self):

        blackjack = Blackjack()
        card = Card()
        player = Player()
        computer = Computer()
        game = Game()
        deck = Deck()

        if game.p_blackjack_counter == 1 or game.c_blackjack_counter == 1:

            if game.p_blackjack_counter == 1 and game.c_blackjack_counter != 1 :
                print("Congrats, you won by Blackjack! Your final sum was 21 and the computers final sum was " + computer.computer_sum)
                game.game_end += 1

            elif game.p_blackjack_counter == 1 and game.c_blackjack_counter == 1:
                print("You tied with the computer! You both got Blackjacks.")
                game.game_end += 1

            else: 
                print("Sorry, you lost by Blackjack! Your final sum was " + player.player_sum + "  and the computers final sum was 21")
                game.game_end += 1

        elif game.p_stay_counter == 1 or game.c_stay_counter == 1:
            
            if game.p_stay_counter > game.c_stay_counter:
                print("Congrats, you won! Your final sum was" + player.player_sum + "and the computers final sum was " + computer.computer_sum)
                game.game_end += 1

            elif game.p_stay_counter == game.c_stay_counter :
                print("You tied with the computer! You both got " + player.player_sum)
                game.game_end += 1

            else: 
                print("Sorry, you lost! Your final sum was" + player.player_sum + "and the computers final sum was " + computer.computer_sum)
                game.game_end += 1
        
        elif game.p_over_limit_counter == 1 or game.c_over_limit_counter == 1:

            if game.p_over_limit_counter == 1 and game.c_over_limit_counter != 1:
                print("Congrats, you won! Your final sum was" + player.player_sum + "and the computers final sum was " + computer.computer_sum)
                game.game_end += 1
            elif game.p_over_limit_counter == 1 and game.c_over_limit_counter == 1:
                print("You tied with the computer! You both went over 21.")
                game.game_end += 1
            else:
                print("Sorry, you lost! Your final sum was" + player.player_sum + "and the computers final sum was " + computer.computer_sum)
                game.game_end += 1







            



    