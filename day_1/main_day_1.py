def challenge_explanation():
    """
    Request an explanation of this day's challenge: day 1.
    :return: A detailed explanation on what the program does.
    :rtype: String
    """

    explanation = '''
    -------------------- DAY01 --------------------
    - Title: Band name generator                  -
    - On day one a Band name generator was        -
    - created.The program asks two questions.     -
    - Based on the user's input you will receive  -
    - a band-name. How original is that!          -
    -----------------------------------------------
    '''

    return explanation


def name_generator():
    """
    Generate a name based on the user's input.
    :return: None
    """
    print('Welcome to the Band Name Generator.')
    city_name = input('What\'s the name of the city you grew up in? ')
    hobby_name = input('What\'s your main hobby? ')
    band_name = hobby_name + 'ing' + ' ' + city_name + ' ' + '5000'
    print('You band name could be: {}'.format(band_name))
