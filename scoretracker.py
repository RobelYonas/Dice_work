class scoreboard:
    def __init__(self, player_names):
        self.player_names = player_names
        self.scores = {name: 0 for name in player_names}

    def hold_score(self, round_score, current_player_index):
        self.scores[self.player_names[current_player_index]] += round_score

    def display_scoreboard(self):
        print("Current scores:")
        for name, score in self.scores.items():
            print(f"{name}: {score}")
