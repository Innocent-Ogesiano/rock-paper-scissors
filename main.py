import random


def rock_paper_scissors():
    player1 = "COM"
    player2 = input("Enter player name: ")
    values = ["R", "P", "S"]
    while True:
        player2_option = input("pick an option between 'R', 'P' or 'S': ")
        while player2_option not in values:
            print("Invalid option, try again!")
            player2_option = input("pick an option between 'R', 'P' or 'S': ")

        player1_option = random.choice(values)
        if player2_option == "R":
            player2_option = "Rock"
        elif player2_option == "P":
            player2_option = "Paper"
        else:
            player2_option = "Scissors"

        if player1_option == "R":
            player1_option = "Rock"
        elif player1_option == "P":
            player1_option = "Paper"
        else:
            player1_option = "Scissors"
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


rock_paper_scissors()
