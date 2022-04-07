from human import Human
from computer import Computer
from player import Player


class Game:
    def __init__(self):
        self.player_one = Human('player_one')
        self.player_two = Player('player_two')

    def run_game(self):
        self.display_welcome_message()
        self.display_rules()
        self.player_type()
        self.game_play()
        self.display_winner()

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

    # As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.
    def player_type(self):
        response = input('How many players are playing this game? ')
        if response == '1' :
            self.player_two = Computer('player_two')
        elif response == '2' :
            self.player_two = Human('player_two')
    
    # As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
    def game_play(self):
        while self






        self.player_one.choose_gesture()
