from Type import CardType
from dataclasses import dataclass

@dataclass
class Deck:
    cards: list["Card"]
    type: CardType

class Card:
    def __init__(self, name: str, type: CardType, content):
        self.name = name
        self.type = type
        self.content = content

    def __str__(self):
        return f"{self.name} ({self.card_type.name})"

    def play(self, player, opponent):
        self.content.apply(player, opponent)
