import random
import sys
import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 5 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'On day five a password generator was created. Password spraying attacks are futile after using '\
                'this program. The program asks three questions the user has to answer (within limits): how many '\
                'letters, symbols and numbers they want in their randomly generated password.'
    expl = explanation.Explanation(expl_text, 5)
    expl.print_explanation()


class RandomPassword:
    """
    Create a RandomPassword object to generate a random password.
    """
    # list_of_symbols will be used as a feed for random symbols
    __list_of_symbols = ['[', ']', '{', '}', '!', '@', '#', '$']

    def __init__(self) -> None:
        """
        Inits the RandomPassword object.
        """
        try:
            # We ask the user for three values (on object initialization), all three of them must 
            # be below 21 and above -1. If not a 'ValueError' will be raised which closes the program.
            self.__num_letters = int(input('How many letters would you like in your password? (max 20)\n'))
            if self.__num_letters > 20 or self.__num_letters < 0:
                raise ValueError
            self.__num_symbols = int(input('How many symbols would you like in your password? (max 20)\n'))
            if self.__num_symbols > 20 or self.__num_symbols < 0:
                raise ValueError
            self.__num_numbers = int(input('How many numbers would you like in your password? (max 20)\n'))
            if self.__num_numbers > 20 or self.__num_numbers < 0:
                raise ValueError
        except ValueError:
            sys.exit('An invalid entry has been made. Shutdown unavoidable...')

    def __shuffle_word(self, word: str) -> str:
        """
        Shuffle a string value.
        :param word: The (ordered) string value that has to be shuffled.
        :type word: str
        :return: The shuffled version of the initial 'word' argument.
        :rtype: str
        """
        self.word = word
        word = list(word)
        random.shuffle(word)
        return ''.join(word)

    def generate_password(self) -> str:
        """
        Generate a password based on the input of:
        - number of letters (capital and regular are randomized by this function)
        - number of symbols (randomly chosen from a pre-defined list)
        - number of numbers
        :return: The generated password, random and shuffled.
        :rtype: str
        """
        generated_password = ''
        # ASCII letters (lower) are 97 to 122
        # ASCII letters (upper) are 65 to 90
        # In this for loop we first generate a random int (0 or 1) that decides if the letter will be 
        # a capital letter or a lowercase letter. After that we generate letters based on their ASCII
        # decimal code. 
        for i in range(0, self.__num_letters):
            upper_or_lower = random.randint(1, 2)
            if upper_or_lower == 1:
                random_int = random.randint(97, 122)
                generated_password += chr(random_int)
            else:
                random_int = random.randint(65, 90)
                generated_password += chr(random_int)

        # The for loop that adds symbols searches in a list of symbols. 
        for i in range(0, self.__num_symbols):
            random_int = random.randint(0, len(self.__list_of_symbols) - 1)
            generated_password += self.__list_of_symbols[random_int]

        # The for loop that adds random numbers. 
        for i in range(0, self.__num_numbers):
            generated_password += str(random.randint(0, 9))

        # After generating all requested characters, we shuffle them using the 'shuffle_word' function. 
        generated_password = self.__shuffle_word(generated_password)

        return generated_password
        