from random import randint


class Die():
    """A class created to emulate a sided dice"""

    def __init__(self, sides=6):
        """Constructor to initiate the Die class"""
        self.sides = sides

    def roll_die(self):
        """Emulates the roll of the die"""
        dice_roll = randint(1, self.sides)
        return dice_roll


d6 = Die(6)
print(f"\nd6 six sided die rolls: ")
roll_1 = d6.roll_die()
print(roll_1)
roll_2 = d6.roll_die()
print(roll_2)
roll_3 = d6.roll_die()
print(roll_3)
roll_4 = d6.roll_die()
print(roll_4)
roll_5 = d6.roll_die()
print(roll_5)
roll_6 = d6.roll_die()
print(roll_6)

print(f"\nd10 ten sided die rolls: ")
d10 = Die(10)
roll_1 = d10.roll_die()
print(roll_1)
roll_2 = d10.roll_die()
print(roll_2)
roll_3 = d10.roll_die()
print(roll_3)
roll_4 = d10.roll_die()
print(roll_4)
roll_5 = d10.roll_die()
print(roll_5)
roll_6 = d10.roll_die()
print(roll_6)
roll_7 = d10.roll_die()
print(roll_7)
roll_8 = d10.roll_die()
print(roll_8)
roll_9 = d10.roll_die()
print(roll_9)
roll_10 = d10.roll_die()
print(roll_10)

print(f"\nd20 twenty sided die rolls: ")
d20 = Die(20)
roll_1 = d20.roll_die()
print(roll_1)
roll_2 = d20.roll_die()
print(roll_2)
roll_3 = d20.roll_die()
print(roll_3)
roll_4 = d20.roll_die()
print(roll_4)
roll_5 = d20.roll_die()
print(roll_5)
roll_6 = d20.roll_die()
print(roll_6)
roll_7 = d20.roll_die()
print(roll_7)
roll_8 = d20.roll_die()
print(roll_8)
roll_9 = d20.roll_die()
print(roll_9)
roll_10 = d20.roll_die()
print(roll_10)
