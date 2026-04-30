from Player.Player import Player
from Cards.Type import CardType
from Cards.Cards import Deck


def make_player():
    return Player("P1")


def test_player_starts_with_default_values():
    p = make_player()

    assert p.name == "P1"
    assert p.hp == 30
    assert p.gold == 0
    assert p.hand == []


def test_take_damage():
    p = make_player()

    p.take_damage(5)

    assert p.hp == 25


def test_heal():
    p = make_player()

    p.heal(5)

    assert p.hp == 35


def test_gain_gold():
    p = make_player()

    p.gain_gold(10)

    assert p.gold == 10


def test_draw_items_adds_cards_to_hand():
    p = make_player()
    p.item_deck = Deck(["item1", "item2"], CardType.Item)

    p.draw_items(1)

    assert len(p.hand) == 1
    assert p.hand[0] == "item2"
    assert len(p.item_deck.cards) == 1


def test_draw_characters_adds_cards_to_hand():
    p = make_player()
    p.characters_deck = Deck(["char1", "char2"], CardType.Character)

    p.draw_characters(1)

    assert len(p.hand) == 1
    assert p.hand[0] == "char2"
    assert len(p.characters_deck.cards) == 1


def test_draw_items_reshuffles_discard_when_deck_empty():
    p = make_player()
    p.item_deck = Deck([], CardType.Item)
    p.item_discard_pile = Deck(["discarded_item"], CardType.Item)

    p.draw_items(1)

    assert len(p.hand) == 1
    assert p.hand[0] == "discarded_item"
    assert p.item_discard_pile.cards == []


def test_draw_characters_reshuffles_discard_when_deck_empty():
    p = make_player()
    p.characters_deck = Deck([], CardType.Character)
    p.characters_discard_pile = Deck(["discarded_character"], CardType.Character)

    p.draw_characters(1)

    assert len(p.hand) == 1
    assert p.hand[0] == "discarded_character"
    assert p.characters_discard_pile.cards == []