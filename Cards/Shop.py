from Cards.Starter import start_shop
from Cards.Type import CardType
from Cards.Cards import Card
from Player.Player import Player

import random

class Shop:
    def __init__(self):
        self.item_shop_deck, self.character_shop_deck = start_shop()
        random.shuffle(self.item_shop_deck)
        random.shuffle(self.character_shop_deck)

        self.shown_items: list[Card] = []
        self.shown_characters: list[Card] = []

        for _ in range(3):
            self.shown_items.append(self.item_shop_deck.pop())
            self.shown_characters.append(self.character_shop_deck.pop())

        self.discarded_items: list[Card] = []
        self.discarded_characters: list[Card] = []

    def __str__(self):
        shop_str = "Available items:\n"
        i = 0
        for item in self.shown_items:
            shop_str += str(i) + " " + str(item.name) + " " + str(item.content) + " costs: " + str(item.content.cost) + " gold\n"
            i += 1
        shop_str += "\nAvailable characters:\n"
        for character in self.shown_characters:
            shop_str += str(i) + " " + str(character.name) + " " + str(character.content) + " costs: " + str(character.content.cost) + " gold\n"
            i += 1
        return shop_str
    
    def buy(self, index, player: Player):
        shop = self.shown_items + self.shown_characters

        if index >= len(shop):
            raise IndexError('index out of shop range')
        
        if index < len(self.shown_items):
            shop = self.shown_items
            deck = self.item_shop_deck
            discards = self.discarded_items
            local_index = index
        else:
            shop = self.shown_characters
            deck = self.character_shop_deck
            discards = self.discarded_characters
            local_index = index - len(self.shown_items)

        bought_card = shop[local_index]

        if player.gold < bought_card.content.cost:
            print("Not enough gold")
            return None
        
        bought_card = shop.pop(local_index)

        if len(deck) == 0:
            random.shuffle(discards)
            deck.extend(discards)
            discards.clear()
        
        if len(deck) > 0:
            shop.append(deck.pop())
        
        return bought_card