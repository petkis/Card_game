from Cards.Starter import start_shop
from Cards.Type import CardType
import random

class Shop:
    def __init__(self):
        self.item_shop_deck, self.character_shop_deck = start_shop()

        self.shown_items = []
        self.shown_characters = []

        self.discarded_items = []
        self.discarded_characer = []

    def __str__(self):
        shop_str = "Available items:\n"
        for item in self.shown_items:
            shop_str += str(item) + " " + str(item.content.cost) + " "
        shop_str += "\nAvailable characters:\n"
        for character in self.shown_items:
            shop_str += str(character) + " " + str(character.content.cost) + " "
        return shop_str
    
    def buy(self, index, type: CardType):
        deck = self.item_shop_deck
        shop = self.shown_items
        discards = self.discarded_items
        if type == CardType.Character:
            deck = self.character_shop_deck
            shop = self.shown_characters
            discards = self.discarded_characer
        if index >= len(shop):
            raise IndexError('index out of shop range')
        if len(deck) == 0:
            deck = random.shuffle(discards)
        shop.append(deck.pop())
        return shop.pop(index)