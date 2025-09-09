import random  
choices = ["rock", "paper", "scissors"]
player = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))
if player not in [0, 1, 2]:
    print("Invalid choice! Please choose 0, 1, or 2.")
else:
    print(f"You chose {choices[player]}")
    pc = random.randint(0, 2)
    print(f"PC chose {choices[pc]}")

    # -------------------------
    # Result logic:
    # (player - pc) % 3 gives:
    #   0 → Draw
    #   1 → Player wins
    #   2 → PC wins
    # -------------------------
    
    if player == pc:
        print("It's a draw!")

    elif (player - pc) % 3 == 1:
        # Player wins if the result is 1
        # Explanation:
        #   (player - pc) % 3 wraps values in the range [0,2]
        #   Cases:
        #     rock (0) beats scissors (2): (0 - 2) % 3 = 1 → player wins
        #     paper (1) beats rock (0):   (1 - 0) % 3 = 1 → player wins
        #     scissors (2) beat paper (1): (2 - 1) % 3 = 1 → player wins
        print("You win!")

    else:
        print("PC wins!")
