import random

#Generate secret number
secret_number = random.randint(1, 100)
print(secret_number)
#Track attmept
attempt = 0

while True:
    try:
        user_guess = int(input("Guess the number (1-100): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Please guess a number between 1 and 100:")
        continue
    attempt += 1
    
    if user_guess > secret_number:
        print("Too high.")
    elif user_guess < secret_number:
        print("Too low")
    else:
        print("correct")
        break

print("Total attempt used: ", attempt)