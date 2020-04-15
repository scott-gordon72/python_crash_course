cities = {
    'leominster': {'country': 'united states',
                   'population': 40759,
                   'fact': 'the birthplace of johnny appleseed.'},
    'fitchburg': {'country': 'united states',
                  'population': 40318,
                  'fact': 'home to fitchburg state university.'},
    'worcester': {'country': 'united states',
                  'population': 181045,
                  'fact': 'nickname is wormtown.'},
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact'].capitalize()}")
