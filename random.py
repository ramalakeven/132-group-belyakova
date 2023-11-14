import random
import json

def generate_random_char():
    return chr(random.randint(33, 126))

array = [[generate_random_char() for _ in range(10)] for _ in range(10)]

with open('random_chars.json', 'w') as file:
    json.dump(array, file)