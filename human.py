from player import Player

class Human(Player):
  def __init__(self, name):
      super().__init__(name)

  def choose_gesture(self):
    self.chosen_gesture = input("What gesture would you like to play for this round? ")
  
  def round_won(self):
    self.current_score += 1