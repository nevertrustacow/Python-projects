import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit(): # checks that it is indeed a number
    top_of_range = int(top_of_range) # if tru it will convert it into an int


    if top_of_range <= 0:
        print("Please type a number that is greater than 0 ")
        quit()

else:
    print("Please type a number next time")
    quit()


random_number = random.randint(0, top_of_range) # it generates up to whatever number the user types in
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): # checks that it is indeed a number
        user_guess = int(user_guess) # if true it will convert it into an int
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You Got It!")
        break

    elif user_guess > random_number:
        print("You wew above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses")

