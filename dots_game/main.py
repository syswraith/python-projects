'''
      0   1   2
    +---+---+---+
    |   |   |   |
    +---+---+---+
    |   |   |   |
    +---+---+---+
    |   |   |   |
    +---+---+---+
    0   1   2   3
'''

end_game = True
last_move = 'A'
square_winner = ' '
board_state = [[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0]]


def Render():
    print('  0   1   2 ')
    for x in board_state:
        if len(x) == 3:
            print('+',end='')
            for line in x:
                if line == 0: print('   +',end='')
                else: print('---+',end='')
        else:
            for line in x:
                if line == 0: print('    ', end='')
                else: print(f'| {square_winner} ', end='')
        print()
    print('0   1   2   3')

def Move():
    move = input('> ')
    x,y = map(int,move.split(','))
    try:
        if board_state[x][y] == 1: 
            print('> Move has already been made')
            Move()
        else: 
            board_state[x][y] = 1
    except IndexError:
        print("Invalid move! Try again")
        Move()

while end_game:
    print()
    Render()
    print()
    Move()
    print()
