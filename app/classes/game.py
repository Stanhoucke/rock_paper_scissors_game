class Game():
    
    def play(self, player_1_choice, player_2_choice):
        if player_1_choice == "Rock" and player_2_choice == "Scissors":
            return f"Player 1 wins by playing {player_1_choice.lower()}!"
        elif player_1_choice == "Paper" and player_2_choice == "Rock":
            return f"Player 1 wins by playing {player_1_choice.lower()}!"
        elif player_1_choice == "Scissors" and player_2_choice == "Paper":
            return f"Player 1 wins by playing {player_1_choice.lower()}!"
        elif player_1_choice == player_2_choice:
            return "It's a tie!"
        else:
            return f"Player 2 wins by playing {player_2_choice.lower()}!"