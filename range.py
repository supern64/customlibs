# Range library
# For calculating hitboxes

import random


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_in_range(self, number):
        if isinstance(number, Range):
            if number.start >= self.start and number.end <= self.end:
                return True
            else:
                return False
        elif isinstance(number, int):
            if number >= self.start and number <= self.end:
                return True
            else:
                return False
        else:
            raise TypeError("'number' must be of type Range or int, not " + type(number))

    def is_overlapping(self, range):
        if not isinstance(range, Range):
            raise TypeError("'range' must be of type Range, not " + type(range))
        else:
            if self.is_in_range(range.start) or self.is_in_range(range.end):
                return True
            else:
                return False

    def random(self):
        return random.randint(self.start, self.end)


class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_hitbox = Range(x, x + width - 1)
        self.y_hitbox = Range(y, y + height - 1)

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.x_hitbox = Range(x, x + self.width - 1)
        self.y_hitbox = Range(y, y + self.height - 1)

    def update_size(self, width, height):
        self.width = width
        self.height = height
        self.x_hitbox = Range(self.x, self.x + self.width - 1)
        self.y_hitbox = Range(self.y, self.y + self.height - 1)

    def is_colliding_with(self, entity):
        if entity.x_hitbox.is_overlapping(self.x_hitbox) and entity.y_hitbox.is_overlapping(self.y_hitbox):
            return True
        else:
            return False
