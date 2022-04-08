class Player:
    def __init__(self, name, current_score):
        self.name = name
    # As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc)
        self.possible_gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ''
        self.current_score = current_score


    def choose_gesture(self):
        pass

