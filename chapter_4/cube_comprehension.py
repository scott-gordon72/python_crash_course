cubes_list = []
for i in range(1, 11):
    cubes_list.append(i)

cubes_list_comprehension = [cube ** 3 for cube in cubes_list]
print(cubes_list_comprehension)