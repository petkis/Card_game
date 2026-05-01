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
                description="Soldier: Deal 3 damage",
                abilities=[
                    lambda player, opponent: opponent.take_damage(3)
                ]
            )
        ),
    ]

    return Deck(cards, CardType.Character)

def start_shop() -> tuple[list[Card], list[Card]]:
    return ([], [])