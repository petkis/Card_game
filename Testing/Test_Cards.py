from Cards.Cards import Deck, Card
from Cards.Type import CardType


class DummyContent:
    def __init__(self):
        self.called = False

    def apply(self, player, opponent):
        self.called = True


def test_deck_length_empty():
    deck = Deck([], CardType.Item)

    assert len(deck) == 0


def test_deck_length_with_cards():
    deck = Deck(["card1", "card2"], CardType.Item)

    assert len(deck) == 2


def test_card_str():
    card = Card("Fireball", CardType.Item, DummyContent())

    assert str(card) == "Fireball (Item)"


def test_card_play_calls_apply():
    content = DummyContent()
    card = Card("Test", CardType.Item, content)

    card.play(None, None)

    assert content.called is True