from Cards.Cards import Deck, Card
from Cards.Type import CardType, OptionType
from Cards.Items import Item
from Cards.Characters import Character

def starter_item_deck():
    cards = [
        # 6 gold items
        Card(
            "Gold",
            CardType.Item,
            Item("Gain 1 gold", cost=0, option=OptionType.Money, amount=1)
        ),
        Card(
            "Gold",
            CardType.Item,
            Item("Gain 1 gold", cost=0, option=OptionType.Money, amount=1)
        ),
        Card(
            "Gold",
            CardType.Item,
            Item("Gain 1 gold", cost=0, option=OptionType.Money, amount=1)
        ),
        Card(
            "Gold",
            CardType.Item,
            Item("Gain 1 gold", cost=0, option=OptionType.Money, amount=1)
        ),
        Card(
            "Gold",
            CardType.Item,
            Item("Gain 1 gold", cost=0, option=OptionType.Money, amount=1)
        ),
        Card(
            "Gold",
            CardType.Item,
            Item("Gain 1 gold", cost=0, option=OptionType.Money, amount=1)
        ),

        # 2 damage items
        Card(
            "Strike",
            CardType.Item,
            Item("Deal 1 damage", cost=0, option=OptionType.Damage, amount=1)
        ),
        Card(
            "Strike",
            CardType.Item,
            Item("Deal 1 damage", cost=0, option=OptionType.Damage, amount=1)
        ),
    ]

    return Deck(cards, CardType.Item)


def starter_character_deck():
    cards = [
        Card(
            "Merchant",
            CardType.Character,
            Character(
                cost=0,
                description="Merchant: Gain 2 gold",
                abilities=[
                    lambda player, opponent: player.gain_gold(2)
                ]
            )
        ),

        Card(
            "Banker",
            CardType.Character,
            Character(
                cost=0,
                description="Banker: Gain 3 gold",
                abilities=[
                    lambda player, opponent: player.gain_gold(3)
                ]
            )
        ),

        Card(
            "Soldier",
            CardType.Character,
            Character(
                cost=0,
                description="Soldier: Deal 3 damage",
                abilities=[
                    lambda player, opponent: opponent.take_damage(3)
                ]
            )
        ),
    ]

    return Deck(cards, CardType.Character)

def start_shop() -> tuple[list[Card], list[Card]]:
    item_shop_cards = [
        Card(
            "Big Gold",
            CardType.Item,
            Item("Gain 2 gold", cost=2, option=OptionType.Money, amount=2)
        ),
        Card(
            "Treasure Chest",
            CardType.Item,
            Item("Gain 3 gold", cost=3, option=OptionType.Money, amount=3)
        ),
        Card(
            "Dagger",
            CardType.Item,
            Item("Deal 2 damage", cost=2, option=OptionType.Damage, amount=2)
        ),
        Card(
            "Sword",
            CardType.Item,
            Item("Deal 3 damage", cost=4, option=OptionType.Damage, amount=3)
        ),
        Card(
            "Greatsword",
            CardType.Item,
            Item("Deal 5 damage", cost=6, option=OptionType.Damage, amount=5)
        ),
    ]

    character_shop_cards = [
        Card(
            "Noble",
            CardType.Character,
            Character(
                cost=4,
                description="Noble: Gain 4 gold",
                abilities=[
                    lambda player, opponent: player.gain_gold(4)
                ]
            )
        ),
        Card(
            "Knight",
            CardType.Character,
            Character(
                cost=4,
                description="Knight: Deal 4 damage",
                abilities=[
                    lambda player, opponent: opponent.take_damage(4)
                ]
            )
        ),
        Card(
            "Healer",
            CardType.Character,
            Character(
                cost=4,
                description="Healer: Heal 5 hp",
                abilities=[
                    lambda player, opponent: player.heal(5)
                ]
            )
        ),
        Card(
            "Assassin",
            CardType.Character,
            Character(
                cost=5,
                description="Assassin: Deal 6 damage",
                abilities=[
                    lambda player, opponent: opponent.take_damage(6)
                ]
            )
        ),
        Card(
            "Tax Collector",
            CardType.Character,
            Character(
                cost=1,
                description="Tax Collector: Gain 2 gold",
                abilities=[
                    lambda player, opponent: player.gain_gold(2)
                ]
            )
        ),
    ]

    return item_shop_cards, character_shop_cards