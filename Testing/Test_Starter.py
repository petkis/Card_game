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
        if card.option == OptionType.Money
    ]

    assert len(gold_items) == 6


def test_starter_item_deck_has_2_damage_items():
    deck = starter_item_deck()

    damage_items = [
        card for card in deck.cards
        if card.option == OptionType.Damage
    ]

    assert len(damage_items) == 2


def test_starter_character_deck_has_3_cards():
    deck = starter_character_deck()

    assert len(deck.cards) == 3
    assert deck.type == CardType.Character


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

    for character in deck.cards:
        player = DummyPlayer()
        opponent = DummyPlayer()

        character.apply(player, opponent)

        if player.gold > 0:
            money_characters += 1

        if opponent.hp < 10:
            damage_characters += 1

    assert money_characters == 2
    assert damage_characters == 1