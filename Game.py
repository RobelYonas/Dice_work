
from dice_roll import Die
from player import Player
from scoretracker import scoreboard
import random


class games:
    game_plays = True

# A class variable indicating whether the game is being played or not

# Initializing the class
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.dice = Die()
        self.scoreboard = scoreboard(player_names=player_names)

    # A function to play the game
    def play_game(self, difficulty):
        # A cheat code that can be used to win the game
        cheat_code = "win"
        # Initializing the current player index to zero
        current_player_index = 0
        # Initializing the maximum round score to zero
        max_round_score = 0
        # A set containing the numbers which, if rolled, result in a score reset to zero
        forbidden_rolls = {1} 

        # Setting the threshold value based on the difficulty level chosen by the user
        if difficulty == "hard":
            threshold = 50
        elif difficulty == "medium":
            threshold = 40
        else:
            threshold = 30

        # A loop to play the game until someone wins
        while True:
            # Displaying the current scoreboard
            self.scoreboard.display_scoreboard()
            # Setting the current player
            current_player = self.players[current_player_index]
            print(f"{current_player.name}'s turn:")

            # A loop to roll the dice until the player decides to hold or rolls a 1
            while True:
                # Asking the player to roll the dice
                roll_input = input("Press enter to roll the dice (or q to quit): ")
                
                # If the player decides to quit
                if roll_input.lower() == 'q':
                    break

                # If the player enters the cheat code to win the game
                elif roll_input == cheat_code:
                    max_round_score += 100
                    print(f"Round score: {max_round_score}")
                    print(f"Congratulations, {current_player.name} wins with a score of {current_player.score}!")
                    return

                # If the player presses enter to roll the dice
                elif not roll_input.strip():
                    # Checking if the player rolled a 1
                    if threshold >= random.randint(1, 100):
                        roll = 1
                        print("Oops, you rolled a 1. Round score reset to 0.")
                        self.scoreboard.hold_score(0, current_player_index)
                        current_player_index = (current_player_index + 1) % len(self.players)
                    else:
                        roll = self.dice.roll()
                        print(f"You rolled a {roll}")

                        # Adding the roll to the maximum round score
                        max_round_score += roll
                        print(f"Round score: {max_round_score}")

                        # If the player wins the game
                        if max_round_score >= 100:
                            print(f"Congratulations, {current_player.name} wins with a score of {current_player.score}!")
                            return

                        # Asking the player if they want to roll again
                        answer = input("Do you want to roll again (y or n)?").lower()
                        if answer == 'n':
                            # Holding the score and updating the current player's score
                            self.scoreboard.hold_score(max_round_score, current_player_index)
                            current_player.score = self.scoreboard.scores[current_player.name]
                            # Display
                        self.scoreboard.display_scoreboard()

                        # Asking the player if they want to change their name
                        name_change_input = ""
                        while name_change_input.lower() not in ('y', 'n'):
                            name_change_input = input("Do you want to change your name (y or n)? ")
                            if name_change_input.lower() == 'y':
                                new_name = input("Enter your new name: ")
                                self.scoreboard.scores[new_name] = self.scoreboard.scores.pop(current_player.name, 0)
                                current_player.update_name(new_name)
                                current_player.name = new_name

                        # Resetting the max round score and switching to the next player
                        max_round_score = 0
                        current_player_index = (current_player_index + 1) % len(self.players)
                else:
                    print("Invalid input. Please press enter to roll the dice (or q to quit).")

            while True:
                quit_input = input("Do you want to quit (q) or restart (r) the game? ").lower()
                if quit_input == 'q':
                    return 
                elif quit_input == 'r':
                    self.reset_game()
                    break 
                else:
                    print("Invalid input. Please type q or r to quit/restart the game.")
