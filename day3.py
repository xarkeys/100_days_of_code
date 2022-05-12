import sys

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
choice1 = input('You\'re at a cross road. Where do you want to go? Type left or right: \n')

if choice1.lower() == 'left':
    choice2 = input('Swim or wait?\n')
    if choice2.lower() == 'wait':
        choice3 = input('Which door? Blue, red or yellow?\n')
        if choice3.lower() == 'yellow':
            sys.exit('You win!')
        else:
            sys.exit('Game Over')
    else:
        sys.exit('Game Over')
else:
    sys.exit('Game Over')
