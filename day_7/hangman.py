import random
import explanation
from day_7.draw_hangman import draw_hangman


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 7 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: None
    """
    expl_text = 'Here you can play hangman, guess the word correctly or the little man dies :(. Good luck!'
    expl = explanation.Explanation(expl_text, 7)
    expl.print_explanation()


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

    def select_random_word(self) -> None:
        """
        Select a random word from a pre-defined list. The word gets assigned to the instance variable:
        __random_word.
        :return: None
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
        # A counter higher than 0 means the guessed letter is in the randomly chosen word.
        if counter > 0:
            return True
        else:
            return False

    def progress(self) -> str:
        """
        Track the progress the player is making. The correctly guessed letters are shown, the unguessed letters are
        replaced by underscores.
        :return: The currently guessed word, including underscores and/or letters.
        :rtype: str
        """
        word_to_print = ' '
        for letter in self.__random_word:
            if letter in self.__correct_guessed_letters:
                word_to_print += letter
            else:
                word_to_print += '_'
        return word_to_print

    def print_revealed_word(self) -> str:
        """
        If required, this function can be used to reveal the randomly chosen word.
        :return: The randomly chosen word.
        :rtype: str
        """
        return self.__random_word


class Game:
    """
    Start a game of hangman, we use the class Word to generate a new word and check the player's input.
    """
    def __init__(self) -> None:
        """
        Inits the Game class. The instance variable __mistake_counter is set to 0 at game start.
        """
        self.__mistake_counter = 0

    def play(self) -> None:
        """
        Start a game of hangman. We use the Word class for everything related to the random word that has to be guessed
        we keep checking whether it's game over (win or loss). If not, reprint the word (progress) and the hangman
        ASCII art.
        :return: None
        """
        sel_word = Word()
        sel_word.select_random_word()
        print(sel_word.progress())
        print(draw_hangman(self.__mistake_counter))
        # As long as the win or lose condition is not met, we keep playing.
        while self.__check_state(sel_word.progress()) == 'go':
            next_letter = input('Give me a letter: ').lower()
            try:
                if len(next_letter) != 1:
                    raise ValueError
                if ord(next_letter) < 97 or ord(next_letter) > 122:
                    raise ValueError
            except ValueError:
                print('Please enter a valid letter, and only one letter.')
                continue
            # Check if the letter has already been guessed correctly, if it is, it's counted as a mistake. If the
            # letter has already been guessed, but it's not in the word to guess, it counts as another mistake.
            if next_letter in sel_word.progress():
                print('This letter has already been guessed, this counts as a mistake.')
                self.__mistake_counter += 1
                print(sel_word.progress())
                print(draw_hangman(self.__mistake_counter))
            else:
                if sel_word.verify_input(next_letter):
                    # Run if the letter is guessed correctly (and it hasn't been guessed yet).
                    print(sel_word.progress())
                    print(draw_hangman(self.__mistake_counter))
                else:
                    # Run if the letter is guessed wrong (not necessarily for the first time).
                    self.__mistake_counter += 1
                    print(sel_word.progress())
                    print(draw_hangman(self.__mistake_counter))
        if self.__check_state(sel_word.progress()) == 'win':
            print('You won!')
        else:
            print(f'The little man died, you lose! The word was: {sel_word.print_revealed_word()}.')

    def __check_state(self, current_word: str) -> str:
        """
        Check the game over condition, win or lose. If neither conditions are met, keep playing.
        :param current_word: The progress towards the word that has to be guessed.
        :type  current_word: str
        :return: One of these options:
            - win: the word was guessed.
            - lose: the little man died.
            - go: game over condition is not met, keep playing.
        :rtype: str
        """
        # We can use the underscore character to verify if the progress towards the selected word is complete. No
        # underscores, means every letter has been guessed = win condition.
        if '_' not in current_word:
            return 'win'
        elif self.__mistake_counter == 6:
            return 'lose'
        else:
            return 'go'
