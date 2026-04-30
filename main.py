from Game.Game import Game
from Player.Player import Player

def main():

    player_one = Player("Player 1")
    player_two = Player("Player 2",)

    game = Game(player_one, player_two)
    winner = game.play_Game()

    print(f"Winner: Player {winner}")


if __name__ == "__main__":
    main()