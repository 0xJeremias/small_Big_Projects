
import random #<-- Import random library to use "random.randint()"
# # Program the computer guess your secret number beteween 1-1000
def guess_my_number(x):
    low = 1      # Initialize all the variables. And print instructions.
    high = x
    answer = ''
    counter = 0
    print("Computer says: ==============================================================")
    print(f"=> Choose a number beteween 1 and {x}. I will guess your secret number... <=")
    print("=============================================================================")
    while answer != 'c': # repeat while the guess number is not (c) "correct."
        counter += 1    #counter attempts
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        answer = input(f"Is {guess} too high (h)?, too low (l)?, or is correct(c)?")
        answer.lower()
        if answer == 'h':
            high = guess - 1
        elif answer == 'l':
            low = guess + 1
        elif answer != 'h' and answer != 'l' and answer != 'c':
            print(f"Please, insert a valid option.")
            answer = input(f"Is {guess} too high (h)?, too low (l)?, or is correct(c)?")
            answer.lower()     

    print("__________________________________________________")
    print(f"Yes!!, the computer guessed your secret number correctly!, it is {guess}")
    print(f"After {counter} attempts.")

guess_my_number(1000)
