import random
import string
chars = [list(string.punctuation), list(string.ascii_uppercase), list(string.ascii_lowercase), list(string.digits)] # Different characters that can be used
length = int(input('What length of password would you like?\n'))
toggle_config = [int(input('Would you like special characters? (1/0)\n')), int(input('Would you like capital letters? (1/0)\n')), int(input('Would you like lowercase letters? (1/0)\n')), int(input('Would you like numbers? (1/0)\n'))]
chars_buffer = chars.copy() # Copies the list of characters to make sure the right indexes are being removed
chars = list(filter(lambda x: toggle_config[chars_buffer.index(x)], chars)) # Filters out options from the list that the user doesn't want.
try:
    password = ''
    for i in range(length):
        password += random.choice(random.choice(chars))
    print(f'Your password is {password}')
except:
    print('Something went wrong. You might want to choose different settings.')
