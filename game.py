from blackjack import Blackjack
from card import Card
from player import  Player
from computer import Computer 
from end_game import End_Game
from deck import Deck

blackjack = Blackjack()
card = Card()
player = Player()
computer = Computer()
end_game = End_Game()
deck = Deck()
    
class Game:
    def base_game(self):
        blackjack = Blackjack()
        card = Card()
        player = Player()
        computer = Computer()
        end_game = End_Game()
        deck = Deck()
        
        input("Lets play Blackjack! (press enter to continue) ")
        
        game_end = 0
        p_blackjack_counter = 0
        p_over_limit_counter = 0
        p_stay_counter = 0
        c_blackjack_counter = 0
        c_over_limit_counter = 0
        c_stay_counter = 0

        while game_end == 0:
            if p_blackjack_counter == 0 and p_over_limit_counter == 0 and p_stay_counter == 0:
                player_choice_counter = 0
                
                
                print("the current sum of all your cards is " + player.player_sum )
                
                
                while player_choice_counter == 0:
                    
                    player_choice = input("Would you like top Hit or Stay? ").lower()

                    if player_choice == "hit":

                        p_sum = player.player_hit()
                    else:
                        p_sum = player.player_stay()
                        p_stay_counter += 1

                blackjack.check_blackjack(p_sum)


            #########################################################################
            
            
            if c_blackjack_counter == 0 and c_over_limit_counter == 0 and c_stay_counter == 0:

                if computer.computer_sum < p_sum or computer.computer_sum < 18:
                
                    c_sum = computer.computer_hit()
            
                else: 
                    c_sum = computer.computer_stay()
                    c_stay_counter += 1

                blackjack.check_blackjack(c_sum)


            

            end_game.check_if_game_end()

        
Game()




        







