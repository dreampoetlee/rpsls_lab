from human import Human
from computer import Computer
from player import Player


class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = Player

    def display_welcome_message(self):
        print("Welcome to Rock,Paper,Scissors,Lizard,Spock!!!")

    def display_rules(self):
        print("Here are the rules for the Game!")
        print("Rock crushes Scissors!!")
        print("Scissors cuts Paper, Paper covers Rock!")
        print("Rock crushes Lizard")
        print("But Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard. Brutal!")
        print("Lizard eats Paper, Nom!")
        print("Paper disproves Spock")
        print("And Spock vaporizes Rock!")
    
