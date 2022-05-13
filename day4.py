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

class rock_paper_scissors():

    def __init__(self):
        try:
            # The user chooses the hand he wants to play. 
            self.__choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.'))
            if self.__choice < 0 or self.__choice > 2: raise ValueError
        except ValueError:
            sys.exit('Fail, you did not enter 0, 1 or 2.')

    def play_a_game(self):

        '''
        This function uses the user's chosen value (0, 1 or 2) and returns any of these three options:
        - You win!
        - Computer wins!
        - Draw
        '''

        computer_choice = random.randint(0,2)
        list_of_choices = ['rock', 'paper', 'scissor']
        print('Computer has: {}'.format(list_of_choices[computer_choice]))

        if self.__choice == 0:
            if computer_choice == 1:
                outcome = 'Computer wins!'
            elif computer_choice == 2:
                outcome = 'You win!'
            else:
                outcome = 'Draw'
        elif self.__choice == 1:
            if computer_choice == 2:
                outcome = 'Computer wins!'
            elif computer_choice == 0:
                outcome = 'You win!'
            else:
                outcome = 'Draw'
        else:
            if computer_choice == 0:
                outcome = 'Computer wins!'
            elif computer_choice == 1:
                outcome = 'You win!'
            else:
                outcome = 'Draw'

        return outcome