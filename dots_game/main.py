'''
+---+---+---+
|   |   
'''


board_state = [[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0],[0,0,0,0],[0,0,0]]

def Render():
    for x in board_state:
        if len(x) == 3:
            print('+',end='')
            for line in x:
                if line == 0: print('   +',end='')
                else: print('---+',end='')
        else:
            for line in x:
                if line == 0: print('    ', end='')
                else: print('|   ', end='')
        print()


board_state[2][1] = 1
board_state[1][2] = 1
Render()
