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
    global square_winner
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
                else: 
                    print(f'| {square_winner} ', end='')

                    square_winner = ' '
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
            Detect_Square(x, y)
    except IndexError:
       print("Invalid move! Try again")
       Move()


def Detect_Square(x,y):
    global square_winner, last_move
    x_limit = len(board_state[0])
    y_limit = len(board_state[1])
    is_square = []
    if x in [0, 2, 4, 5]:
       for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0: continue
                nx, ny = x+dx, y+dy
                if 0 <= nx < x_limit and 0 <= ny < y_limit:
                    if board_state[nx][ny] == 1: 
                        is_square.append(True)
                    else:
                        is_square.append(False)
                    if False in is_square: pass
                    else: square_winner = last_move
    else: pass

while end_game:
    print()
    Render()
    print()
    Move()
    print()
