import re

valid_pieces = { 'P': 1, 'C': 5, 'H': 3, 'B': 3, 'Q': 9, 'K': 40 }
error_msg = 'Error! The selected piece was not recognized!'

def get_value(type):
    if type in valid_pieces:
        return valid_pieces[type]
    else:
        print(error_msg)
        return False

def get_selection(input_string):
    if len(input_string != 2):
        return False
    
    if not re.search("[a-hA-H]", input_string[0]):
        return False

    if not input_string.isnumeric():
        return False

    row = input_string[1]
    col = input_string[0]

    if row < 1 or row > 8:
        return False
    
    return [row, col]

def get_moves(piece, squares):
    if piece.type == 'P':
        one_forward = piece.row + 1 if piece.color == 'dark' else piece.row - 1
        two_forward = piece.row + 2 if piece.color == 'dark' else piece.row - 2
        one_left = piece.col + 1 if piece.color == 'dark' else piece.col - 1
        one_right = piece.col - 1 if piece.color == 'dark' else piece.col + 1

        # Check if the pawn can move one space forward
        if one_forward < 8 and squares[one_forward][piece.col] == '':
            piece.avail_moves.append([one_forward, piece.col])
        
        # Check if the pawn can move two spaces forward
        if two_forward < 8 and squares[one_forward][piece.col] == '' and squares[two_forward][piece.col] == '' and len(piece.prev_moves) == 0:
            piece.avail_moves.append([two_forward, piece.col])

        # Check if the pawn can attack left
        if one_left < 8 and squares[one_forward][one_left] != '' and squares[one_forward][one_left].color != piece.color:
            piece.avail_moves.append([one_forward, one_left, squares[one_forward][one_left].type])
        
        # Check if the pawn can attack right
        if one_right > -1 and squares[one_forward][one_right] != '' and squares[one_forward][one_right].color != piece.color:
            piece.avail_moves.append([one_forward, one_right, squares[one_forward][one_right].type])

    if piece.type == 'C' or piece.type == 'Q':
        # Check forward spaces available
        r = piece.row - 1 
        c = piece.col
        while r > -1 and r < 7 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            r -= 1
        if r > -1 and r < 7 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])

        # Check backward spaces available
        r = piece.row + 1
        c = piece.col
        while r > 0 and r < 8 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            r += 1
        if r > 0 and r < 8 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])

        # Check left spaces available
        r = piece.row
        c = piece.col - 1
        while c > -1 and c < 7 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            c -= 1
        if c > -1 and c < 7 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])
        
        # Check right spaces available
        r = piece.row
        c = piece.col + 1
        while c > 0 and c < 8 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            c += 1
        if c > 0 and c < 8 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c])

    if piece.type == 'B' or piece.type == 'Q':
        # Check forward-right spaces available
        r = piece.row - 1 
        c = piece.col + 1
        while r > -1 and r < 7 and c > 0 and c < 8 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            r -= 1
            c += 1
        if r > -1 and r < 7 and c > 0 and c < 8 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])

        # Check forward-left spaces available
        r = piece.row - 1 
        c = piece.col - 1
        while r > -1 and r < 7 and c > -1 and c < 7 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            r -= 1
            c -= 1
        if r > -1 and r < 7 and c > -1 and c < 7 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])

        # Check backward-right spaces available
        r = piece.row + 1 
        c = piece.col + 1
        while r > 0 and r < 8 and c > 0 and c < 8 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            r += 1
            c += 1
        if r > 0 and r < 8 and c > 0 and c < 8 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])

        # Check backward-left spaces available
        r = piece.row + 1 
        c = piece.col - 1
        while r > 0 and r < 8 and c > -1 and c < 7 and squares[r][c] == '':
            piece.avail_moves.append([r, c])
            r += 1
            c -= 1
        if r > 0 and r < 8 and c > -1 and c < 7 and squares[r][c].color != piece.color:
            piece.avail_moves.append([r, c, squares[r][c].type])

    if piece.type == 'H':
        # Check the 8 possible move options
        r = piece.row
        c = piece.col
        options = [ [r-2, c+1], [r-2, c-1], [r+2, c+1], [r+2, c-1], [r-1, c+2], [r+1, c+2], [r-1, c-2], [r+1, c-2] ]
        for opt in options:
            if opt[0] > -1 and opt[0] < 8 and opt[1] > -1 and opt[1] < 8:
                landing_square = squares[opt[0]][opt[1]]
                if landing_square == '':
                    piece.avail_moves.append([opt[0], opt[1]])
                if landing_square != '' and landing_square.color != piece.color:
                    piece.avail_moves.append([opt[0], opt[1], landing_square.type])
    
    if piece.type == 'K':
        # Check the 8 possible surrounding moves
        r = piece.row
        c = piece.col
        options = [ [r-1, c], [r-1, c+1], [r, c+1], [r+1, c+1], [r+1, c], [r+1, c-1], [r, c-1], [r-1, c-1] ]
        for opt in options:
            if opt[0] > -1 and opt[0] < 8 and opt[1] > -1 and opt[1] < 8:
                landing_square = squares[opt[0]][opt[1]]
                if landing_square == '':
                    piece.avail_moves.append([opt[0], opt[1]])
                if landing_square != '' and landing_square.color != piece.color:
                    piece.avail_moves.append([opt[0], opt[1], landing_square.type])

    if piece.type not in valid_pieces:
        print(error_msg)
        return False
