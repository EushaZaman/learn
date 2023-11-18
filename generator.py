import random
import string





#password = random.choice(valid_password_characters)


def generate_password():
    password_length = random.randrange(10, 21)
    valid_password_characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join([random.choice(valid_password_characters) for _ in range(password_length)])
    return password

def generate_minecraft_seed(length):
    valid_seed_characters = string.ascii_letters + string.digits
    seed = ''.join([random.choice(valid_seed_characters) for _ in range(length)])
    return seed



'''
for _ in range(PASSWORD_LENGTH):
    password += random.choice(valid_password_characters)
'''


