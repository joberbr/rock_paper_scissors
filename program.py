import random
from actors import Roll, Player


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 0
    p1_rounds_won = 0
    p2_rounds_won = 0
    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = get_player_roll(rolls, player1)

        outcome = p1_roll.can_defeat(p2_roll)

        print(
            f"{player2.name.capitalize()} has rolled '{p2_roll.name}'' and {player1.name.capitalize()} has rolled '{p1_roll.name}'."
        )

        if not outcome:
            if p2_roll == p1_roll:
                continue
            else:
                print(f"{player2.name.capitalize()} has won round!")
                p2_rounds_won += 1
        else:
            print(f"{player1.name} has won round!")
            p1_rounds_won += 1

        count += 1

    print(
        f"{player1.name} has won {p1_rounds_won} rounds and {player2.name.capitalize()} has won {p2_rounds_won} rounds."
    )
    if p1_rounds_won > p2_rounds_won:
        print(f"{player1.name} has WON game!!!")
    elif p2_rounds_won > p1_rounds_won:
        print(f"{player2.name.capitalize()} has WON game!!!")
    else:
        print("Game is a TIE.")


def print_header():
    print(
        """
    -------------------------------------------------
                    Rock, Paper, Scissors
    -------------------------------------------------
    """
    )


def build_the_three_rolls():
    rock = Roll("rock", "scissors")
    paper = Roll("paper", "rock")
    scissors = Roll("scissors", "paper")

    return rock, paper, scissors


def get_players_name():
    player_name = input("What is your name?: ")

    return player_name


def get_player_roll(rolls, player1):
    p1_choice = input(f"{player1.name}, do you choose (r)ock, (p)aper, (s)cissors?: ")
    if p1_choice == "r":
        p1_roll = rolls[0]
    if p1_choice == "p":
        p1_roll = rolls[1]
    if p1_choice == "s":
        p1_roll = rolls[2]

    return p1_roll


if __name__ == "__main__":
    main()
