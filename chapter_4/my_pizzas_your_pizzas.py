pizzas = ['pepperoni', 'cheese', 'hamburg', 'hawaiian', 'greek', 'meat']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('bacon & olive')
friend_pizzas.append('brocolli & cauliflower')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)