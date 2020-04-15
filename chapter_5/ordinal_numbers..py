lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in lst:
    if index == 1:
        print(str(index) + "st")
    elif index == 2:
        print(str(index) + "nd")
    elif index == 3:
        print(str(index) + "rd")
    else:
        print(str(index) + "th")
