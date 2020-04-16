"""Module for dice rolling using Die class"""
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
