class Player:
    def __init__(self, name):
        self.name = name
        self.possible_gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ''
        self.score = 0
    
    def choose_gesture(self):
        pass
