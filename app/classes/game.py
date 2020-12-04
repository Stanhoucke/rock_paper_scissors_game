class Game():
    
    def play(self, player_1_choice, player_2_choice):
        player_choice_list = [player_1_choice, player_2_choice]
        valid_choice_list = ["Rock", "Paper", "Scissors"]
        valid_choice_count = 0

        # Check if both players input valid options
        for player_choice in player_choice_list:
            for valid_choice in valid_choice_list:
                if player_choice == valid_choice:
                    valid_choice_count += 1
        if valid_choice_count != 2:
            return "One of the players didn't choose 'Rock', 'Paper', or 'Scissors', please check your spelling and try again."
        # Check for winner
        else:
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