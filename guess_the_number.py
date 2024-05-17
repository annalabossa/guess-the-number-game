import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guess = None

    print("Welcome to Guess the Number!")
    print("I have selected a number between 1 and 10.")
    
    while guess != number_to_guess:
        guess = int(input("Take a guess: "))
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")

if __name__ == "__main__":
    guess_the_number()
