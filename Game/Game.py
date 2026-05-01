from Player.Player import Player
from Game.Turn import TurnManager
from Cards.Shop import Shop

class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.TurnManager = TurnManager()
        self.player_one = player_one
        self.player_two = player_two
        self.shop = Shop()

    def play_Game(self) -> int:
        while True:
            self.TurnManager.play_turn(self.player_one, self.player_two)
            if self.player_two.hp <= 0:
                print("Player two lost.")
                return 1
            self.TurnManager.play_turn(self.player_two, self.player_one)
            if self.player_one.hp <= 0:
                print("Player one lost.")
                return 2
