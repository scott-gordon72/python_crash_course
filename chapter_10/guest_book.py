filename = 'guest_book.txt'

while True:
    name = input("What is your name: ")
    print("Type 'q' to quit: ")

    if name != 'q':
        print(f"Welcome to our guest_book {name.title()}!")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()}\n")
    else:
        break
