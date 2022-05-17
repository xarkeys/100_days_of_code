import sys
import day_1.name_generator as day1


def print_welcome_message():
    """
    This function prints the welcome message which gives the user some choices:
    - Which day do you want to explore, which shows details about the challenge?
    - Do you want to run the program?
    :returns: tuple (result1, result2)
        WHERE
        str result1 is the chosen day by the user.
        str result2 is the chosen action by the user (Y or N).
    """

    print('''
    -------------------- MAIN --------------------
    - Welcome to the 100 days of code challenge. -
    - This is the main page where you can try    -
    - the challenges. Every challenge has        -
    - a \'challenge_explanation\' function which   -
    - gives you details about the goal of the    -
    - challenge.                                 -
    ----------------------------------------------
    ''')

    print('These days have been completed so far:\n')

    # The 'available_days' dictionary contains the following information:
    # KEY: day name, e.g. Day 1
    # TITLE: challenge title, e.g. Band name generator
    # In this for loop we print all items in the 'available_days' dictionary. 
    for day_num, desc in available_days.items():
        print('', day_num, desc, sep=' - ', end='\n')
    try:
        # The user enters a day (number) for which he wants to see more details. 
        # The value gets validated, if it's not valid, the program will end. 
        day_choice = int(input('\nPlease enter a number for which day you want to explore (day 1 to day 5 are '
                               'available at the moment): '))
        if day_choice < 0 or day_choice > 5:
            raise ValueError
    except ValueError:
        sys.exit('An invalid option has been entered, why would you do such a monstrous thing.')

    print('\nDay {}, what a lovely choice. This is the challenge explanation:'.format(day_choice))

    # We format the day variable based on the word day and the user's input (chosen number).
    fabricated_day = 'day' + str(day_choice)

    # Every challenge has a .challenge_explanation() function which prints more details. 
    explanation_function = fabricated_day + '.challenge_explanation()'

    # Eval allows us to 'run' an ordinary string as a function. 
    eval(explanation_function)

    try:
        run_it_input = input('Would you like to run this program? (Y or N) ')
    except ValueError:
        sys.exit('Invalid option selected, shutting down...')

    # We return the two choices the user made, the run_it (Y or N) and the chosen day (day + number).
    return run_it_input, fabricated_day


def run_the_program(day_param):
    """
    Create an object of the specified day. Use this object to start the associated program.
    :param day_param: String
    :return: None
    """

    if day_param == 'day1':
        city_name = input('What city did you grow up in?\n')
        hobby_name = input('What is your favourite hobby?\n')
        program = day1.BandName(city_name, hobby_name)
        print(program.get_band_name())
        sys.exit('Run completed.')
    # elif day == 'day2':
    #     day2.split_the_bill()
    #     sys.exit('Run completed.')
    # elif day == 'day3':
    #     treasure_island = day3.treasure_island()
    #     treasure_island.play_a_game()
    #     sys.exit('Run completed.')
    # elif day == 'day4':
    #     rock_paper_scissors = day4.rock_paper_scissors()
    #     print(rock_paper_scissors.play_a_game())
    #     sys.exit('Run completed.')
    # elif day == 'day5':
    #     random_password = day5.random_password()
    #     print(random_password.generate_password())
    #     sys.exit('Run completed.')


available_days = {
    'Day 1': 'Band name generator',
    'Day 2': 'Split the bill',
    'Day 3': 'Find the treasure',
    'Day 4': 'Rock, paper, scissors',
    'Day 5': 'Password generator',
}

run_it, chosen_day = print_welcome_message()

if run_it == 'Y':
    run_the_program(chosen_day)
else:
    run_it, day = print_welcome_message()
