class Player:
    def __init__(self, name, man_wins, machine_wins):
        self.name = name
    # As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc)
        self.possible_gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ''
        self.man_wins = man_wins
        self.machine_wins = machine_wins

    def choose_gesture(self):
        pass

    def man_vs_machine(self):
        pass

    def machine_vs_man(self):
        pass

