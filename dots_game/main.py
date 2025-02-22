# implementing dots game
# gonna try to do this with the newfound bitboard method

DOTS = 3

moves = []
lines = [0 for dot in range((DOTS ** 2 + DOTS - 2))]
board_state = [ 0 for dot in range((DOTS - 1)**2) ]


'''
for x in range(len(board_state)): 
    if x % BOARD_WIDTH == 0: print()
    print(f' {board_state[x]} ',end='')

print()
for x in range(DOTS ** 2):
    if x % BOARD_WIDTH == 0 and x != 0: 
        print()
        print()
    print(f'  + ',end='')
print()
'''

print(len(lines), len(board_state))
