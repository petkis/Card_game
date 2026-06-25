from Player.Player import Player
from Cards.Type import CardType
from Cards.Cards import Card
from Cards.Shop import Shop

class TurnManager:
    def __init__(self):
        pass
    
    def shopping(self, player: Player, shop: Shop):
        print("Entering shop:")
        exit = (len(shop.shown_characters) + len(shop.shown_items))

        while True:
            print("Available gold: " + str(player.gold))
            print(shop)
            print(exit, "for Exit")
            print("Select a card to buy:")
            index = int(input())
            if index == exit:
                return
            if index < exit:
                card = shop.buy(index, player)
                if card is None:
                    continue
                player.bought(card, card.type)
            else:
                print("Wrong input")


    def play_turn(self, player: Player, opponent: Player, shop: Shop):
        player.draw_items(5)
        player.draw_characters(1)

        while len(player.hand) > 0:
            print(player,"turn")
            i = 0
            for card in player.hand:
                print(f"{i}: {card}")
                i += 1
            print(f"{i}: shop")
            print(f"{i+1}: END TURN")
            print("Select a card to play:")
            index = input()
            try:
                index = int(index)
            except:
                print("Invalid Input!")
                continue
            if index < 0 or index > len(player.hand) + 1:
                print("Invalid input, try number between 0 and", (len(player.hand) + 1))
                continue
            elif index == len(player.hand):
                self.shopping(player, shop)
            elif index == (len(player.hand) + 1):
                player.end_turn()
                print("ENDING TURN")
                return
            else:
                card: Card = player.hand.pop(index)
                card.play(player, opponent)
                player.played.append(card)
                if card.type == CardType.Item:
                    player.item_discard_pile.cards.append(card)
                else:
                    player.characters_discard_pile.cards.append(card)
        
        print("0 Enter shop")
        print("Otherwise END TURN")
        index = input()
        try:
            index = int(index)
        except:
            print("ENDING TURN")
            player.end_turn()
            return
        if index == 0:
            self.shopping(player, shop)

