from Cards.Starter import starter_item_deck, starter_character_deck
from Cards.Type import CardType, OptionType


def test_starter_item_deck_has_8_cards():
    deck = starter_item_deck()

    assert len(deck.cards) == 8
    assert deck.type == CardType.Item


def test_starter_item_deck_has_6_gold_items():
    deck = starter_item_deck()

    gold_items = [
        card for card in deck.cards
        if card.content.option == OptionType.Money
    ]

    assert len(gold_items) == 6


def test_starter_item_deck_has_2_damage_items():
    deck = starter_item_deck()

    damage_items = [
        card for card in deck.cards
        if card.content.option == OptionType.Damage
    ]

    assert len(damage_items) == 2


def test_starter_item_deck_gold_items_gain_1_gold():
    deck = starter_item_deck()

    gold_items = [
        card for card in deck.cards
        if card.content.option == OptionType.Money
    ]

    for card in gold_items:
        assert card.name == "Gold"
        assert card.type == CardType.Item
        assert card.content.amount == 1
        assert card.content.cost == 0


def test_starter_item_deck_damage_items_deal_1_damage():
    deck = starter_item_deck()

    damage_items = [
        card for card in deck.cards
        if card.content.option == OptionType.Damage
    ]

    for card in damage_items:
        assert card.name == "Strike"
        assert card.type == CardType.Item
        assert card.content.amount == 1
        assert card.content.cost == 0


def test_starter_character_deck_has_3_cards():
    deck = starter_character_deck()

    assert len(deck.cards) == 3
    assert deck.type == CardType.Character


def test_starter_character_deck_has_correct_names():
    deck = starter_character_deck()

    names = [
        card.name for card in deck.cards
    ]

    assert "Merchant" in names
    assert "Banker" in names
    assert "Soldier" in names


def test_starter_characters_include_two_money_and_one_damage():
    deck = starter_character_deck()

    class DummyPlayer:
        def __init__(self):
            self.gold = 0
            self.hp = 10

        def gain_gold(self, amount):
            self.gold += amount

        def take_damage(self, amount):
            self.hp -= amount

    money_characters = 0
    damage_characters = 0

    for card in deck.cards:
        player = DummyPlayer()
        opponent = DummyPlayer()

        card.content.apply(player, opponent)

        if player.gold > 0:
            money_characters += 1

        if opponent.hp < 10:
            damage_characters += 1

    assert money_characters == 2
    assert damage_characters == 1