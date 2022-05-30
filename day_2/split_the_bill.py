import explanation


def print_challenge_explanation() -> None:
    """
    Request an explanation of the DAY 2 challenge.
    :return: None
    """
    expl_text = 'The second day was filled with dollar signs. This program splits the bill for you (including the tip '\
                'percentage) and your friends. Bien provecho!'
    expl = explanation.Explanation(expl_text, 2)
    expl.print_explanation()


class Bill:
    """
    Create an object of the Bill class. The Bill class can be used to split the bill between a number of people. It
    automatically adds the tip percentage that has been chosen.
    """
    def __init__(self, bill_no_tip: float, tip_percentage: int) -> None:
        """
        Inits the Bill class.
        :param bill_no_tip: The total amount on the bill without tip.
        :type bill_no_tip: float
        :param tip_percentage: The tip percentage to add to the bill (10, 12 or 15).
        :type tip_percentage: int
        """
        self.__bill_no_tip = bill_no_tip
        self.__tip_percentage = tip_percentage

    def split(self, num_diners: int) -> float | str:
        """
        Adds the tip percentage and splits the bill between a number of people.
        :param num_diners: Number of people among whom the bill must be split.
        :type num_diners: int
        :return:
            Normal execution: The dollar amount that every person has to pay.
            Exception occurred: None.
        :rtype: float, None
        :raises:
            ValueError: if self.__tip_percentage is not 10, 12 or 15
            ZeroDivisionError: if num_diners is equal to 0
        """
        try:
            # Any option other than 10, 12 or 15 will end up in a ValueError.
            if self.__tip_percentage != 10 and self.__tip_percentage != 12 and self.__tip_percentage != 15:
                raise ValueError
        except ValueError:
            return 'Incorrect tip percentage value entered.'
        # Calculating the total bill, adding the tip percentage to the bill_no_tip value.
        total_bill = (self.__bill_no_tip / 100) * (100 + self.__tip_percentage)
        try:
            # Using the function argument to divide the bill into equal parts and return the value per person.
            bill_per_person = round(total_bill / num_diners, 2)
        except ZeroDivisionError:
            return 'Did you, by chance ofcourse, enter 0 when asked how many people will split the bill? Don\'t you ' \
                   'have any friends? '
        return bill_per_person
