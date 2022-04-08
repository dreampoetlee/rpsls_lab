from player import Player
import random

class Computer(Player):
  def __init__(self, name):
      super().__init__(name)
    
  def choose_gesture(self):
    self.chosen_gesture = random.randrange(len(self.possible_gestures))
  
  def round_won(self):
    self.current_score += 1