
from Game import games
from Game2 import games2


class main:
    def main(self):
        game_type = input("Do you want to play against the computer (1) or against another player (2)? ")
        player_names = []

        if game_type == "1":
            diffculity1 = input("What diffculity level do you want(easy, medium or hard)")
            play_game = games2()
            play_game.game_play(diffculity1)
        elif game_type == "2":
            player1_name = input("Enter name for Player 1: ")
            player2_name = input("Enter name for Player 2: ")
            diffculity2 = input("What diffculity level do you want(easy, medium or hard)")
            player_names.append(player1_name)
            player_names.append(player2_name)
            my_game = games(player_names)
            my_game.play_game(diffculity2)
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main_instance = main()
    main_instance.main()
