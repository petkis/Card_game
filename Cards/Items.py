from Cards.Type import OptionType, Guild

class Item:
    def __init__(self, description: str, cost: int, option: OptionType, amount: int, guild = None):
        self.description = description
        self.cost = cost
        self.option = option
        self.amount = amount
        self.guild: Guild | None = guild

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
        addon = ""
        if self.guild:
            addon += " Guild: " + self.guild.name
        return(self.description)