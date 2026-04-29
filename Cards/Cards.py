from Type import CardType, OptionType

class Deck:
    def __init__(self, cards: list[Card], type: CardType):
        self.cards = cards
        self.type = type

class Card:
    def __init__(self, name: str, type: CardType, option: OptionType, amount: int):
        self.name = name
        self.type = type
        self.amount = amount
        self.option = option

    def play(self, player, opponent):
        if self.option == OptionType.Damage:
            opponent.take_damage(self.amount)
        elif self.option == OptionType.Draw:
            player.draw_card(self.amount)
        elif self.option == OptionType.Money:
            player.gain_gold(self.amount)
        elif self.option == OptionType.Heal:
            player.heal(self.amount)
