from player import Player

class Human(Player):
  def __init__(self, name):
      super().__init__(name)

  def choose_gesture(self):
    self.chosen_gesture = input("What gesture would you like to play for this round? ")
  
  def man_vs_machine(self):
    self.man_wins += 1