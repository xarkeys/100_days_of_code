import explanation


def challenge_explanation() -> None:
    """
    Request an explanation of the DAY 1 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: String
    """
    expl_text = 'On day one a Band name generator was created. The program asks two questions. Based on the user\'s '\
                'input you will receive a band name. How original is that!'
    expl = explanation.Explanation(expl_text, 1)
    expl.print_explanation()


class BandName:
    """
    Create an object of the BandName class. The class can be used to generate a band name based
    on a city and hobby.
    """
    def __init__(self, city_name: str, hobby_name: str) -> None:
        """
        Inits the BandName class.
        :param city_name: The name of the city where the user lives.
        :type city_name: str
        :param hobby_name: The hobby of the user.
        :type hobby_name: str
        """
        self.__city_name = city_name
        self.__hobby_name = hobby_name
        self.__band_name = ''

    def get_band_name(self) -> str:
        """
        Create a band name, using the objects __city_name, __hobby_name vars and the String 5000.
        :return: The generated band name.
        :rtype: str
        """
        self.__band_name = self.__hobby_name + self.__city_name + 'ers' + ' 5000'
        return 'We generated the following band name for you: ' + self.__band_name
