def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, this file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['chapter_10/text_files/alice.txt', 'chapter_10/text_files/siddhartha.txt',
             'chapter_10/text_files/moby_dick.txt', 'chapter_10/text_files/little_women.txt']
for filename in filenames:
    count_words(filename)
