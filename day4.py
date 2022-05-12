import random

choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.'))
computer_choice = random.randint(0,2)
list_of_choices = ['rock', 'paper', 'scissor']
print('computer chooses {}'.format(list_of_choices[computer_choice]))

if choice == 0:
    if computer_choice == 1:
        print('computer wins')
    elif computer_choice == 2:
        print('you win')
    else:
        print('draw')
elif choice == 1:
    if computer_choice == 2:
        print('computer wins')
    elif computer_choice == 0:
        print('you win')
    else:
        print('draw')
else:
    if computer_choice == 0:
        print('computer wins')
    elif computer_choice == 1:
        print('you win')
    else:
        print('draw')
