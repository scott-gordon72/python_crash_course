from admin import Admin


scott = Admin('scott', 'gordon', 'p4wn574r',
              '5c077_60rd0n@gmail.com', 'united states')
scott.privileges.show_privileges()

print(f"\nAdding {scott.first_name}'s privileges")
scott_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    'can make you jealous of his code'
]
scott.privileges.privileges = scott_privileges
scott.privileges.show_privileges()
