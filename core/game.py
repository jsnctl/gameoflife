import numpy as np


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = np.zeros(shape=(width, height))

    def set_state(self, state_array):
        self.state = np.reshape(
            state_array,
            newshape=(self.width, self.height)
        )


