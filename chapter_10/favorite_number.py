import json

filename = 'numbers.json'

number = int(input("What's your favorite number?"))

with open(filename, 'w') as f:
    json.dump(number, f)
