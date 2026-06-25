from Cards.Type import Guild

class Character:
    def __init__(self, description: str, abilities, cost: int, guild = None):
        self.description = description
        self.abilities = abilities
        self.cost = cost
        self.guild: Guild | None = guild

    def apply(self, player, opponent):
        for ability in self.abilities:
            ability.use_ability(player, opponent)

    def __str__(self):
        addon = ""
        if self.guild:
            addon += " Guild: " + self.guild.name
        return(self.description + addon)