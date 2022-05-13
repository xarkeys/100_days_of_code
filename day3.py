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

class treasure_island():

    def __input_validator(self, user_choice, step):
        '''
        This function takes the user's choice and the step he is currently playing. These values
        are used to verify a valid choice has been made. If not the program will close. 
        '''
        try: 
            if step == 1:
                if user_choice.lower() != 'left' and user_choice.lower() != 'right': raise ValueError
            elif step == 2:
                if user_choice.lower() != 'swim' and user_choice.lower() != 'wait': raise ValueError
            elif step == 3:
                if user_choice.lower() != 'blue' and user_choice.lower() != 'red' and user_choice.lower() != 'yellow': raise ValueError
        except ValueError:
            print('Why are you doing this? Stick to the rules!')
            sys.exit('I\'m done with you!')
    
    def __check_step1(self, user_choice):

        '''
        This function takes one parameter, the user's choice. (left or right)
        Left will allow the user to continue to step 2.
        Right will end the game.
        '''

        self.__input_validator(user_choice, 1)

        if user_choice.lower() == 'left':
            choice2 = input('Oh no, water! Do you want to swim or wait? ')
            self.__check_step2(choice2)
        else:
            sys.exit('Game Over')

    def __check_step2(self, user_choice):

        '''
        This function takes one parameter, the user's choice. (swim or wait)
        Swim will allow the user to continue to step 3.
        Wait will end the game. 
        '''

        self.__input_validator(user_choice, 2)

        if user_choice.lower() == 'swim':
            choice3 = input('Which door do you want to open? Blue, red or yellow? ')
            self.__check_step3(choice3)
        else:
            sys.exit('Game Over')

    def __check_step3(self, user_choice):

        '''
        This function takes one parameter, the user's choice. (blue, red or yellow)
        Yellow will lead to the user's victory.
        Blue or red will end the game. 
        '''

        self.__input_validator(user_choice, 3)

        if user_choice.lower() == 'yellow':
            print('You found the treasure!')
        else:
            print('Game over!')
            sys.exit()


    def play_a_game(self):

        '''
        This function starts a game of treasure island, input is asked to record the user's first choice:
        Left or right. This input is used to call the __check_step1 function. 
        '''

        print('Welcome to Treasure Island.')
        print('Your mission is to find the treasure.')
        choice1 = input('You\'re at a cross road. Where do you want to go, left or right? ')
        self.__check_step1(choice1)

