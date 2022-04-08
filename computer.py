from player import Player
import random

class Computer(Player):
  def __init__(self, name, current_score):
      super().__init__(name, current_score)
    
  def choose_gesture(self):
    self.chosen_gesture = random.randrange(len(self.possible_gestures))
  
  def round_won(self):
    self.current_score += 1