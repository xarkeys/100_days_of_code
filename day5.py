import random
import sys

def shuffle_word(word):
    '''
    Shuffle a string. 

    This function returns the scrambled version of the *word* parameter. The function uses the
    'shuffle' function from the 'random' module. 
    '''
    word = list(word)
    random.shuffle(word)
    print(word)
    return ''.join(word)


print('Welcome to the PyPassword Generator!')
try:
    # We ask the user for three values, all three of them must be below 21 and above -1. If not
    # a 'ValueError' will be raised which closes the program. 
    num_letters = int(input('How many letters would you like in your password? (max 20)\n'))
    if num_letters > 20 or num_letters < 0: raise ValueError
    num_symbols = int(input('How many symbols would you like in your password? (max 20)\n'))
    if num_symbols > 20 or num_symbols < 0: raise ValueError
    num_numbers = int(input('How many numbers would you like in your password? (max 20)\n'))
    if num_numbers > 20 or num_symbols < 0: raise ValueError
except ValueError:
    sys.exit('An invalid entry has been made. Shutdown unavoidable...')

# list_of_symbols will be used as a feed for random symbols
list_of_symbols = ['[',']','{','}','!','@','#','$']
generated_password = ''

# ASCII letters (lower) are 97 to 122
# ASCII letters (upper) are 65 to 90
# In this 
for letter in range(num_letters):
    upper_or_lower = random.randint(1,2)
    if upper_or_lower == 1:
        random_int = random.randint(97,122)
        generated_password += chr(random_int)
    else:
        random_int = random.randint(65,90)
        generated_password += chr(random_int)


for symbol in range(num_symbols):
    random_int = random.randint(0,num_symbols - 1)
    generated_password += list_of_symbols[random_int]

for number in range(num_numbers):
    generated_password += str(random.randint(0,9))

generated_password = shuffle_word(generated_password)

print('Here is your password: {}'.format(generated_password))