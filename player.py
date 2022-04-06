import random

class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"] 
        self.chosen_gesture = random.randrange(len(self.gestures))
        self.score = 0