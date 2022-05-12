import random
import sys

def challenge_explanation():
    '''
    This function returns an intro text to the challenge.
    '''
    explanation = '''
    -------------------- DAY04 --------------------
    - Title: Rock, paper, scissors                -
    - Another game??? Ubisoft, here I come.       -
    - You saw the title right? I refuse to        -
    - explain this any further.                   -
    - I SHALL NOT EXPLAIN                         -
    -----------------------------------------------
    '''

    return explanation 

def rock_paper_scissors():
    '''
    Main program.
    '''
    try:
        choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.'))
        if choice < 0 or choice > 2: raise ValueError
    except ValueError:
        sys.exit('Fail, you did not enter 0, 1 or 2.')
    computer_choice = random.randint(0,2)
    list_of_choices = ['rock', 'paper', 'scissor']
    print('computer chose {}'.format(list_of_choices[computer_choice]))

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
