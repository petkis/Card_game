from Player import Player

class TurnManager:
    def __init__(self):
        pass

    def playTurn(self, player: Player, opponent: Player):
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
                card = player.hand.pop(index)
                card.play(player, opponent)
