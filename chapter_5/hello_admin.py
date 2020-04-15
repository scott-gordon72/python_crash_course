usernames = ['admin', 'scott123', 'lisa1337', 'connor2002', 'alf']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a staus report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")