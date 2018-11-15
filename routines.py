"""Minesweeper routines."""

import numpy as np


def neighbors(index, shape):
    """Indices of adjacent cells (side-to-side and diagonally)."""
    index = list(index)
    shape = list(shape)
    # split in bins (left wall, middle, right wall)
    positions = [np.digitize(i, bins=[1, s-1]) for i, s in zip(index, shape)]

    idx = [[]] * len(index)
    for i, pos in enumerate(positions):
        if pos == 0:
            idx[i] = [index[i], index[i]+1]
        elif pos == 1:
            idx[i] = [index[i]-1, index[i], index[i]+1]
        else:
            idx[i] = [index[i]-1, index[i]]

    nb = np.array(np.meshgrid(*idx)).T.reshape(-1, len(index))
    cidx = np.bincount(np.where(nb == index)[0]).argmax()
    nb = np.delete(nb, cidx, axis=0)
    return nb


def Click():
    """Convert index string to index list."""
    click = input()
    click_x, click_y = map(int, click.split(","))
    click = (click_x, click_y)
    return click
