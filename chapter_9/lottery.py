from random import choice
"""A random lottery ticket genertator using ranoms choice() method."""

numbers_and_letters = ('A', 'Z', 'D', 'R', 'V', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
chosen = []

for i in range(4):
    lucky_choice = choice(numbers_and_letters)
    chosen.append(lucky_choice)

print(f"Any ticket matching {chosen} wins a prize.")
