dream_vacations = []
vacation = ""
while vacation != 'q':
    vacation = input(
        f"If you could visit one place in the world, where would you go?")
    if vacation != 'q':
        dream_vacations.append(vacation)

print("Results of the poll are: ")
if dream_vacations:
    for dream_vacation in dream_vacations:
        print(f"\t{dream_vacation}")
