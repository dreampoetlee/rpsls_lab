from player import Player

class Computer(Player):
  def __init__(self, name):
    #! player can choose a gesture, but is it inherited from the parent class or does it have to be placed here
      super().__init__(name)