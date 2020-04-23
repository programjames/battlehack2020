# Genetic

This contains the heuristic-based genetic algorithm, and for some reason the custom branch of the `battlecode20-minimal` engine
(in `bh20min/`).

## Heuristics:

### Overlord Heuristics:
**Center** - How far away is this column from the center of the board?
**Distance Enemy** - How close to being promoted is the nearest enemy in this column?
**Distance Friendly** - How close to the spawn point is the nearest friend in this column?
**Finished** - Did we promote a pawn on this column?
**Odd** - Is this column an odd number column? (Useful to make "pillars" of pawns alternating columns.)
**Pawns** - How many pawns are there in this column and the two neighboring ones? Add one for a friend,
and subtract one for an enemy.

Example:
```
  0 1 2 3 4 5 6 7 8 9
0 W   W
1 W
2 W
3           W
4
5           W
6     B B
7     B B
8     B B B
9       W B
```
Looking at column 3, we would have the following values for the heuristics:
```
Center = 4.5 - 3 = 1.5
Distance Enemy = 6
Distance Friendly = 9
Finished = 1
Odd = 1
Pawns = 2 - 8 = -6
```

### Pawn Heuristics
Okay! It looks like these heuristics got destroyed to make way for a hand-crafted pawn. You can check
out previous commits to try to find them. Maybe try around commit 20?
