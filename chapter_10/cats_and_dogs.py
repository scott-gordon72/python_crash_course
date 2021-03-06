filenames = ['chapter_10/text_files/cats.txt',
             'chapter_10/text_files/dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            lines = f.read()
            print(lines)

    except FileNotFoundError:
        print(" Sorry, I can't find that file.")