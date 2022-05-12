def challenge_explanation():
    '''
    This function returns an intro text to the challenge.
    '''
    explanation = '''
    -------------------- DAY01 --------------------
    - Title: Band name generator                  -
    - On day one a Band name generator was        -
    - created.The program asks two questions.     -
    - Based on the user's input you will receive  -
    - a bandname. How original is that!           -
    -----------------------------------------------
    '''

    return explanation 


def name_generator():
    '''
    Main program.
    '''
    print('Welcome to the Band Name Generator.')
    city_name = input('What\'s the name of the city you grew up in? ')
    hobby_name = input('What\'s your main hobby? ')
    band_name = hobby_name + 'ing' + ' ' + city_name + ' ' + '5000'
    print('You band name could be: {}'.format(band_name))

