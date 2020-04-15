pizza = {
    'crust': ['thick', 'thin', 'stuffed'],
    'toppings': ['mushrooms', 'extra cheese', 'bacon', 'hamburg', 'onion',
    'olives', 'pepperoni',],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the folowing toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
