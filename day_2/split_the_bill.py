import sys
import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 2 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: String
    """
    expl_text = 'The second day was filled with dollar signs. This program splits the bill for you (including the tip '\
                'percentage) and your friends. Bien provecho!'
    expl = explanation.Explanation(expl_text, 1)
    expl.print_explanation()


class Bill:
    """
    Create an object of the Bill class. The Bill class can be used to split the bill between a number of people. It
    automatically adds the tip percentage that has been chosen.
    """
    def __init__(self, bill_no_tip: float, tip_percentage: int) -> None:
        """
        Inits the Bill class.
        :param bill_no_tip:
        :type bill_no_tip: float
        :param tip_percentage: The percentage to add to the bill (10, 12 or 15).
        :type tip_percentage: int
        """
        self.__bill_no_tip = bill_no_tip
        self.__tip_percentage = tip_percentage

    def split(self, num_diners: int) -> float:
        """
        Adds the tip percentage and splits the bill between a number of people.
        :param num_diners: Number of people among whom the bill must be split.
        :return: The dollar amount that every person has to pay.
        :rtype: float
        """
        try:
            # Any option other than 10, 12 or 15 will end up in a ValueError.
            if self.__tip_percentage != 10 and self.__tip_percentage != 12 and self.__tip_percentage != 15:
                raise ValueError
        except ValueError:
            print('Incorrect tip percentage value entered, the program will die now.')
            sys.exit('I died.')
        # Calculating the total bill, adding the tip percentage to the bill_no_tip value.
        total_bill = (self.__bill_no_tip / 100) * (100 + self.__tip_percentage)
        try:
            # Using the function argument to divide the bill into equal parts and return the value per person.
            bill_per_person = round(total_bill / num_diners, 2)
        except ZeroDivisionError:
            print('Did you, by chance ofcourse, enter 0 when asked how many people will split the bill? Don\'t you '
                  'have any friends?')
            sys.exit('Bye!')
        return bill_per_person
