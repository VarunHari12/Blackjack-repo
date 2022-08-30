from card import Card
from deck import Deck

class Computer:

    computer_cards = []
    computer_sum = 0


    def computer_hit (self):

        print("The computer decided to hit!")
        card.computer_display_card(deck.card_picker)


        for i in computer.computer_cards:
            if i == "j":
                computer.computer_cards[i] = "10"
            elif i == "q":
                computer.computer_cards[i] = "10"
            elif i == "k":
                computer.computer_cards[i] = "10"
            
            computer_sum = computer.computer_sum + int(computer.computer_cards[i])

            print("The sum of the computer's cards is now " + computer_sum)


        return computer_sum
        
    
    def computer_stay (self):

        print("you decided to stay! ")

        computer_sum = computer.computer_sum
        
        print("The final sum of your cards is " + computer_sum)


        return computer_sum
        
        






deck = Deck()
card = Card()
computer = Computer()