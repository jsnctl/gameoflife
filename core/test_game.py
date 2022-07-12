import random
import numpy as np
import pytest

from core import game

@pytest.fixture
def board():
    board = game.Board(5, 5)
    return board

@pytest.fixture
def state_array():
    state_array = [
        0, 0, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0
    ]
    return state_array


def test_board():
    width = random.randint(0, 1000)
    height = random.randint(0, 1000)
    board = game.Board(width, height)

    assert np.shape(board.state) == (width, height)


def test_board_set_state(board, state_array):
    board.set_state(state_array)

    assert board.state[0][0] == 0
    assert board.state[1][1] == 1
    assert board.state[1][3] == 1
    assert board.state[3][1] == 1
    assert board.state[3][3] == 1
    assert board.state[4][4] == 0
