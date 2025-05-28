import random
hidden_number= random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("the number in between of 1 t0 100 ,can you guess it")
while True:
    try:
        guess=int(input("Enter your guess: "))
        
        if guess <hidden_number:
            print("Too low! Try again.")
        elif guess >hidden_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {hidden_number} correctly!")
            break
    except ValueError:
        print("Please enter a valid number.")
