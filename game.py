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
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!!!")

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
        while True:
            print(f"Player one's chosen gesture is: {self.player_one.chosen_gesture}, and Player two's chosen gesture is: {self.player_two.chosen_gesture} ")



            #  = input(f'You have chosen to play{self.player_one.chosen_gesture}, the computer has chosen {self.player_two.chosen_gesture} ')

           # self.player_one.choose_gesture()

    def display_winner(self) :
        if self.player_one.man_wins == 2 :
            print(f'{self.player_one} wins the game!')
        elif self.player_two.machine_wins == 2 :
            print(f'{self.player_two} wins the game!')