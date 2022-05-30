import sys
import explanation
import object_manager.object_manager as om
import day_1.name_generator as day1
import day_2.split_the_bill as day2
import day_3.treasure_island as day3
import day_4.rock_paper_scissors as day4
import day_5.password_generator as day5
import day_6.reeborgs_world_maze as day6
import day_7.hangman as day7
import day_8.ceasar_cipher as day8


def print_main_menu() -> None:
    """
    Print the welcome message. Give the user the ability to choose a specific project (day).
    :return: None
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
        day_choice = input('\nPlease enter a number for which day you want to explore (day 1 to day 8 are '
                           'available at the moment). Enter q to quit. ')
        if day_choice == 'q':
            sys.exit('Thank you for checking out this awesome project. Come back soon!')
        day_choice = int(day_choice)
        if day_choice < 0 or day_choice > 8:
            raise ValueError
    except ValueError:
        sys.exit('An invalid option has been entered, why would you do such a monstrous thing.')

    run_the_program(day_choice)


def run_the_program(day_param):
    """
    Create an object of the specified day. Use this object to start the associated program.
    :param day_param: String
    :return: None
    """
    day_param = str(day_param)
    print('\nDay {}, what a lovely choice. This is the challenge explanation:'.format(day_param))

    # The day is formatted: the word day is added in front of the chosen day.
    fabricated_day = 'day' + day_param

    # Every challenge has a .challenge_explanation() function which prints more details.
    explanation_function = fabricated_day + '.print_challenge_explanation()'

    # Eval allows us to 'run' an ordinary string as a function.
    eval(explanation_function)

    # After showing the explanation, does the user want to run the project?
    run = ''
    while run != 'y' and run != 'n':
        run = input('Does this explanation trigger your interests? Do you want to run the project? (y or n)')

    if run == 'n':
        print_main_menu()
    else:
        if day_param == '1':
            result = object_manager.run_day_01()
            print(result)
        elif day_param == '2':
            result = object_manager.run_day_02()
            print(result)
        elif day_param == '3':
            program = day3.TreasureIsland()
            program.play()
        elif day_param == '4':
            program = day4.RockPaperScissors()
            program.play()
        elif day_param == '5':
            program = day5.RandomPassword()
            print(program.generate_password())
        elif day_param == '6':
            print('This day can not be tested here.')
        elif day_param == '7':
            program = day7.Game()
            program.play()
        elif day_param == '8':
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

        # A choice has to be made, quit the program or continue (return to the welcome page).
        print('\n... run completed.\n')
        rerun = ''
        while rerun != 'q' and rerun != 'c':
            rerun = input('Enter q to quit, c to continue to the main menu and run a new project.')
        if rerun == 'c':
            print_main_menu()
        else:
            sys.exit('Thank you for checking out this awesome project. Come back soon!')


object_manager = om.ObjectManager()
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
print_main_menu()

