filename = 'poll_response.txt'
while True:
    answer = input("Why do you like programming so much?: ")
    print(f"Type 'q' to quit ")
    if answer != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(f"{answer}\n")
    else:
        break
