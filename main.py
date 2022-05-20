import sys
import explanation
import day_1.name_generator as day1
import day_2.split_the_bill as day2
import day_3.treasure_island as day3
import day_4.rock_paper_scissors as day4
import day_5.password_generator as day5
import day_6.reeborgs_world_maze as day6
import day_7.hangman as day7
import day_8.ceasar_cipher as day8


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
    expl = explanation.Explanation('Welcome to the 100 days of code challenge. This is the main page where you can '
                                   'try the challenges. Every challenge has a \'challenge_explanation\' function '
                                   'which gives you details about the goal of the challenge.', 0)
    expl.print_explanation()
    print('\nThese days have been completed so far:\n')

    # The 'available_days' dictionary contains the following information:
    # KEY: day name, e.g. Day 1
    # TITLE: challenge title, e.g. Band name generator
    # In this for loop we print all items in the 'available_days' dictionary. 
    for day_num, desc in available_days.items():
        print('', day_num, desc, sep=' - ', end='\n')
    try:
        # The user enters a day (number) for which he wants to see more details. 
        # The value gets validated, if it's not valid, the program will end. 
        day_choice = int(input('\nPlease enter a number for which day you want to explore (day 1 to day 8 are '
                               'available at the moment): '))
        if day_choice < 0 or day_choice > 8:
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
    elif day_param == 'day2':
        bill_no_tip = float(input('What is the bill amount?\n'))
        tip_percentage = int(input('How much percent do you want to tip? (10, 12 or 15)\n'))
        num_diners = int(input('Among how many people do you want to split the bill?\n'))
        program = day2.Bill(bill_no_tip, tip_percentage)
        print(program.split(num_diners))
        sys.exit('Run completed.')
    elif day_param == 'day3':
        program = day3.TreasureIsland()
        program.play()
        sys.exit('Run completed.')
    elif day_param == 'day4':
        program = day4.RockPaperScissors()
        program.play()
        sys.exit('Run completed.')
    elif day_param == 'day5':
        program = day5.RandomPassword()
        print(program.generate_password())
        sys.exit('Run completed.')
    elif day_param == 'day6':
        print('This day can not be tested here.')
        sys.exit('Run completed.')
    elif day_param == 'day7':
        program = day7.Game()
        program.play()
        sys.exit('Run completed.')
    elif day_param == 'day8':
        try:
            action = input('Do you want to encrypt or decrypt? e or d: ')
            message = input('Provide a message:\n')
            key = int(input('Enter the key: '))
            if action == 'e':
                decrypt = False
            else:
                decrypt = True
            print(day8.encrypt(message, key, decrypt=decrypt))
            if action != 'e' and action != 'd':
                raise ValueError
        except ValueError as e:
            print('Please provide correct values.')
            print(e.__str__())
        sys.exit('Run completed.')


available_days = {
    'Day 1': 'Band name generator',
    'Day 2': 'Split the bill',
    'Day 3': 'Find the treasure',
    'Day 4': 'Rock, paper, scissors',
    'Day 5': 'Password generator',
    'Day 6': 'Reeborg\'s World - Maze',
    'Day 7': 'Hangman',
    'Day 8': 'Caesar Cipher',
}

run_it, chosen_day = print_welcome_message()

if run_it == 'Y':
    run_the_program(chosen_day)
else:
    run_it, day = print_welcome_message()
