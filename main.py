import random


def rock_paper_scissors():
    cpu = "CPU"
    player = input("Enter player name: ")
    values = ["R", "P", "S"]
    while True:
        player_option = player_game_option(values)
        cpu_option = cpu_random_option(values)
        print(player + "(" + player_option + ") : " + cpu + "(" + cpu_option + ")")

        if player_option == cpu_option:
            print("It's a tie, play again")
        elif (cpu_option == "Rock" and player_option == "Scissors") or \
                (cpu_option == "Paper" and player_option == "Rock") or \
                (cpu_option == "Scissors" and player_option == "Paper"):

            print(cpu + " wins")
            break
        else:
            print(player + " wins")
            break


def player_game_option(accepted_values):
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
