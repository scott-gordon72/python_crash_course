filename = 'chapter_10/text_files/learning_python.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    # Get rid of newline, then replace python with c.
    line = line.rstrip()
    print(line.replace('python', 'c'))

print("\n")
