from Game.Game import Game


class DummyTM:
    def __init__(self):
        self.calls = 0

    def play_turn(self, player, opponent, shop):
        opponent.hp = 0  # force win


class DummyPlayer:
    def __init__(self):
        self.hp = 10


def test_game_player_one_wins(monkeypatch):
    p1 = DummyPlayer()
    p2 = DummyPlayer()

    game = Game(p1, p2)
    game.TurnManager = DummyTM()

    result = game.play_Game()

    assert result == 1