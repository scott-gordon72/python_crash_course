rivers_in_usa = {'missouri': 'united states',
                 'mississippi': 'united states', 'yukon': 'united states'}

for river, country in rivers_in_usa.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nEach river included in the dictionary:")
for river in rivers_in_usa.keys():
    print(river)

print("\nEach country included in the dictionary:")
for country in rivers_in_usa.values():
    print(country)
