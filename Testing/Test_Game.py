from Game.Game import Game


class DummyPlayer:
    def __init__(self, hp=10):
        self.hp = hp


class PlayerOneWinsTurnManager:
    def play_turn(self, player, opponent, shop):
        opponent.hp = 0


class PlayerTwoWinsTurnManager:
    def __init__(self):
        self.calls = 0

    def play_turn(self, player, opponent, shop):
        self.calls += 1

        if self.calls == 2:
            opponent.hp = 0


def test_game_player_one_wins():
    p1 = DummyPlayer()
    p2 = DummyPlayer()

    game = Game(p1, p2)
    game.TurnManager = PlayerOneWinsTurnManager()

    result = game.play_Game()

    assert result == 1


def test_game_player_two_wins():
    p1 = DummyPlayer()
    p2 = DummyPlayer()

    game = Game(p1, p2)
    game.TurnManager = PlayerTwoWinsTurnManager()

    result = game.play_Game()

    assert result == 2