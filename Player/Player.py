from Cards import Deck

class Player:
    def __init__(self, name: str, starter_item_deck: Deck, starter_character_deck: Deck):
        self.name = name
        self.item_deck = starter_item_deck
        self.character_deck = starter_character_deck
        self.hand = []
        self.hp = 30
