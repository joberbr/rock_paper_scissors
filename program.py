"""A simple Rock, Paper, Scissors game using classes."""


import random
from actors import Roll, Player


def main():
    """Main function if file is not imported as a module."""
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    """Starts the game and initiates the counts"""
    count = 0
    p1_rounds_won = 0
    p2_rounds_won = 0
    p1_name = player1.name.upper()
    p2_name = player2.name.upper()
    while count < 3 and p1_rounds_won < 2 and p2_rounds_won < 2:
        p2_roll = random.choice(rolls)
        p1_roll = get_player_roll(rolls, player1)

        outcome = check_round_winner(p1_roll, p2_roll)
        if outcome == "Player 1":
            p1_rounds_won += 1
        if outcome == "Player 2":
            p2_rounds_won += 1

        print_round_results(player1, player2, p1_roll, p2_roll, outcome, count)
        print()

        if not outcome == "Tie":
            count += 1

    print_game_results(p1_name, p1_rounds_won, p2_name, p2_rounds_won)


def print_header():
    """Prints the header of the game."""
    print(
        """
==================================================================
##################################################################

                    Rock, Paper, Scissors

##################################################################
==================================================================
    """
    )


def build_the_three_rolls():
    """Builds the rock, paper and scissors rolls."""
    rock = Roll("rock", "scissors", "paper")
    paper = Roll("paper", "rock", "scissors")
    scissors = Roll("scissors", "paper", "rock")

    return rock, paper, scissors


def get_players_name():
    """Gets the player's name."""
    player_name = input("What is your name?: ")

    return player_name


def get_player_roll(rolls, player1):
    """Gets the roll for the human player."""
    p1_name = player1.name.upper()
    while True:
        try:
            p1_choice = input(
                f"{p1_name}, do you choose (r)ock, (p)aper, (s)cissors?: "
            )

            if p1_choice.lower() == "r":
                p1_roll = rolls[0]
            elif p1_choice.lower() == "p":
                p1_roll = rolls[1]
            elif p1_choice.lower() == "s":
                p1_roll = rolls[2]
            else:
                print("Please provide a valid choice.")

            return p1_roll

        except UnboundLocalError:
            continue


def check_round_winner(p1_roll, p2_roll):
    """Checks the winner of the round."""
    won = p1_roll.can_defeat(p2_roll)
    lost = p1_roll.defeated_by(p2_roll)

    if won:
        return "Player 1"
    elif lost:
        return "Player 2"
    else:
        return "Tie"


def print_round_results(player1, player2, p1_roll, p2_roll, outcome, count):
    """Prints the rolls for each player and who won."""
    p1_name = player1.name.upper()
    p2_name = player2.name.upper()
    rnd = count + 1
    print(
        f"{p2_name} has rolled '{p2_roll.name}' and {p1_name} has rolled '{p1_roll.name}'."
    )

    if outcome == "Tie":
        print("This round is a TIE.")
    if outcome == "Player 2":
        print(f"{p2_name} has won round {rnd}!")
    if outcome == "Player 1":
        print(f"{p1_name} has won round {rnd}!")


def print_game_results(p1_name, p1_rounds_won, p2_name, p2_rounds_won):
    """Prints which player won the game."""
    print(
        f"{p1_name} has won {p1_rounds_won} rounds and {p2_name} has won {p2_rounds_won} rounds."
    )
    if p1_rounds_won > p2_rounds_won:
        print(f"{p1_name} has WON game!!!")
    if p2_rounds_won > p1_rounds_won:
        print(f"{p2_name} has WON game!!!")


if __name__ == "__main__":
    main()
