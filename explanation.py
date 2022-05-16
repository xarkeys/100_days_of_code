def add_line_end(space_to_fill: int) -> str:
    """
    Create a string consisting of whitespace and a '-' character. This string can be used to add to the end of
    one line in the explanation.
    :param space_to_fill: The amount of characters we are short of the maximum line length.
    :type space_to_fill: int
    :return: The whitespaces and - symbol to add at the back of a line in an explanation.
    :rtype: str
    """
    line_ending = ''
    for i in range(space_to_fill - 1):
        line_ending += ' '
    line_ending += '-'
    return line_ending


class Explanation:
    """
    The explanation class can be used to format an explanation for a new program (from the 100 days of code challenge).
    This class makes sure that every explanation has the same sizing in all the 100 challenges.
    """
    def __init__(self, expl_text: str, day: int) -> None:
        """
        Inits the Explanation class.
        :param expl_text: The explanation for a specific challenge.
        :type expl_text: str
        :param day: The day that accompanied the challenge.
        :type day: int
        """
        self.__expl_text = expl_text
        self.__day = day
        # A line in an explanation has a width of 47, including ' and whitespace. So the maximum number of characters
        # we will allow in one line is 47 - 10. 2 for the ' symbols, 2 for whitespaces and 6 extra for keeping it clean.
        self.__max_text_width = 37
        self.__max_line_width = 47
        self.__expl_formatted = []

    def __format_explanation(self) -> None:
        """
        Create an explanation that dynamically adds the given string and adds the standard formatting.
        :return: None
        """
        # If the given day is below 10, we add an extra 0 in front. If the given day is 10 or above we just add
        # the day number.
        if self.__day < 10:
            self.__expl_formatted = [f'-------------------- DAY0{self.__day} --------------------']
        else:
            self.__expl_formatted = [f'-------------------- DAY{self.__day} --------------------']

        # The entire text is split into a list of strings, every word is an element.
        expl = self.__expl_text.split(' ')
        one_line = '- '
        counter = len(one_line)

        # An iteration over every element of the expl list. We count the total line length and check if it's still
        # below the maximum text width limit. If it is, we just add the word and a whitespace. If it's not we start
        # a new line and add the current word in the iteration.
        for word in expl:
            counter += len(word)
            if counter < self.__max_text_width:
                one_line += word + ' '
            else:
                # The one_line function is used to add the line ending.
                one_line += add_line_end(self.__max_line_width - len(one_line))
                self.__expl_formatted.append(one_line)
                one_line = '- ' + word + ' '
                counter = len(one_line)
        # The one_line function is used to add the line ending.
        one_line += add_line_end(self.__max_line_width - len(one_line))
        self.__expl_formatted.append(one_line)
        # After all the lines have been added, the bottom line is added.
        self.__expl_formatted.append('-----------------------------------------------')

    def print_explanation(self) -> None:
        """
        Print the formatted explanation text, line per line.
        :return: None
        """
        self.__format_explanation()
        for line in self.__expl_formatted:
            print(line)


test = Explanation('this is a test string bla bla test hallo een twee drie vier hoedje van papier lolsnorretjes '
                   'ditadfads ahqeqr ds;fad langere tekst feest lololsa fsadfasdfa,adsf kadsf', 2)
print(test.print_explanation())
