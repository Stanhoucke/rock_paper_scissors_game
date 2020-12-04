class Game():
    
    def play(self, player_1_choice, player_2_choice):
        # Convert inputs to lowercase
        player_1_choice = player_1_choice.lower()
        player_2_choice = player_2_choice.lower()

        player_choice_list = [player_1_choice, player_2_choice]
        valid_choice_list = ["rock", "paper", "scissors"]
        valid_choice_count = 0

        # Check if both players input valid options
        for player_choice in player_choice_list:
            for valid_choice in valid_choice_list:
                if player_choice == valid_choice:
                    valid_choice_count += 1
        if valid_choice_count != 2:
            return "One of the players didn't choose 'rock', 'paper', or 'scissors', please check your spelling and try again."
        # Check for winner
        else:
            if player_1_choice == "rock" and player_2_choice == "scissors":
                return f"Player 1 wins by playing {player_1_choice}!"
            elif player_1_choice == "paper" and player_2_choice == "rock":
                return f"Player 1 wins by playing {player_1_choice}!"
            elif player_1_choice == "scissors" and player_2_choice == "paper":
                return f"Player 1 wins by playing {player_1_choice}!"
            elif player_1_choice == player_2_choice:
                return None
            else:
                return f"Player 2 wins by playing {player_2_choice}!"