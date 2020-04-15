current_users = ['admin', 'scott123', 'lisa1337', 'connor2002', 'alf']

new_users = ['alf', 'george', 'frank', 'scott123', 'paris']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(
            f"Sorry {new_user} has been taken please choose another username.")
    else:
        print(f"{new_user} is available")
