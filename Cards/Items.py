from Cards.Type import OptionType

class Item:
    def __init__(self, description, cost, option, amount):
        self.description = description
        self.cost = cost
        self.option = option
        self.amount = amount

    def apply(self, player, opponent):
        if self.option == OptionType.Damage:
            opponent.take_damage(self.amount)
        elif self.option == OptionType.Draw:
            player.draw_items(self.amount)
        elif self.option == OptionType.Money:
            player.gain_gold(self.amount)
        elif self.option == OptionType.Heal:
            player.heal(self.amount)

    def __str__(self):
        return(self.description)