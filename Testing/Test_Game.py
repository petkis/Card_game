from Game.Game import Game


class DummyTurnManager:
    def play_turn(self, player, opponent):
        opponent.hp = 0


class DummyPlayer:
    def __init__(self, hp=10):
        self.hp = hp


def test_game_player_one_wins():
    p1 = DummyPlayer()
    p2 = DummyPlayer()

    game = Game(p1, p2)
    game.TurnManager = DummyTurnManager()

    result = game.play_Game()

    assert result == 1


def test_game_player_two_wins():
    class PlayerTwoWinsTurnManager:
        def __init__(self):
            self.calls = 0

        def play_turn(self, player, opponent):
            self.calls += 1

            if self.calls == 1:
                # Player 1 attacks but does not win
                pass
            else:
                # Player 2 attacks and wins
                opponent.hp = 0

    p1 = DummyPlayer()
    p2 = DummyPlayer()

    game = Game(p1, p2)
    game.TurnManager = PlayerTwoWinsTurnManager()

    result = game.play_Game()

    assert result == 2