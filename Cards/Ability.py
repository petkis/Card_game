class Ability:
    def __init__(self, condition, ability):
        self.condition = condition
        self.ability = ability

    def __str__(self):
        return self.ability

    #def use_ability(self):
    #    if self.condition:
    #        return self.ability
