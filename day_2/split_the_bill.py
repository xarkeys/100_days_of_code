import sys


def challenge_explanation():
    """
    Request an explanation of the DAY 2 challenge.
    :return: A detailed explanation on what the program does.
    :rtype: String
    """
    explanation = '''
    -------------------- DAY02 --------------------
    - Title: Split the bill                       -
    - The second day was filled with dollar       -
    - signs. This program splits the bill for you -
    - (including the tip percentage) and your     -
    - friends. Bien provecho!                     -
    -----------------------------------------------
    '''

    return explanation 


def split_the_bill():
    '''
    Main program.
    '''
    try:
        total_bill = float(input('What was the total bill? '))
        tip_percent = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
        # Any option other than 10, 12 or 15 will end up in a ValueError.
        if tip_percent != 10 and tip_percent != 12 and tip_percent != 15:
            raise ValueError
    except ValueError:
        print('Incorrect tip percentage value entered, the program will die now.')
        # I tried quit() and exit() but they gave an error in IDLE, sys.exit (with the
        # import sys combined does not exit IDLE. 
        sys.exit('I died.')

    total_bill = (total_bill / 100) * (100 + tip_percent)
    try:
        people_split = int(input('How many people to split the bill? '))
        print('Each person should pay: ${}'.format(round(total_bill/people_split, 2)))
    except ZeroDivisionError:
        print('Did you, by chance ofcourse, enter 0 when asked how many people will split the bill? Don\'t you have any friends?')
        sys.exit('Bye!')
