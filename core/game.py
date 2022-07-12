from copy import copy
from enum import Enum

import numpy as np


class Direction(Enum):
    NORTHWEST = (-1, -1)
    NORTH = (0, -1)
    NORTHEAST = (1, -1)
    EAST = (1, 0)
    SOUTHEAST = (1, 1)
    SOUTH = (0, 1)
    SOUTHWEST = (-1, 1)
    WEST = (-1, 0)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = np.zeros(shape=(width, height), dtype=int)

    def set_state(self, state_array):
        self.state = np.reshape(
            state_array,
            newshape=(self.height, self.width),
        )

    def get_value(self, x, y):
        return self.state[y][x]

    def set_value(self, x, y, value):
        self.state[y][x] = value

    def get_neighbours(self, x, y):
        neighbours = []
        for direction in Direction:
            neighbour_point = (
                x + direction.value[0],
                y + direction.value[1]
            )

            if not self._check_valid_point(*neighbour_point):
                neighbours.append(None)
                continue

            neighbour = self.get_value(*neighbour_point)
            neighbours.append(neighbour)
        return neighbours

    def _check_valid_point(self, x, y):
        if x < 0 or x > (self.width - 1):
            return False
        if y < 0 or y > (self.height - 1):
            return False
        return True

    def tick(self):
        new_state = copy(self.state)
        for y, row in enumerate(self.state):
            for x, value in enumerate(row):
                neighbours = self.get_neighbours(x, y)
                n_live_neighbours = sum(filter(None, neighbours))

                if value == 1 and n_live_neighbours in [2, 3]:
                    new_state[y][x] = 1
                elif value == 0 and n_live_neighbours == 3:
                    new_state[y][x] = 1
                else:
                    new_state[y][x] = 0

        self.state = new_state
        return self.state

