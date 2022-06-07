import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input('Do you want - rock, paper or scissors?\n')

if computer_choice == user_choice:
    print(f'TIE the computer had {computer_choice} as well')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(f'WIN, the computer had {computer_choice}')
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f'WIN, the computer had {computer_choice}')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(f'WIN, the computer had {computer_choice}')
else:
    print(f'You lose, the computer had {computer_choice}')
