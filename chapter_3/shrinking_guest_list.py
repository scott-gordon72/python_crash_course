guests = ['einstein', 'tesla', 'musk', 'gates', 'branson']

print(f"{guests[0]}, I would like to cordially invite you to dine with me.")
print(f"{guests[1]}, I would like to cordially invite you to dine with me.")
print(f"{guests[2]}, I would like to cordially invite you to dine with me.")
print(f"{guests[3]}, I would like to cordially invite you to dine with me.")
print(f"{guests[4]}, I would like to cordially invite you to dine with me.")
print("I found a bigger dinner table and will be inviting more guests!")

guests.insert(0,"angeloo")
guests.insert(3, "mr. robot")
guests.append("darth vader")
print(f"{guests[0]}, I would like to cordially invite you to dine with me.")
print(f"{guests[1]}, I would like to cordially invite you to dine with me.")
print(f"{guests[2]}, I would like to cordially invite you to dine with me.")
print(f"{guests[3]}, I would like to cordially invite you to dine with me.")
print(f"{guests[4]}, I would like to cordially invite you to dine with me.")
print(f"{guests[5]}, I would like to cordially invite you to dine with me.")
print(f"{guests[6]}, I would like to cordially invite you to dine with me.")
print(f"{guests[7]}, I would like to cordially invite you to dine with me.")
print("My table will not be in until next week, I now can only invite two of you, my apologies")

popped_guest = guests.pop()
print(f"{popped_guest} I am sorry but I cannot invite you to dinner...")
popped_guest = guests.pop()
print(f"{popped_guest} I am sorry but I cannot invite you to dinner...")
popped_guest = guests.pop()
print(f"{popped_guest} I am sorry but I cannot invite you to dinner...")
popped_guest = guests.pop()
print(f"{popped_guest} I am sorry but I cannot invite you to dinner...")
popped_guest = guests.pop()
print(f"{popped_guest} I am sorry but I cannot invite you to dinner...")
popped_guest = guests.pop()
print(f"{popped_guest} I am sorry but I cannot invite you to dinner...")
remaining_guest = guests[0]
print(f"{remaining_guest} you are still invited")
remaining_guest = guests[1]
print(f"{remaining_guest} you are still invited")