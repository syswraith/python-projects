```
lines = [0 for dot in range((DOTS ** 2 + DOTS - 2))]
board_state = [ 0 for dot in range((DOTS - 1)**2) ]
```

In bitboard method, you update the index of positions as such
INDEX = DOTS * ROWS + COLUMNS
start from 0
