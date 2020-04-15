sandwich_orders = ['tuna', 'ham and cheese',
                   'steak and cheese', 'bologna', 'peanut butter and jelly']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nHere are the finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich")
