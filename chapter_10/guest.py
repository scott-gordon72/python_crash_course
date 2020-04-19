name = input("Enter your name: ")

filename = 'chapter_10/text_files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name)
