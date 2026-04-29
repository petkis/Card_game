from Cards.Type import CardType
from dataclasses import dataclass
from typing import Union
from Cards.Items import Item
from Cards.Characters import Character

@dataclass
class Deck:
    cards: list["Card"]
    type: CardType

    def shuffle(self):
        import random
        random.shuffle(self.cards)
        return self
    
    def __len__(self):
        return len(self.cards)

class Card:
    def __init__(self, name: str, type: CardType, content: Union[Item, Character]):
        self.name = name
        self.type = type
        self.content = content

    def __str__(self):
        return f"{self.name} ({self.type.name})"

    def play(self, player, opponent):
        self.content.apply(player, opponent)
