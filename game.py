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
        print("Welcome to an exciting game of  Rock, Paper, Scissors, Lizard, Spock!!!")

    def display_rules(self):
        print("Here are the rules for the Game!")

        print("Rock crushes Scissors!!")
        print("Rock crushes Lizard")

        print("Paper covers Rock!")
        print("Paper disapproves Spock")

        print("Spock vaporizes Rock!")
        print("Spock smashes Scissors")

        print("Scissors cuts Paper!")
        print("Scissors decapitates Lizard. Brutal!")
                
        print("But Lizard poisons Spock")
        print("Lizard eats Paper, Nom!")       

    # As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.
    def player_type(self):
        response = input('How many players are playing this game? ')
        if response == '1' :
            self.player_two = Computer('player_two')
        elif response == '2' :
            self.player_two = Human('player_two')
    def game_play(self):# As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
        while self.player_one.round_won < 2 and self.player_two.round_won < 2 :
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
        # As a player, I want the correct player to win a given round based on the choices* made by each player.
        #^ Player one Chooses Rock        
        if self.player_one.chosen_gesture == 'rock' :
            if self.player_two.chosen_gesture == 'rock' :
                print("It's a TIE!!")
            elif self.player_two.chosen_gesture == 'scissors' :
                print('Rock crushes Scissors!! You Win!!!')
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'lizard' :
                print("Yippe!! Rock crushes Lizard!!! You win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'paper' :
                print('Paper covers Rock! You Lose!!')
                self.player_two.current_score += 1
            elif self.player_two.chosen_gesture == 'spock' :
                print ("Ouch, Spock vaporizes Rock! You Lose!!")
                self.player_two.current_score += 1            
        #^ Player one Chooses Scissors
        if self.player_one.chosen_gesture == 'scissors' :
            if self.player_two.chosen_gesture == 'scissors' :
                print("It's a TIE!!")
            elif self.player_two.chosen_gesture == 'paper' :
                print("Scissors cuts Paper!!! You win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'lizard' :
                print("Sicissors decapitates Lizard!! Man That's BRUTAL!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'spock' :
                print("Ouch, Spock smashes Scissors!! You Lose!!!")
                self.player_two.current_score += 1
            elif self.player_two.chosen_gesture == 'rock' :
                print('That sucks, Rock crushes Scissors!! You Lose!!')
                self.player_two.current_score += 1
        #^ Player one Chooses Paper
        if self.player_one.chosen_gesture == 'paper' :
            if self.player_two.chosen_gesture == 'paper' :
                print("It's a TIE!!!")
            elif self.player_two.chosen_gesture == 'rock' :
                print("Yippie!! Paper covers Rock!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'spock' :
                print("Boyah!! Paper disapproves Spock!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'scissors' :
                print('Aww man, Scissors cuts Paper!! You Lose!!!')
                self.player_two.current_score += 1
            elif self.player_two.chosen_gesture == 'lizard' :
                print('Lizard eats Paper, NOM NOM!! You lose!!')
                self.player_two.current_score += 1
        #^ Player one Chooses Lizard
        if self.player_one.chosen_gesture == 'lizard' :
            if self.player_two.chosen_gesture == 'lizard' :
                print("It's a TIE!!!")
            elif self.player_two.chosen_gesture == 'spock' :
                print("Yippie!! Lizard poisons Spock!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'paper' :
                print("Boyah!! Lizard eats Paper!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'scissors' :
                print('Aww man, Scissors decapitates Lizard!! You Lose!!!')
                self.player_two.current_score += 1
            elif self.player_two.chosen_gesture == 'rock' :
                print('Watch Out!! Rock crushes Lizard!! You lose!!')
                self.player_two.current_score += 1
        #^ Player one Chooses Spock
        if self.player_one.chosen_gesture == 'spock' :
            if self.player_two.chosen_gesture == 'spock' :
                print("It's a TIE!!!")
            elif self.player_two.chosen_gesture == 'rock' :
                print("Yippie!! Spock vaporizes Rock!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'scissors' :
                print("Boyah!! Spock smashes Scissors!! You Win!!")
                self.player_one.current_score += 1
            elif self.player_two.chosen_gesture == 'paper' :
                print('Aww man, Paper disapproves Spock!! You Lose!!!')
                self.player_two.current_score += 1
            elif self.player_two.chosen_gesture == 'lizard' :
                print('Lizard poisons Spock!! You lose!!')
                self.player_two.current_score += 1
    def display_winner(self):
        if self.player_one == 2 :
            print(f'Congratulations {self.player_one} wins the game!!')
        elif self.player_two == 2 :
            print(f' Aww man, {self.player_two} wins the game!!')