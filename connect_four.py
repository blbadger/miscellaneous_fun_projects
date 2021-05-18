# connect_four.py

def connect_four_winner(moves_list):
    '''A function that takes a list of connect four moves (each
    move in the format of X_color where X is the row of piece addition
    and color is the color of the piece moved) and returns the winning 
    color, or 'Draw' if there is no winner.
    '''

    # initialize the board
    board = [[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]

    # add each move to the board and check if either color has won
    for move in moves_list:
        if move[2:] == 'Red':
            piece = 1
        else: 
            piece = 2
        for i, letter in enumerate('ABCDEFG'):
            if move[0] == letter:
                for k in range(6):
                    if board[k][i] == 0:
                        board[k][i] = piece
                        break
        import pprint
        pprint.pprint (board)

        for i in range(6):
            for j in range(7):
            
                # check for a horizontal four
                count = 0
                for k in range(4):
                    if board[i][j+k] == piece: count += 1
                    else: break
                if count == 4:
                    return 'Red' if piece == 1 else 'Yellow'

                # check for a vertical four
                count = 0
                for n in range(4):
                    if board[i+n][j] == piece: count += 1
                    else: break
                if count == 4:
                    return'Red' if piece == 1 else 'Yellow'

                # check for diagonal four right
                count = 0
                for r in range(4):
                    if board[i+r][j+r] == piece: count += 1
                    else: break
                if count == 4:
                    return 'Red' if piece == 1 else 'Yellow'

                # check for diagonal four left
                count = 0
                for s in range(4):
                    if board[i-s+3][j+s] == piece: count += 1
                    else: break
                if count == 4:
                    return 'Red' if piece == 1 else 'Yellow'

    return 'Draw'


# example input
moves_list = [
"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red"]

# example function call
print (connect_four_winner(moves_list))