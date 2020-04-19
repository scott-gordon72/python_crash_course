
try:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the socond number: "))
except ValueError:
    print("You must enter a numbers and not text values.")
else:
    result = number_1 + number_2
    print(f"The results of your addition are: {result}")
