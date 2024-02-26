
class player2:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        # Method to add score to the player's current score
        self.score += score

    def reset_score(self):
        # Method to reset the player's score to 0
        self.score = 0
