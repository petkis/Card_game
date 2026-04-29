from enum import Enum

class CardType(Enum):
    Item = 0
    Character = 1

class OptionType(Enum):
    Damage = 0
    Draw = 1
    Money = 2
    Heal = 3