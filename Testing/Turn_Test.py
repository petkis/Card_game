from Game.Turn import TurnManager
from Cards.Type import CardType
from Cards.Cards import Deck
from unittest.mock import patch


class DummyCard:
    def __init__(self):
        self.type = CardType.Item
        self.played = False

    def play(self, p, o):
        self.played = True


class DummyPlayer:
    def __init__(self):
        self.hand = [DummyCard()]
        self.item_discard_pile = Deck([], CardType.Item)
        self.characters_discard_pile = Deck([], CardType.Character)

    def draw_items(self, x): pass
    def draw_characters(self, x): pass


@patch("builtins.input", side_effect=["0"])
def test_play_turn(mock_input):
    tm = TurnManager()
    p1 = DummyPlayer()
    p2 = DummyPlayer()

    tm.play_turn(p1, p2)

    assert len(p1.hand) == 0
    assert len(p1.item_discard_pile.cards) == 1