import secrets
import string
chars = [string.punctuation, string.ascii_uppercase, string.ascii_lowercase, string.digits] # Different characters that can be used
length = int(input('What length of password would you like?\n'))
toggle_config = [int(input('Would you like special characters? (1/0)\n')), int(input('Would you like capital letters? (1/0)\n')), int(input('Would you like lowercase letters? (1/0)\n')), int(input('Would you like numbers? (1/0)\n'))]
chars = list(filter(lambda x: toggle_config[chars.index(x)], chars)) # Filters out options from the list that the user doesn't want.
try:
    password = ''
    for i in range(length):
        password += secrets.choice(secrets.choice(chars))
    print(password)
except:
    print('Something went wrong. You might want to choose different settings.')
