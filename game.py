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
    def game_play(self):# As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
     def game_play(self):
        while self.player_one.current_score >= 2 or self.player_two.currennt_score >=2 :
           print('Help me')
    
            
            








            # if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            # print("its a tie")
            # elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors" or self.player_two.chosen_gesture == "Lizard":
            #         print("Player one wins")
            #         self.player_one.machine_wins += 1
            # elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Spock":
            #         print("Player one wins")
            #         self.player_one.machine_wins += 1
            # elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Lizard":
            #         print("Player one wins")
            #         self.player_one.machine_wins += 1
            # elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Spock":
            #         print("Player one wins")
            #         self.player_one.machine_wins += 1
            # elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Scissors":
            #         print("Player one wins")
            #         self.player_one.machine_wins += 1
            # else:
            #         self.player_two.man_wins += 1
            #         print("Player two wins")



            #  = input(f'You have chosen to play{self.player_one.chosen_gesture}, the computer has chosen {self.player_two.chosen_gesture} ')

           # self.player_one.choose_gesture()

# # GAME PLAY ABOVE******* Unsure what to write. finished compare and left your code above in game play. ****
#     def compare_chosen_gesture(self):
       
            

#     def display_winner(self):
#         if(self.player_one ==2):
#             print(f'{self.player_one} wins the game!')
        
#         elif(self.player_two == 2):
#             print(f'{self.player_two} wins the game!')