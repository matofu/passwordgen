import secrets
import string
possible_chars = [string.punctuation, string.ascii_uppercase, string.ascii_lowercase, string.digits] # Different characters that can be used
config = [input('Would you like to allow special characters? (1/0)\n'), input('Would you like to allow capital letters? (1/0)\n'), input('Would you like to allow lowercase letters? (1/0)\n'), input('Would you like to allow numbers? (1/0)\n'), input('What length would you like your password(s) to be? (integer)\n'), input('How may passwords would you like to generate? (integer)\n')]
try:
    possible_chars = list(filter(lambda x: int(config[possible_chars.index(x)]), possible_chars)) # Filters out options from the list that the user doesn't want.
    for i in range(int(config[5])):
        password = ''
        for i in range(int(config[4])):
            password += secrets.choice(secrets.choice(possible_chars))
        print(f'\n{password}')
except:
    print('\nSomething went wrong. You may want to choose different settings.')
