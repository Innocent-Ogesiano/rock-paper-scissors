import random


def rock_paper_scissors():
    player1 = "COM"
    player2 = input("Enter player name: ")
    values = ["R", "P", "S"]
    while True:
        player2_option = player2_game_option(values)
        player1_option = cpu_random_option(values)
        print(player2 + "(" + player2_option + ") : " + player1 + "(" + player1_option + ")")

        if player2_option == player1_option:
            print("It's a tie, play again")
        elif (player1_option == "Rock" and player2_option == "Scissors") or \
                (player1_option == "Paper" and player2_option == "Rock") or \
                (player1_option == "Scissors" and player2_option == "Paper"):

            print(player1 + " wins")
            break
        else:
            print(player2 + " wins")
            break


def player2_game_option(accepted_values):
    option = input("pick an option between 'R', 'P' or 'S': ")
    while option not in accepted_values:
        print("Invalid option, try again!")
        option = input("pick an option between 'R', 'P' or 'S': ")
    if option == "R":
        option = "Rock"
    elif option == "P":
        option = "Paper"
    else:
        option = "Scissors"
    return option


def cpu_random_option(accepted_values):
    cpu_option = random.choice(accepted_values)
    if cpu_option == "R":
        cpu_option = "Rock"
    elif cpu_option == "P":
        cpu_option = "Paper"
    else:
        cpu_option = "Scissors"
    return cpu_option


rock_paper_scissors()
