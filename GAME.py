import random

n = random.randint(1, 100)

name = str(input("Hello! What is your name? "))
guess = int(input("Enter an number from 1 to 100: "))
guess_count = 1

while n != guess:
    if guess < n:
        print("Your guess is too low")
        guess = int(input("Try another number: "))
        guess_count += 1
    elif guess > n:
        print("Your guess is too high")
        guess = int(input("Try another number: "))
        guess_count += 1
   
if guess == n:
    print(f"Good job, {name}! You found the number in {guess_count} tries!")