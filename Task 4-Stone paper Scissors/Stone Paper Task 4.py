import random
from PIL import Image

choices = ["stone", "paper", "scissors"]

def display_image(choice):
    image_path = f"C:/college/internships/Codsoft Python/Python programming/Game - Task 4/{choice}.png"  # Replace with the actual path to your images
    image = Image.open(image_path)
    image.show()

def Game_Play():
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (0 for stone, 1 for paper, 2 for scissors): ")

    if user_choice not in ["0", "1", "2"]:
        print("You entered an invalid choice. You lose.")
    else:
        user_choice = choices[int(user_choice)]
        print("Your choice:", user_choice)
        display_image(user_choice)
        print("Computer's choice:", computer_choice)
        display_image(computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
            display_image("tie")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "stone") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            display_image("win")
        else:
            print("Computer wins!")
            display_image("lose")

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        Game_Play()

Game_Play()