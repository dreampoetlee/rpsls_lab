# Current algorithm for how to run and play the game

 #! Classes needed 
    #todo Parent class
      #? Player
        #^ has a: 
          # -name
          # -list of possible gestures
          # -chosen_gesture
          # -score
      #& Child classes
          # computer
          # human
        #^ Can do
          # choose gestures
    #todo Regular Classes
      #? Game
        #^ has a
          # player_one
          # player_two
        #^ Game Phases
          #! Intro Phase
            # -welcome message
            # -display rules
            # -find out how many players & create player two
          #! Main game phase
            # -player_one chooses gesture
            # -player_two chooses gesture
            # -compares gestures, find winner
            # -repeat until somone has 2 pts
          #! Endgame
            # -display winner


#~ need classes
  #* 1) paper
  #* 2) scissors
  #* 3) rock
  #* 4) lizard
  #* 5) spock 

# !Display the rules of the game
  #todo Rock crushes Scissors 
  #todo Scissors cuts Paper 
  #todo Paper covers Rock 
  #todo Rock crushes Lizard 
  #todo Lizard poisons Spock
  #todo Spock smashes Scissors 
  #todo Scissors decapitates Lizard 
  #todo Lizard eats Paper 
  #todo Paper disproves Spock 
  #todo Spock vaporizes Rock

# As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.

  #? types of players: 
    #? 2 humans: need classes ---> human_one & human_two
    #? 1 AI : class name ----> the_machine
  
  #? where should the players methods be called?
    #? main.py file

# As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).
  #& Store gestures & options in a list
  #& should use the random()

# As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
  #^ need a while loop to run up 3 times and to pick the winner from those three runs

# As a player, I want the correct player to win a given round based on the choices* made by each player.

# As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.

# ^ Logic thoughts from Tarsha
  # 1 MAIN-  import Game. game_run
  # 2 AI/PC- pc where  will be importing random options.
  # 3 Human file-can choose their option to play game
  # 4 Game file-Runs entire game. import AI, import human, import options, import rules. display welcome, random choice options for player.

 


    



    # renamed the following files: lizard to player...paper to AI....rock to human...scissors to game...deleted spock ile
