from Cards.Cards import Deck
from Cards.Type import CardType

class Player:
    def __init__(self, name: str, starter_item_deck: Deck, starter_character_deck: Deck):
        self.name = name
        self.item_deck = starter_item_deck
        self.item_discard_pile: Deck = Deck(CardType.Item)
        self.characters_deck = starter_character_deck
        self.characters_discard_pile: Deck = Deck(CardType.Character)
        self.hand = []
        self.hp = 30

    def draw_items(self, amount: int):
        for _ in range(amount):
            if len(self.item_deck) == 0:
                self.item_deck = self.item_discard_pile.shuffle()
                self.item_discard_pile.cards = []
            card = self.item_deck.cards.pop()
            self.hand.append(card)

    def draw_characters(self, amount: int):
        for _ in range(amount):
            if len(self.characters_deck) == 0:
                self.characters_deck = self.characters_discard_pile.shuffle()
                self.characters_discard_pile.cards = []
            card = self.characters_deck.cards.pop()
            self.hand.append(card)
