filename = 'chapter_10/text_files/the_works_of_edgar_allan_poe.txt'

with open(filename) as f:
    contents = f.read()

print(contents.lower().count('the '))
