from terminal_messages import *
from game_objects import *
from game_rules import get_moves

def play_chess():
    # Get player information
    new_name = ''
    print('Type your name and press ENTER to begin.')
    while True:
        new_name = input()
        if new_name.strip() != '':
            break
    print('')
    print(welcome)

    # Select new game or instructions
    while True:
        print(main_menu)
        response = input('Type your selection and press ENTER.  ')
        if response == '2':
            print(how_to_play)
        if response == '1':
            break

    # Setup the game
    player = Player(new_name, 'light', True)
    computer = Player('Hal', 'dark', False)
    check_mate = False
    board = Board()
    board.reset()
    
    while not check_mate:

        while True:
            player_selected_piece = input('Choose a piece to move by typing the row and column.  For example, "A1" ENTER.')




play_chess()

# TESTING FOR EACH PIECE MOVES

# my_board = Board()
# my_board.reset_board()

# my_castle = Piece('dark', 'C', 4, 2)
# my_board.squares[4][2] = my_castle

# my_pawn = Piece('light', 'P', 5, 3)
# my_board.squares[5][3] = my_pawn

# my_horse = Piece('light', 'H', 3, 4)
# my_board.squares[3][4] = my_horse

# my_bishop = Piece('dark', 'B', 4, 4)
# my_board.squares[4][4] = my_bishop

# my_queen = Piece('light', 'Q', 3, 3)
# my_board.squares[3][3] = my_queen

# my_king = Piece('dark', 'K', 2, 2)
# my_board.squares[2][2] = my_king

# my_board.print_board()

# get_moves(my_castle, my_board.squares)
# print('Castle: ', my_castle.avail_moves)

# get_moves(my_pawn, my_board.squares)
# print('Pawn: ', my_pawn.avail_moves)

# get_moves(my_horse, my_board.squares)
# print('Horse: ', my_horse.avail_moves)

# get_moves(my_bishop, my_board.squares)
# print('Bishop: ', my_bishop.avail_moves)

# get_moves(my_queen, my_board.squares)
# print('Queen: ', my_queen.avail_moves)

# get_moves(my_king, my_board.squares)
# print('King: ', my_king.avail_moves)
