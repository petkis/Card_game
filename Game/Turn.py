from Player import Player

class TurnManager:
    def __init__(self):
        pass

    def playTurn(self, player: Player, opponent: Player):
        player.draw_items(5)
        player.draw_characters(1)

        