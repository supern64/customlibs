# Range library
# For calculating if numbers are in a certain range

import random

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def is_in_range(self, number):
        if number >= self.start and number <= self.end:
            return True
        else:
            return False
    def random(self):
        return random.randint(self.start, self.end)