import random

# Choices mapping
choices = ["rock", "paper", "scissors"]

# Player input
player = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))

if player not in [0, 1, 2]:
    print("Invalid choice! Please choose 0, 1, or 2.")
else:
    print(f"You chose {choices[player]}")

    # PC choice
    pc = random.randint(0, 2)
    print(f"PC chose {choices[pc]}")

    # Result logic
    if player == pc:
        print("It's a draw!")
    elif (player - pc) % 3 == 1:  # clever math trick ✨
        print("You win!")
    else:
        print("PC wins!")
