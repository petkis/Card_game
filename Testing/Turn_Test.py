from unittest.mock import patch

from Game.Turn import TurnManager
from Cards.Type import CardType
from Cards.Cards import Deck


class DummyCard:
    def __init__(self, card_type=CardType.Item):
        self.type = card_type
        self.played = False

    def play(self, player, opponent):
        self.played = True


class DummyPlayer:
    def __init__(self, card_type=CardType.Item):
        self.hand = [DummyCard(card_type)]
        self.item_discard_pile = Deck([], CardType.Item)
        self.characters_discard_pile = Deck([], CardType.Character)

    def draw_items(self, amount):
        pass

    def draw_characters(self, amount):
        pass


@patch("builtins.input", side_effect=["0"])
def test_play_turn_plays_item_card(mock_input):
    tm = TurnManager()
    p1 = DummyPlayer(CardType.Item)
    p2 = DummyPlayer()

    card = p1.hand[0]

    tm.play_turn(p1, p2)

    assert card.played is True
    assert len(p1.hand) == 0
    assert len(p1.item_discard_pile.cards) == 1
    assert p1.item_discard_pile.cards[0] is card


@patch("builtins.input", side_effect=["0"])
def test_play_turn_plays_character_card(mock_input):
    tm = TurnManager()
    p1 = DummyPlayer(CardType.Character)
    p2 = DummyPlayer()

    card = p1.hand[0]

    tm.play_turn(p1, p2)

    assert card.played is True
    assert len(p1.hand) == 0
    assert len(p1.characters_discard_pile.cards) == 1
    assert p1.characters_discard_pile.cards[0] is card