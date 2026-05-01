from Cards.Cards import Deck, Card
from Cards.Type import CardType
from Cards.Starter import starter_item_deck, starter_character_deck

class Player:
    def __init__(self, name: str):
        self.name = name

        self.item_deck = starter_item_deck()
        self.characters_deck = starter_character_deck()

        self.item_discard_pile = Deck([], CardType.Item)
        self.characters_discard_pile = Deck([], CardType.Character)

        self.hand: list[Card] = []
        self.hp = 30
        self.gold = 0

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

    def bought(self, card: Card, type: CardType):
        self.gold -= card.content.cost
        discard = self.item_discard_pile
        if type == CardType.Character:
            discard = self.characters_discard_pile
        discard.cards.append(card)

    def take_damage(self, amount: int):
        self.hp -= amount

    def heal(self, amount: int):
        self.hp += amount

    def gain_gold(self, amount: int):
        self.gold += amount

    def __str__(self):
        return self.name + " hp: " + str(self.hp) + " gold: " + str(self.gold)