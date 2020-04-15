favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

favorite_languages_poll = [
    'jen', 'edward', 'jimmy', 'stu', 'fran', 'vinny', 'jon', 'sara'
]

for name in favorite_languages_poll:
    if name in favorite_languages.keys():
        print(f"{name}, thank you for responding to our poll!")
    else:
        print(f"{name}, we invite you to take our poll.")
