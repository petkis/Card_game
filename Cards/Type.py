from enum import Enum, auto

class CardType(Enum):
    Item = 0
    Character = 1

class OptionType(Enum):
    Damage = auto()
    Draw = auto()
    Money = auto()
    Heal = auto()

class Guild(Enum):
    TradeGuild = auto()
    ThievesGuild = auto()
    Soldiers = auto()
    Peasants = auto()
    Church = auto()
