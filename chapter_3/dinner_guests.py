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

print(f"The number of guests invited: {len(guests)}")