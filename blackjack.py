
class Blackjack:

    def __init__ (self, sum_of_cards):
        self.sum_of_cards = sum_of_cards


    def check_blackjack(self, sum_of_cards):

        if sum_of_cards == 21:

            return True

        else:

            return False


