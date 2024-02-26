from dice_roll import Die
import random

class games2:
    
    def __init__(self):
        # creating an instance of Die class
        self.dice = Die()
        
    def name(self):
        # getting the name of the player from user input
        player_name = input("What is your name? ")
        return player_name

    def game_play(self, difficulty):
        # getting player names and initializing their scores
        players_name = self.name()
        players = [players_name, 'Computer']
        scores = {players_name: 0, 'Computer': 0}
        
        # determining the maximum score for each turn based on the difficulty level
        max_turn_score = {'easy': 15, 'medium': 20, 'hard': 25}[difficulty]
        
        while True:
            for player in players:
                if player == players_name:
                    # player's turn
                    choice = input("Roll(r) or Hold(h)?: ")
                    turn_score = 0
                    total_score = 0
                    
                    # player keeps rolling until they decide to hold or pig out
                    while choice == 'r':
                        dice_value = self.dice.roll()
                        if dice_value == 1:
                            turn_score = 0
                            print("- rolled a ",dice_value)
                            print("Pigged out!")
                            break
                        else:
                            turn_score += dice_value
                            print("- rolled a ", dice_value)

                        # checking if the turn score is greater than or equal to the maximum score for the turn
                        if turn_score >= max_turn_score:
                            total_score += turn_score
                            print("Turn score is: ", turn_score)
                            print("Your total score is: ", total_score)

                            if total_score >= 100:
                                break

                            choice = input("Roll(r) or Hold(h)?: ")
                        else:
                            choice = input("Roll(r) or Hold(h)?: ")

                    # player chooses to hold
                    if choice.lower() == 'h':
                        total_score += turn_score
                        scores[player] += total_score
                        print("Your total score is: ", total_score)
                        print("Your score so far is: ", scores[player])
                        
                else:
                    # computer's turn
                    turn_score = 0
                    print("It is " + str(player) + "'s turn.")
                    
                    # defining the computer's turn as a separate function for reusability
                    def computer_turn(dice):
                        nonlocal turn_score, scores
                        
                        roll_again = True
                        
                        # computer keeps rolling until they decide to hold or pig out or the turn score reaches the maximum for the turn
                        while roll_again and (turn_score <= max_turn_score):
                            dice_value = dice.roll()
                            if dice_value == 1:
                                turn_score = 0
                                print("- rolled a ", dice_value)
                                print("Pigged out!")
                                roll_again = False
                                break
                            else:
                                turn_score += dice_value
                                print("- rolled a ", dice_value)
                                
                                if (scores['Computer'] + turn_score) >= 100:
                                    roll_again = False
                                    break
                                
                                if turn_score > max_turn_score // 2:
                                    # Decide whether to continue rolling based on the computer's IQ
                                    if random.random() < {'easy': 0.25, 'medium': 0.5, 'hard': 0.75}[difficulty]:
                                        roll_again = True
                                    else:
                                        roll_again = False
                                else:
                                    roll_again = True
                    
                    computer_turn(self.dice)
                    
                    scores[player] += turn_score
                    
                    # Print the turn score and both players' scores
                    print("Turn score is: ", turn_score)
                    print('{} score: {} {} score: {}'.format(players[0], scores[players[0]], players[1], scores[players[1]]))
                    
                    # Check for win condition
                    if scores[player] >= 100:
                        winner = [k for k, v in scores.items() if v == max(scores.values())]
                        print(str(winner[0]) + " is the winner!")
                        return

                    # Allow player to quit with cheat code
                    cheat_code = input("Enter 'win' to win the game or 'quit' to end the game or press enter to continue: ")
                    if cheat_code.lower() == 'win' and player == players_name:
                        scores[player] = 100
                        winner = [k for k, v in scores.items() if v == max(scores.values())]
                        print(str(winner[0]) + " is the winner!")
                        return
                    elif cheat_code.lower() == 'quit':
                        print("Thanks for playing!")
                        return
                    
                    # Allow player to change their name
                    name_change = input("Enter 'change' to change your name or any other key to continue playing or press enter to continue: ")
                    if name_change.lower() == 'change':
                        new_name = self.name()
                        scores[new_name] = scores.pop(player)
                        players[players.index(player)] = new_name
                        print("Your name has been changed to " + new_name)
