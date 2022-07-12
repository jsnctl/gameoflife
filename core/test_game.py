import random
import numpy as np
import pytest

from core import game


@pytest.fixture
def board():
    board = game.Board(6, 5)
    return board


@pytest.fixture
def state_array():
    state_array = [
        0, 0, 0, 0, 0, 0,
        0, 1, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 1, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 0
    ]
    return state_array


def test_board():
    width = random.randint(0, 1000)
    height = random.randint(0, 1000)
    board = game.Board(width, height)

    assert np.shape(board.state) == (width, height)


def test_board_set_state(board, state_array):
    board.set_state(state_array)

    assert board.get_value(0, 0) == 0
    assert board.get_value(1, 1) == 1
    assert board.get_value(1, 3) == 1
    assert board.get_value(3, 1) == 1
    assert board.get_value(3, 3) == 1
    assert board.get_value(5, 4) == 0


def test_board_get_neighbours(board, state_array):
    board.set_state(state_array)

    result = board.get_neighbours(0, 0)
    assert result == [None, None, None, 0, 1, 0, None, None]

    result = board.get_neighbours(1, 1)
    assert result == [0, 0, 0, 0, 0, 0, 0, 0]

    result = board.get_neighbours(4, 4)
    assert result == [1, 0, 0, 0, None, None, None, 0]

    result = board.get_neighbours(2, 4)
    assert result == [1, 0, 1, 0, None, None, None, 0]