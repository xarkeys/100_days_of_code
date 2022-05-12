import sys
import day1
import day2
import day3
import day4
import day5

def print_welcome_message():
    '''
    This function prints the welcome message which gives the user some choices:
    - which day do you want to explore, which shows details about the challenge
    - do you want to run the program
    
    The function returns the choice Y or N wether the user wants to run the program
    and the chosen day. 
    '''
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
    for day, desc in available_days.items():
        print('', day, desc, sep=' - ', end='\n')
    try:
        # The user enters a day (number) for which he want's to see more details. 
        day_choice = int(input('\nPlease enter a number for which day you want to explore (day 1 to day 5 are available at the moment): '))
        if day_choice < 0 or day_choice > 5: raise ValueError
    except ValueError:
        sys.exit('An invalid option has been entered, why would you do such a monstrous thing.')

    print('\nDay {}, what a lovely choice. This is the challenge explanation:'.format(day_choice))
    # We format the day variable based on the word day and the user's input (chosen number).
    day = 'day' + str(day_choice)
    # Every challenge has a .challenge_explanation() function which prints more details. 
    explanation_function = day + '.challenge_explanation()'
    # Eval allows us to 'run' an ordinary string as a function. 
    print(eval(explanation_function))
    try:
        run_it = input('Would you like to run this program? (Y or N) ')
    except ValueError:
        sys.exit('Invalid option selected, shutting down...')
    
    # We return the two choices the user made, the run_it (Y or N) and the chosen day (day + number).
    return run_it, day

def run_the_program(day):
    '''
    This function will start the specific challenge of the chosen day.
    '''
    if day == 'day1':
        day1.name_generator()
        sys.exit('Run completed.')
    elif day == 'day2':
        day2.split_the_bill()
        sys.exit('Run completed.')
    elif day == 'day3':
        day3.treasure_island()
        sys.exit('Run completed.')
    elif day == 'day4':
        day4.rock_paper_scissors()
        sys.exit('Run completed.')
    elif day == 'day5':
        day5.generate_random_password()
        sys.exit('Run completed.')

available_days = {
    'Day 1':'Band name generator',
    'Day 2':'Split the bill',
    'Day 3':'Find the treasure',
    'Day 4':'Rock, paper, scissors',
    'Day 5':'Password generator'}

run_it, day = print_welcome_message()

if run_it == 'Y':
    run_the_program(day)
else:
    run_it, day = print_welcome_message()

