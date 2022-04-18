import random #<-- Import random library to use "random.randint()"
# # Program to guess a number beteween 1-1000.
def guess(x):
    random_number = random.randint(1,x) #<- computer take a random number beteween (1,x) and store it in varaible "random_number"
    guess = 0 # <- initialize guess variable
    attempts = 0 # <- initialize attempts variable for counter
    print("Computer says: =========================================================")
    print(f"=> Choose a number beteween 1 and {x}. And guess my secret number... <=")
    print("========================================================================")
    while guess != random_number:  # while guess != random_number, choose, is high or low, otherwise you found the secret number.
        attempts += 1 # <- a counter for attemps by 1
        guess = int(input(f"Choose a number beteween 1 and {x}: "))
        if guess < random_number:
            print(f"Sorry, {guess} is too low, guess again!: ")
        elif guess > random_number:
            print(f"Sorry, {guess} is too high, guess again!: ")
    print("__________________________________________________")
    print(f"Yesss! you guessed!! the number is {random_number}!!, congrats!!.\nAfter {attempts} attempts!.")

guess(1000)
