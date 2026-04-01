from Player import Player
from Turn import TurnManager

class Game:
    def __init__(self, player_one, player_two):
        self.TurnManager = TurnManager()
        self.player_one = player_one
        self.player_two = player_two

    def play_Game(self):
        while self.player_two.hp > 0 and self.player_one.hp > 0:
            self.TurnManager.play_turn(self.player_one)
            self.TurnManager.play_turn(self.player_two)
