trigger = {
    'pet_type': 'horse',
    'owner_name': 'frank',
}

larry = {
    'pet_type': 'parrot',
    'owner_name': 'sherry',
}

beardie = {
    'pet_type': 'bearded_dragon',
    'owner_name': 'connor',
}

tigger = {
    'pet_type': 'cat',
    'owner_name': 'scott',
}

julie = {
    'pet_type': 'parakeet',
    'owner_name': 'lisa',
}

pets = [trigger, larry, beardie, tigger, julie]

for pet_names in pets:
    for info in pet_names.items():
        print(f"\t{info}")