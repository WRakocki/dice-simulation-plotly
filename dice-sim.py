from random import randint

class Die():
    """Class representing one game dice"""

    def __init__(self, num_sides=6):
        """Making the assumption that dice has form of a cube"""
        self.num_sides = num_sides

    def roll(self):
        """Returns values from 1 to number of dice sides"""
        return randint(1, self.num_sides)