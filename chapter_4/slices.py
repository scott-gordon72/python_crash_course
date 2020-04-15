import math
cubes_list = []
for i in range(1, 11):
    cubes_list.append(i)

cubes_list_comprehension = [cube ** 3 for cube in cubes_list]
print(cubes_list_comprehension)
print(
    f"The first three items in the list of cubes are:{cubes_list_comprehension[:3]}")
cube_middle = int((len(cubes_list_comprehension) / 2) - 1)
print(cube_middle)
print(
    f"The items from the middle of the cube list are: {cubes_list_comprehension[cube_middle-1:cube_middle+2]}")
print(f"The last three items in a list are: {cubes_list_comprehension[-3:]}")
