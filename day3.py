import sys

def challenge_explanation():
    '''
    This function returns an intro text to the challenge.
    '''
    explanation = '''
    -------------------- DAY03 --------------------
    - Title: Find the treasure                    -
    - A game??? On day three???? How about that   -
    - This game uses some advanced, interactive,  -
    - AI powered, choice mechanism. Don't         -
    - believe me? Give it a go!                   -
    -----------------------------------------------
    '''

    return explanation 

def treasure_island():
    '''
    Main program.
    '''
    print('Welcome to Treasure Island.')
    print('Your mission is to find the treasure.')
    try:
        choice1 = input('You\'re at a cross road. Where do you want to go? Type left or right: \n')
        choice1 = choice1.lower()
        if choice1 != 'left' and choice1 != 'right': raise ValueError
        if choice1 == 'left':
            choice2 = input('Oh no, water! Do you want to swim or wait?\n')
            choice2 = choice2.lower()
            if choice2 != 'swim' and choice1 != 'wait': raise ValueError
            if choice2 == 'wait':
                choice3 = input('Which door do you want to open? Blue, red or yellow?\n')
                choice3 = choice3.lower()
                if choice3 != 'blue' and choice3 != 'red' and choice3 != 'yellow': raise ValueError
                if choice3 == 'yellow':
                    sys.exit('You win!')
                else:
                    sys.exit('Game Over')
            else:
                sys.exit('Game Over')
        else:
            sys.exit('Game Over')
    except ValueError:
        print('Why are you doing this? Stick to the rules!')
