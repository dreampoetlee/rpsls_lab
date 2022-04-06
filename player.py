class Player:
    def __init__(self):
        self.name = ""
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = []
        self.player_one = None
        self.player_two = None
    
    def chosen_gestures(self):
        print("Type O for Rock")
