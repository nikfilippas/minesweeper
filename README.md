# minesweeper
<pre>
"Smart" minesweeper, not based on luck.

In situations like the one below:
 _____________________
|      |      |  <|  |
|______|______|___|__|
|  1   |   3  |  <|  |
|______|______|___|__|,

you would potentialy need to repair your
computer monitor from the rage-caused
damage.

Fear not, this game of minesweeper runs
a parallel solver and tests such ambiguous
cases.

Supposing there are two fields of equal
probability to be mined, the solver lets
you choose either - and the mine just
moves to the field you didn't click!

Minesweeper is an NP-complete game
(https://en.wikipedia.org/wiki/NP-completeness),
so the solver runs in exponential time.
For large boards, this might take some
time to load, but it will never leave
a field to luck.

Enjoy this smart version of minesweeper!
