import random
import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 7 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'Here you can play hangman, guess the word correctly or the little man dies :(. Good luck!'
    expl = explanation.Explanation(expl_text, 7)
    expl.print_explanation()


def draw_hangman(mistake_count: int) -> None:
    print(mistake_count)


class Word:
    """
    The word class allows for generating a random word from a list. You can check a guess against this word and
    return whether it is correct (blanks filled) or wrong.
    """
    list_of_words = ['dodgy', 'clarkson', 'funtimes']

    def __init__(self) -> None:
        """
        Inits the Word object.
        """
        self.__random_word = ''
        self.__correct_guessed_letters = []

    def select_random_word(self) -> str:
        """
        Select a random word from a pre-defined list.
        :return: A random word, selected from the class variable list_of_words.
        :rtype: str
        """
        random_int = random.randint(0, len(Word.list_of_words) - 1)
        self.__random_word = Word.list_of_words[random_int]

    def verify_input(self, input_letter: str) -> bool:
        """
        Verify whether the chosen letter is in the word that has to be guessed. If it is, it's added to a list of
        correctly guessed letters. This list is later used to print the progress towards the solution.
        :param input_letter: The next letter the user entered to guess the word.
        :type input_letter: str
        :return: True if the letter is in the word, false if the letter is not.
        :rtype: bool
        """
        counter = 0
        for letter in self.__random_word:
            if letter == input_letter:
                counter += 1
                if letter not in self.__correct_guessed_letters:
                    self.__correct_guessed_letters.append(letter)
        if counter > 0:
            return True
        else:
            return False

    def progress(self) -> str:
        word_to_print = ' '
        for letter in self.__random_word:
            if letter in self.__correct_guessed_letters:
                word_to_print += letter
            else:
                word_to_print += '_'
        return word_to_print

    def print_revealed_word(self) -> str:
        return self.__random_word


class Game:
    """
    Start a game of hangman, we use the class Word to generate a new word and check the player's input.
    """
    def __init__(self) -> None:
        self.__mistake_counter = 0

    def play(self) -> None:
        sel_word = Word()
        sel_word.select_random_word()
        print(sel_word.progress())
        draw_hangman(self.__mistake_counter)
        # As long as the win or lose condition is not met, we keep playing.
        while self.__check_state(sel_word.progress()) == 'go':
            next_letter = input('Give me a letter: ')
            if sel_word.verify_input(next_letter):
                print(sel_word.progress())
                draw_hangman(self.__mistake_counter)
            else:
                self.__mistake_counter += 1
                sel_word.progress()
                draw_hangman(self.__mistake_counter)
        if self.__check_state(sel_word.progress()) == 'win':
            print('You won!')
        else:
            print(f'The little man died, you lose! The word was: {sel_word.print_revealed_word()}.')

    def __check_state(self, current_word: str) -> str:
        if '_' not in current_word:
            return 'win'
        elif self.__mistake_counter > 6:
            return 'lose'
        else:
            return 'go'
