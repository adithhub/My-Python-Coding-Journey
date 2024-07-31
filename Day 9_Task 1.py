# random number guessing game by random module
import random
random_number = random.randint(1, 20)
print(random_number)
start_game = input("Guessing game. Guess the number within the range of 1 to 20. ,"
                   "You only have 3 chance to win the game. Press any key to start: ")
user_input = 0
for i in range(1, 4):
    user_input = int(input("Enter the number: "))
    if user_input == random_number:
        print(f"{random_number} is the answer. YOU WON.")
        break
    elif user_input > random_number:
        print("Your number is greater than the number.Try again")
    else:
        print("Your number is lesser than the number. Try again.")
if user_input == random_number:
    print("Ma boy you won !")
else:
    print(f"You are out of chances. By the way {random_number} is the correct answer.")
