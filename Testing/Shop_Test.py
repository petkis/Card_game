from Cards.Shop import Shop
from Cards.Type import CardType


class FakeContent:
    def __init__(self, cost):
        self.cost = cost


class FakeCard:
    def __init__(self, name, cost):
        self.name = name
        self.content = FakeContent(cost)

    def __str__(self):
        return self.name


def make_shop():
    return Shop()


def test_shop_starts_with_default_values():
    s = make_shop()

    assert s.shown_items == []
    assert s.shown_characters == []
    assert s.discarded_items == []

    # This matches the current typo in the Shop class.
    assert s.discarded_characer == []


def test_buy_item_returns_selected_item():
    s = make_shop()
    s.item_shop_deck = [
        FakeCard("Sword", 3),
        FakeCard("Shield", 5),
    ]
    s.shown_items = [
        FakeCard("Potion", 1),
    ]

    bought = s.buy(0, CardType.Item)

    assert str(bought) == "Potion"


def test_buy_item_adds_new_item_to_shop():
    s = make_shop()
    s.item_shop_deck = [
        FakeCard("Sword", 3),
        FakeCard("Shield", 5),
    ]
    s.shown_items = [
        FakeCard("Potion", 1),
    ]

    s.buy(0, CardType.Item)

    assert len(s.shown_items) == 1
    assert str(s.shown_items[0]) == "Shield"
    assert len(s.item_shop_deck) == 1
    assert str(s.item_shop_deck[0]) == "Sword"


def test_buy_character_returns_selected_character():
    s = make_shop()
    s.character_shop_deck = [
        FakeCard("Warrior", 2),
        FakeCard("Mage", 4),
    ]
    s.shown_characters = [
        FakeCard("Rogue", 6),
    ]

    bought = s.buy(0, CardType.Character)

    assert str(bought) == "Rogue"


def test_buy_character_adds_new_character_to_shop():
    s = make_shop()
    s.character_shop_deck = [
        FakeCard("Warrior", 2),
        FakeCard("Mage", 4),
    ]
    s.shown_characters = [
        FakeCard("Rogue", 6),
    ]

    s.buy(0, CardType.Character)

    assert len(s.shown_characters) == 1
    assert str(s.shown_characters[0]) == "Mage"
    assert len(s.character_shop_deck) == 1
    assert str(s.character_shop_deck[0]) == "Warrior"


def test_buy_item_with_second_index():
    s = make_shop()
    s.item_shop_deck = [
        FakeCard("Sword", 3),
        FakeCard("Shield", 5),
    ]
    s.shown_items = [
        FakeCard("Potion", 1),
        FakeCard("Boots", 2),
    ]

    bought = s.buy(1, CardType.Item)

    assert str(bought) == "Boots"
    assert len(s.shown_items) == 2
    assert str(s.shown_items[0]) == "Potion"
    assert str(s.shown_items[1]) == "Shield"


def test_buy_item_raises_error_when_index_does_not_exist():
    s = make_shop()
    s.item_shop_deck = [
        FakeCard("Sword", 3),
    ]
    s.shown_items = []

    try:
        s.buy(0, CardType.Item)
        assert False
    except IndexError:
        assert True


def test_str_shows_available_items():
    s = make_shop()
    s.shown_items = [
        FakeCard("Potion", 1),
        FakeCard("Boots", 2),
    ]

    result = str(s)

    assert "Available items:" in result
    assert "Potion 1" in result
    assert "Boots 2" in result


def test_str_has_available_characters_section():
    s = make_shop()

    result = str(s)

    assert "Available characters:" in result


def test_str_does_not_currently_show_characters_due_to_bug():
    s = make_shop()
    s.shown_items = []
    s.shown_characters = [
        FakeCard("Warrior", 2),
    ]

    result = str(s)

    assert "Warrior 2" not in result