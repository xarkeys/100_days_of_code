import sys

total_bill = float(input('What was the total bill? '))

try:
    tip_percent = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
    if tip_percent != 10 and tip_percent != 12 and tip_percent != 15:
        raise ValueError
except ValueError:
    print('Incorrect tip percentage value entered, the program will die now.')
    # I tried quit() and exit() but they gave an error in IDLE, sys.exit (with the
    # import sys combined does not exit IDLE. 
    sys.exit('I died.')

total_bill = (total_bill / 100) * (100 + tip_percent)
people_split = int(input('How many people to split the bill? '))
print('Each person should pay: ${}'.format(round(total_bill/people_split, 2)))
