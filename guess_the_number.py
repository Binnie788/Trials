import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0

    while guess != random_num:
        guess = int(input(f"Enter any number between 1 to {x}:  "))

        if guess > random_num:
            print("lower!")
        
        elif guess < random_num:
            print("higher!")
        
    print("You won")

guess(100)