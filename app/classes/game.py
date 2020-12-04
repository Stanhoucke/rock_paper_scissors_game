class Game():
    
    def play(self, player_1_choice, player_2_choice):
        if player_1_choice == "Rock" and player_2_choice == "Scissors":
            return f"Player 1 wins by playing {player_1_choice.lower()}!"