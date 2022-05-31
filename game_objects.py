from game_rules import get_value

class Board:
    def __init__(self):
        self.squares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
    
    def reset(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = ''

        self.squares[0][0] = Piece('dark', 'C', 0, 0)
        self.squares[0][1] = Piece('dark', 'H', 0, 1)
        self.squares[0][2] = Piece('dark', 'B', 0, 2)
        self.squares[0][3] = Piece('dark', 'Q', 0, 3)
        self.squares[0][4] = Piece('dark', 'K', 0, 4)
        self.squares[0][5] = Piece('dark', 'B', 0, 5)
        self.squares[0][6] = Piece('dark', 'H', 0, 6)
        self.squares[0][7] = Piece('dark', 'C', 0, 7)
        for i in range(8):
            self.squares[1][i] = Piece('dark', 'P', 1, i)

        self.squares[7][0] = Piece('light', 'C', 7, 0)
        self.squares[7][1] = Piece('light', 'H', 7, 1)
        self.squares[7][2] = Piece('light', 'B', 7, 2)
        self.squares[7][3] = Piece('light', 'Q', 7, 3)
        self.squares[7][4] = Piece('light', 'K', 7, 4)
        self.squares[7][5] = Piece('light', 'B', 7, 5)
        self.squares[7][6] = Piece('light', 'H', 7, 6)
        self.squares[7][7] = Piece('light', 'C', 7, 7)
        for j in range(8):
            self.squares[6][j] = Piece('light', 'P', 6, j)
    
    def print_board(self):
        letter_border = '    A    B    C    D    E    F    G    H   '
        horizontal_border = ' -|----|----|----|----|----|----|----|----|- '

        print(letter_border)
        print(horizontal_border)

        for row in range(8):
            curr_board_line = str(row+1) + ' |'

            for col in range(8):
                val = self.squares[row][col]
                square_is_white = (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1)
                if val == '':
                    curr_board_line += '[  ]' if square_is_white else '    '
                else:
                    piece = val.type + '*' if val.color == 'light' else val.type + '!'
                    curr_board_line += f'[{piece}]' if square_is_white  else f' {piece} '
                curr_board_line += '|'

            curr_board_line += ' ' + str(row+1)
            print(curr_board_line)
            print(horizontal_border)

        print(letter_border)

class Piece:
    def __init__(self, color, type, row, col):
        self.color = color
        self.type = type
        self.value = get_value(type)
        self.row = row
        self.col = col
        self.avail_moves = []
        self.prev_moves = []
        
    def move(self, board, to_row, to_col):
        self.prev_moves.append([self.row, self.col], [to_row, to_col])
        board.squares[to_row][to_col] = self
        board.squares[self.row][self.col] = ''
        self.row = to_row
        self.col = to_col
        self.avail_moves = []
    
    def change_type(self):
        print('Nice! Your pawn has reached the opposite side of the board.')
        print('You may trade your pawn for a different game piece.')
        available_types = ['C', 'H', 'B', 'Q']
        new_type = ''

        while True:
            print('You may choose from: ', available_types)
            new_type = input('Enter your choice here:  ').upper()
            if new_type in available_types:
                break
        self.type = new_type

class Player:
    def __init__(self, name, color, human):
        self.name = name
        self.color = color
        self.human = human
        self.points = 0