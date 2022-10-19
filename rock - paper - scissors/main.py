import random
import sys
import time

end, wins, losses, ties, elements_list = False, 0, 0, 0, ["ROCK", "PAPER", "SCISSOR"]
print("Let's play ROCK, PAPER, SCISSOR!")
while not end:
    time.sleep(1)
    print(f"{wins} Wins, {losses} Losses and {ties} Ties")
    time.sleep(0.5)
    move = input("Enter your move: (r)ock, (p)aper, (s)cissor or (q)uit\n> ")
    # Input "r" for Rock, "p" for Paper, "s" for Scissor and "q" for Quit.
    if move.lower() == "q":  # Quitting the Game
        print("Hope you enjoyed the game :)")
        break

    if move.lower() == "r":  # Inputted Rock
        print("ROCK versus..")
        time.sleep(0.5)
        random_element = random.choice(elements_list)
        print(random_element)

        if random_element.lower() == "rock":
            print("It's a tie!\n")
            ties += 1
        elif random_element.lower() == "paper":
            print("You lose!\n")
            losses += 1
        elif random_element.lower() == "scissor":
            print("You win!\n")
            wins += 1

    elif move.lower() == "p":  # Inputted Paper
        print("PAPER versus..")
        time.sleep(0.5)
        random_element = random.choice(elements_list)
        print(random_element)

        if random_element.lower() == "rock":
            print("You win!\n")
            wins += 1
        elif random_element.lower() == "paper":
            print("It's a tie!\n")
            ties += 1
        elif random_element.lower() == "scissor":
            print("You lose!\n")
            losses += 1

    if move.lower() == "s":  # Inputted Scissor
        print("SCISSOR versus..")
        time.sleep(0.5)
        random_element = random.choice(elements_list)
        print(random_element)

        if random_element.lower() == "rock":
            print("You lose!\n")
            losses += 1
        elif random_element.lower() == "paper":
            print("You win!\n")
            wins += 1
        elif random_element.lower() == "scissor":
            print("It's a tie!\n")
            ties += 1
print("See ya!"), sys.exit()
