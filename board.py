"""Minesweeper board."""

import numpy as np
import numpy.random as rnd
from scipy.signal import convolve

from routines import neighbors, Click


## INPUT ##
nrows = 5  # 16
ncols = 5 # 30
nmines = None


## MINEFIELD PROPERTIES ##
nrows = int(nrows)
ncols = int(ncols)
nplayers = 1
if not nmines:
    percentage = 20.625
    nmines = percentage/100 * (nrows*ncols)
nmines = int(np.around(nmines))


## INITIALISE BOARD ##
rnd.seed(0)  # seed for multiplayer

cover = np.zeros((nrows,ncols), dtype=int)    # what the player sees
field = np.zeros((nrows,ncols), dtype=int)    # minefield
click = np.zeros((nrows,ncols), dtype=int)    # what has been clicked (mask)
trash = np.zeros((nrows,ncols), dtype=int)    # inactive cells

# first input
x = Click()
click[x] = int(1)
neighborlist = neighbors(x, (nrows,ncols))
for n in neighborlist:
    n = tuple(n)
    click[n] = int(1)

field = np.ma.MaskedArray(field, mask=click)

# spread mines
pos = rnd.choice(np.arange(field.count()), size=nmines, replace=False)
idx = tuple(np.take((~field.mask).nonzero(), pos, axis=1))

field[idx] = -1

# if all neighbours are masked, don't loop over it











