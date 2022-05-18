import random
import sys
import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 4 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'Another game??? Ubisoft, here I come. You saw the title right? I refuse to explain this any further.'\
                'I SHALL NOT EXPLAIN'
    expl = explanation.Explanation(expl_text, 4)
    expl.print_explanation()


class RockPaperScissors:
    """
    Create a RockPaperScissors object to play a game of rock, paper, scissors.
    """
    def __init__(self) -> None:
        """
        Inits the RockPaperScissors class. A question is asked on initialization: does the user want to play with
        rock, paper or scissors.
        0 = rock
        1 = paper
        2 = scissors
        """
        try:
            # The user chooses the hand he wants to play and cannot choose anything else than 0, 1 or 2
            self.__choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.'))
            if self.__choice < 0 or self.__choice > 2:
                raise ValueError
        except ValueError:
            sys.exit('Fail, you did not enter 0, 1 or 2.')

    def play(self) -> None:
        """
        Start the game, the AI bot gets a pseudo random hand (0, 1 or 2). This hand gets checked against the users
        choice. The outcome is either a print: 'Computer Wins!', 'You Win!' or 'Draw'.
        :return: None
        """
        # We generate a random int from 0 to 2, this converts to the hand the computer will play agains the user.
        computer_choice = random.randint(0, 2)
        list_of_choices = ['rock', 'paper', 'scissors']
        print('Computer has: {}'.format(list_of_choices[computer_choice]))

        # 0 wins vs 2, loses vs 1
        if self.__choice == 0:
            if computer_choice == 1:
                outcome = 'Computer wins!'
            elif computer_choice == 2:
                outcome = 'You win!'
            else:
                outcome = 'Draw'
        # 1 wins vs 0, loses vs 2
        elif self.__choice == 1:
            if computer_choice == 2:
                outcome = 'Computer wins!'
            elif computer_choice == 0:
                outcome = 'You win!'
            else:
                outcome = 'Draw'
        # 2 wins vs 1, loses vs 0
        else:
            if computer_choice == 0:
                outcome = 'Computer wins!'
            elif computer_choice == 1:
                outcome = 'You win!'
            else:
                outcome = 'Draw'

        print(outcome)
