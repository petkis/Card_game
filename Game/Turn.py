from Player.Player import Player
from Cards.Type import CardType
from Cards.Cards import Card

class TurnManager:
    def __init__(self):
        pass

    def play_turn(self, player: Player, opponent: Player):
        player.draw_items(5)
        player.draw_characters(1)

        while len(player.hand) > 0:
            print("Player's hand:")
            for i, item in enumerate(player.hand):
                print(f"{i}: {item}")
            print("Select a card to play:")
            index = int(input())
            if index < 0 or index >= len(player.hand):
                print("Invalid input, try number between 0 and", len(player.hand) - 1)
                continue
            else:
                card: Card = player.hand.pop(index)
                card.play(player, opponent)
                if card.type == CardType.Item:
                    player.item_discard_pile.cards.append(card)
                else:
                    player.characters_discard_pile.cards.append(card)
