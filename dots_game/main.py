'''
implementing dots game
gonna try to do this with the newfound bitboard method
need a bitboard for:
board state (which cells are occupied and stuff)
-- lines
| lines
A moves
B moves

notations used: "0,0 0,1" (for simplicity)
'''

DOTS = 4
vertical_lines = [ 0 for line in range((DOTS-1)*(DOTS)) ]
horizontal_lines = [0 for line in range((DOTS-1)*(DOTS))] 
board_state = [ 0 for dot in range((DOTS - 1)**2) ]
player_A = board_state
player_B = board_state

win_state = True

def draw():
    counter = 0
    for x in range(len(horizontal_lines)):
        if counter == 2 and x != 0: 
            print(f"+ {horizontal_lines[x]} ", end='')
            print('+')
            counter = 0
        else: 
            print(f"+ {horizontal_lines[x]} ", end='')
            counter += 1

def gameloop():
    while win_state:
        input_A = input()

draw()
# printing function
'''
for x in range(DOTS ** 2):
    if x % DOTS == 0 and x != 0: 
        print()
        print()
    print(f'  + ',end='')
print()
'''
