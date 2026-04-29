from enum import Enum, auto

class CardType(Enum):
    Item = 0
    Character = 1

class OptionType(Enum):
    Damage = auto()
    Draw = auto()
    Money = auto()
    Heal = auto()