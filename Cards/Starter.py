from Cards.Cards import Deck, Card
from Cards.Type import CardType, OptionType, Guild
from Cards.Items import Item
from Cards.Characters import Character
from Cards.Ability import Ability
import Cards.Ability_Help.conditions as cond
import Cards.Ability_Help.effects as eff

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
                    Ability(condition = cond.always, 
                            ability = eff.gain_gold(2))
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
                    Ability(condition = cond.always, 
                            ability = eff.gain_gold(3))
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
                    Ability(condition = cond.always, 
                            ability = eff.deal_damage(3))
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
            Item("Gain 3 gold", cost=3, option=OptionType.Money, amount=3, guild=Guild.Adventurers)
        ),
        Card(
            "Dagger",
            CardType.Item,
            Item("Deal 2 damage", cost=2, option=OptionType.Damage, amount=2, guild=Guild.ThievesGuild)
        ),
        Card(
            "Guard's sword",
            CardType.Item,
            Item("Deal 3 damage", cost=4, option=OptionType.Damage, amount=3, guild=Guild.Soldiers)
        ),
        Card(
            "Greatsword",
            CardType.Item,
            Item("Deal 5 damage", cost=6, option=OptionType.Damage, amount=5, guild=Guild.Soldiers)
        ),
    ]

    character_shop_cards = [
        Card(
            "Noble",
            CardType.Character,
            Character(
                cost=4,
                description="Noble: If your health is above 15 gain 4 gold.\n Otherwise gain 2 gold.",
                abilities=[
                    Ability(condition = cond.health_over_X(15), 
                            ability = eff.gain_gold(4)),
                    Ability(condition = cond.health_under_X(16), 
                            ability = eff.gain_gold(2)),
                ],
                guild=Guild.Nobility
            )
        ),
        Card(
            "Knight",
            CardType.Character,
            Character(
                cost=4,
                description="Knight: Deal 4 damage",
                abilities=[
                    Ability(condition = cond.always,
                            ability = eff.deal_damage(4))
                ],
                guild=Guild.Soldiers
            )
        ),
        Card(
            "Priest",
            CardType.Character,
            Character(
                cost=4,
                description="Healer: Heal 5 hp",
                abilities=[
                    Ability(condition = cond.always,
                            ability = eff.heal(5))
                ],
                guild=Guild.Church
            )
        ),
        Card(
            "Assassin",
            CardType.Character,
            Character(
                cost=5,
                description="Assassin: If you have more health tahn your opponent deal 6 damage.\n Otherwise deal 3 damage.",
                abilities=[
                    Ability(condition = cond.opponent_less_healt(), 
                            ability = eff.deal_damage(6)),
                    Ability(condition = cond.opponent_NOT_less_healt(), 
                            ability = eff.deal_damage(3)),
                ],
                guild=Guild.ThievesGuild
            )
        ),
        Card(
            "Tax Collector",
            CardType.Character,
            Character(
                cost=1,
                description="Tax Collector: Gain 2 gold",
                abilities=[
                    Ability(condition = cond.always,
                            ability = eff.gain_gold(2))
                ],
                guild=Guild.TradeGuild
            )
        ),
    ]

    return item_shop_cards, character_shop_cards