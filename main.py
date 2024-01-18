import secrets
import string
chars = [string.punctuation, string.ascii_uppercase, string.ascii_lowercase, string.digits] # Different characters that can be used
config = [int(input('Would you like special characters? (1/0)\n')), int(input('Would you like capital letters? (1/0)\n')), int(input('Would you like lowercase letters? (1/0)\n')), int(input('Would you like numbers? (1/0)\n')), int(input('What length would you like your password(s) to be?\n')), int(input('How may passwords would you like to generate?\n'))]
chars = list(filter(lambda x: config[chars.index(x)], chars)) # Filters out options from the list that the user doesn't want.
try:
    for i in range(config[5]):
        password = ''
        for i in range(config[4]):
            password += secrets.choice(secrets.choice(chars))
        print(f'\n{password}')
except:
    print('Something went wrong. You may want to choose different settings.')
