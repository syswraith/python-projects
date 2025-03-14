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
    global player_turn  # Needed to modify player_turn
    square_made = 0  # Initialize square_made
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
        player_turn = 1 - player_turn  # Switch turns if no square was made
    
def if_square(x, y):
    global player_turn
    player = 'A' if player_turn == 0 else 'B'
    squares_completed = 0  # Track how many squares were completed

    for square_coords in coords:
        if (x, y) in square_coords:
            if all(board_state[a][b] == 1 for (a, b) in square_coords):
                if square_coords not in squares_owned[player]:  # Avoid duplicates
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
                square_owner = ' '  # Default empty space

                # Check if (x, line) is part of a completed square
                for owner, squares in squares_owned.items():
                    if any(square[1] == (x, line) for square in squares):
                        square_owner = owner
                        break  # Stop searching after finding the owner

                # Print '|' if the point exists in board_state, followed by owner if applicable
                if board_state[x][line] == 1:
                    print(f"| {square_owner} ", end='')
                else:
                    print("    ", end='')
        print()
            # check if the point exists as 1 on board_state
            # check if the point exists inside squares_owned
            # if it does record square_owner as the key
            # print the '|' and follow it with spaces if only the point exists as 1
            # print the '|' and follow it with square_owner if both are true

while end_game:
    Render()
    if len(squares_owned['A'])+len(squares_owned['B'])==9: end_game = False
    print('A' if player_turn == 0 else 'B', end='')
    Move()
    print()

