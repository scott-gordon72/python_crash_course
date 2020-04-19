filename = 'chapter_10/text_files/learning_python.txt'

# Read the entire file
with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)
print("\n")

# Loop over the file object
with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())

print("\n")

# Store items in a list and work with them outside the with block
with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.rstrip())

print("\n")
