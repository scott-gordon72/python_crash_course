filenames = ['chapter_10/text_files/cats.txt',
             'chapter_10/text_files/dogs.txt']

for filename in filenames:
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        print(line.rstrip())
