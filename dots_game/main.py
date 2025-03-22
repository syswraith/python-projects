end_game = True
board_state = [[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0]]
num_blocks = 3
player_turn = 0
squares_owned = {
    'A': [],
    'B': []
}

def generate_coordinates(num_blocks):
    coords = []
    for b in range(num_blocks):
        x_offset = b * 2
        coords.extend([
            [(x_offset, 0), (x_offset + 1, 0), (x_offset + 1, 1), (x_offset + 2, 0)],
            [(x_offset, 1), (x_offset + 1, 1), (x_offset + 1, 2), (x_offset + 2, 1)],
            [(x_offset, 2), (x_offset + 1, 2), (x_offset + 1, 3), (x_offset + 2, 2)]
        ])
    return coords

coords = generate_coordinates(num_blocks)

def Move():
    global player_turn
    square_made = 0 
    move = input(' > ')
    x, y = map(int, move.split(','))
    try:
        if board_state[x][y] == 1:
            print(" > Move already made. Try again.")
            return Move()
        else:
            board_state[x][y] = 1
            if if_square(x, y):
                square_made = 1
    except IndexError:
        print(" > Invalid move. Try again.")
        return Move()
    
    if square_made == 0:
        player_turn = 1 - player_turn
    
def if_square(x, y):
    global player_turn
    player = 'A' if player_turn == 0 else 'B'
    squares_completed = 0

    for square_coords in coords:
        if (x, y) in square_coords:
            if all(board_state[a][b] == 1 for (a, b) in square_coords):
                if square_coords not in squares_owned[player]:
                    squares_owned[player].append(square_coords)
                    squares_completed += 1

    if squares_completed > 0:
        return True
    return False

def Render():
    for x in range(len(board_state)):
        if len(board_state[x]) == 3:
            print('+', end='')
            for line in board_state[x]:
                print('---+' if line else '   +', end='')
        else:
            for line in range(len(board_state[x])):
                square_owner = ' '

                for owner, squares in squares_owned.items():
                    if any(square[1] == (x, line) for square in squares):
                        square_owner = owner
                        break

                if board_state[x][line] == 1:
                    print(f"| {square_owner} ", end='')
                else:
                    print("    ", end='')
        print()

while end_game:
    Render()
    if all(all(cell == 1 for cell in row) for row in board_state):
        winner = max(squares_owned, key=lambda k: len(squares_owned[k]))
        print(f"{winner} wins")
        break
    print('A' if player_turn == 0 else 'B', end='')
    Move()
    print()

