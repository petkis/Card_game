class Character:
    def __init__(self, description, abilities, cost):
        self.description = description
        self.abilities = abilities
        self.cost = cost

    def apply(self, player, opponent):
        for ability in self.abilities:
            ability(player, opponent)

    def __str__(self):
        return(self.description)