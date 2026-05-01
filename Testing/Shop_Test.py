import pytest

from Cards.Shop import Shop
from Cards.Type import CardType


class FakeContent:
    def __init__(self, cost):
        self.cost = cost

    def __str__(self):
        return ""


class FakeCard:
    def __init__(self, name, cost, type):
        self.name = name
        self.content = FakeContent(cost)
        self.type = type

    def __str__(self):
        return self.name


class FakePlayer:
    def __init__(self, gold):
        self.gold = gold


def make_shop():
    return Shop()


def test_shop_starts_with_default_values():
    s = make_shop()

    assert len(s.shown_items) == 3
    assert len(s.shown_characters) == 3
    assert s.discarded_items == []
    assert s.discarded_characters == []


def test_buy_item_returns_selected_item():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.item_shop_deck = [
        FakeCard("Sword", 3, CardType.Item),
        FakeCard("Shield", 5, CardType.Item),
    ]
    s.shown_items = [
        FakeCard("Potion", 1, CardType.Item),
    ]
    s.shown_characters = []

    bought = s.buy(0, player)

    assert str(bought) == "Potion"


def test_buy_item_adds_new_item_to_shop():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.item_shop_deck = [
        FakeCard("Sword", 3, CardType.Item),
        FakeCard("Shield", 5, CardType.Item),
    ]
    s.shown_items = [
        FakeCard("Potion", 1, CardType.Item),
    ]
    s.shown_characters = []

    s.buy(0, player)

    assert len(s.shown_items) == 1
    assert str(s.shown_items[0]) == "Shield"
    assert len(s.item_shop_deck) == 1
    assert str(s.item_shop_deck[0]) == "Sword"

def test_buy_character_returns_selected_character():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.character_shop_deck = [
        FakeCard("Warrior", 2, CardType.Character),
        FakeCard("Mage", 4, CardType.Character),
    ]
    s.shown_items = []
    s.shown_characters = [
        FakeCard("Rogue", 6, CardType.Character),
    ]

    bought = s.buy(0, player)

    assert str(bought) == "Rogue"


def test_buy_character_adds_new_character_to_shop():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.character_shop_deck = [
        FakeCard("Warrior", 2, CardType.Character),
        FakeCard("Mage", 4, CardType.Character),
    ]
    s.shown_items = []
    s.shown_characters = [
        FakeCard("Rogue", 6, CardType.Character),
    ]

    s.buy(0, player)

    assert len(s.shown_characters) == 1
    assert str(s.shown_characters[0]) == "Mage"
    assert len(s.character_shop_deck) == 1
    assert str(s.character_shop_deck[0]) == "Warrior"


def test_buy_item_with_second_index():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.item_shop_deck = [
        FakeCard("Sword", 3, CardType.Item),
        FakeCard("Shield", 5, CardType.Item),
    ]
    s.shown_items = [
        FakeCard("Potion", 1, CardType.Item),
        FakeCard("Boots", 2, CardType.Item),
    ]
    s.shown_characters = []

    bought = s.buy(1, player)

    assert str(bought) == "Boots"
    assert len(s.shown_items) == 2
    assert str(s.shown_items[0]) == "Potion"
    assert str(s.shown_items[1]) == "Shield"


def test_buy_character_uses_index_after_items():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.item_shop_deck = [
        FakeCard("Shield", 5, CardType.Item),
    ]
    s.character_shop_deck = [
        FakeCard("Mage", 4, CardType.Character),
    ]

    s.shown_items = [
        FakeCard("Potion", 1, CardType.Item),
    ]
    s.shown_characters = [
        FakeCard("Rogue", 6, CardType.Character),
    ]

    bought = s.buy(1, player)

    assert str(bought) == "Rogue"
    assert len(s.shown_characters) == 1
    assert str(s.shown_characters[0]) == "Mage"


def test_buy_raises_error_when_index_does_not_exist():
    s = make_shop()
    player = FakePlayer(gold=10)

    s.shown_items = []
    s.shown_characters = []

    with pytest.raises(IndexError):
        s.buy(0, player)


def test_buy_returns_none_when_player_does_not_have_enough_gold():
    s = make_shop()
    player = FakePlayer(gold=0)

    s.item_shop_deck = [
        FakeCard("Sword", 3, CardType.Item),
    ]
    s.shown_items = [
        FakeCard("Potion", 1, CardType.Item),
    ]
    s.shown_characters = []

    bought = s.buy(0, player)

    assert bought is None
    assert len(s.shown_items) == 1
    assert str(s.shown_items[0]) == "Potion"


def test_str_shows_available_items():
    s = make_shop()
    s.shown_items = [
        FakeCard("Potion", 1, CardType.Item),
        FakeCard("Boots", 2, CardType.Item),
    ]
    s.shown_characters = []

    result = str(s)

    assert "Available items:" in result
    assert "Potion" in result
    assert "costs: 1 gold" in result
    assert "Boots" in result
    assert "costs: 2 gold" in result


def test_str_shows_available_characters():
    s = make_shop()
    s.shown_items = []
    s.shown_characters = [
        FakeCard("Warrior", 2, CardType.Character),
    ]

    result = str(s)

    assert "Available characters:" in result
    assert "Warrior" in result
    assert "costs: 2 gold" in result