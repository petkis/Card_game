from Player.Player import Player
from Cards.Type import CardType
from Cards.Cards import Deck

def make_player():
    return Player(
        "P1",
        Deck([], CardType.Item),
        Deck([], CardType.Character),
    )


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