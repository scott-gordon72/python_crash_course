person_i_know = {
    'first_name': 'connor',
    'last_name': 'gordon',
    'age': 18,
    'city': 'leominster',
}

person_i_want_to_know = {
    'first_name': 'elon',
    'last_name': 'musk',
    'age': 48,
    'city': 'pretoria',
}

person_i_never_want_to_know = {
    'first_name': 'donald',
    'last_name': 'trump',
    'age': 73,
    'city': 'queens',
}

people = [person_i_know, person_i_want_to_know, person_i_never_want_to_know]
for person in people:
    print(f"\nFirst name: {person['first_name'].title()}"
          f"\nLast name: {person['last_name'].title()}"
          f"\nAge: {person['age']}"
          f"\nCity: {person['city'].title()}"
          )
