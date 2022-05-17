import sys
import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 3 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'A game??? On day three???? How about that? This game uses some advanced, interactive, AI powered, '\
                'choice mechanism. Don\'t believe me? Give it a go!'
    expl = explanation.Explanation(expl_text, 3)
    expl.print_explanation()


class TreasureIsland:
    """
    Create an object of the TreasureIsland class. This starts one game of Treasure Island.
    """
    def __init__(self) -> None:
        # empty constructor
        pass

    def __input_validator(self, user_choice: str, step: int) -> None:
        """
        Validate the choice the user made, the choice must be made between the presented options. Entering any other
        value will result in a ValueError in this function.
        :param user_choice:
        :type user_choice: str
        :param step:
        :type step: int
        :raises: ValueError
        :return: None
        """
        try: 
            if step == 1:
                if user_choice.lower() != 'left' and user_choice.lower() != 'right':
                    raise ValueError
            elif step == 2:
                if user_choice.lower() != 'swim' and user_choice.lower() != 'wait':
                    raise ValueError
            elif step == 3:
                if user_choice.lower() != 'blue' and user_choice.lower() != 'red' and user_choice.lower() != 'yellow':
                    raise ValueError
        except ValueError:
            print('Why are you doing this? Stick to the rules!')
            sys.exit('I\'m done with you!')
    
    def __check_step1(self, user_choice: str) -> None:
        """
        Check whether the first choice allows the user to continue to step 2 or if the game ends here.
        :param user_choice: The choice the user made, either left or right.
        :type user_choice: str
        :return: None
        """
        self.__input_validator(user_choice, 1)
        if user_choice.lower() == 'left':
            # Left is correct, we present the user with another question and use the next function for validating the
            # answer.
            choice2 = input('Oh no, water! Do you want to swim or wait? ')
            self.__check_step2(choice2)
        else:
            sys.exit('Game Over')

    def __check_step2(self, user_choice: str) -> None:
        """
        Check whether the second choice allows the user to continue to step 3 or if the game ends here.
        :param user_choice: The choice the user made, either wait or swim.
        :type user_choice: str
        :return: None
        """
        self.__input_validator(user_choice, 2)
        if user_choice.lower() == 'swim':
            # Swim is correct, we present the user with another question and continue to the next step.
            choice3 = input('Which door do you want to open? Blue, red or yellow? ')
            self.__check_step3(choice3)
        else:
            sys.exit('Game Over')

    def __check_step3(self, user_choice: str) -> None:
        """
        Check whether the third choice allows the user to continue and win the game or if the game ends here.
        :param user_choice: The choice the user made, either yellow, blue or red.
        :type user_choice: str
        :return: None
        """
        self.__input_validator(user_choice, 3)
        if user_choice.lower() == 'yellow':
            # Yellow is correct, the user wins the game.
            print('You found the treasure!')
        else:
            print('Game over!')
            sys.exit()

    def play(self) -> None:
        """
        Start a game of Treasure Island. This function asks the first question, validates the answer and does
        the appropriate action:
        - Either you made the right choice and continue the game, or
        - you made the wrong choice and the game ends.
        :return: None
        """
        print('Welcome to Treasure Island.')
        print('Your mission is to find the treasure.')
        choice1 = input('You\'re at a cross road. Where do you want to go, left or right? ')
        self.__check_step1(choice1)
