count = 0
total = 0
people = int(input("How many people are buying tickets? "))
while count < people:
    age = int(input("Please enter age: "))
    if age < 3:
        ticket = 0
    elif age <= 12:
        ticket = 10
    elif age > 12:
        ticket = 15
    count += 1
    total += ticket
    print(f"Your ticket price is ${ticket}")
print(f"The total ticket cost is: ${total}")
