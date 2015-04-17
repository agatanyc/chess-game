#### Implementation Goes Here ####

# +---------------------------------------------------------------------------+
# | Immutable State                                                           |
# +---------------------------------------------------------------------------+

# Keep track of the two players, black and white.
BLACK = 'Black'
WHITE = 'White'
NEXT_PLAYER = {BLACK: WHITE, WHITE: BLACK}

# +---------------------------------------------------------------------------+
# | Mutable State                                                             |
# +---------------------------------------------------------------------------+

current_player = WHITE

# Uppercase is black, lowercase is white.
board = (list("RNBQKBNR"),  # 8
         list("PPPPPPPP"),  # 7
         list("        "),  # 6
         list("        "),  # 5
         list("        "),  # 4
         list("        "),  # 3
         list("pppppppp"),  # 2
         list("rnbqkbnr"))  # 1
             # abcdefgh

# +---------------------------------------------------------------------------+
# | Functions                                                                 |
# +---------------------------------------------------------------------------+

def decode_cell(cell):
    """Return (row, column)."""
    assert(is_valid_cell(cell))
    row = 8 - int(cell[1])
    col = "abcdefgh".index(cell[0])
    return row, col

def get_next_move():
    move = prompt_move()
    while not is_valid_move(move):
        print("invalid move")
        move = prompt_move()
    return move

def get_piece_at(cell):
    """Return the piece or pawn at the specified location, or empty string."""
    row, col = decode_cell(cell)
    return board[row][col].strip()

def is_checkmate():
    pass    # TODO

def is_stalemate():
    pass    # TODO

def is_valid_cell(cell):
    """(str) -> bool"""
    return len(cell) == 2 and cell[0] in "abcdefgh" and cell[1] in "12345678"

def is_valid_move(move):

    # Check for valid notation (i.e., a pair of cells).
    cells = move.split()
    if len(cells) != 2:
        return False
    source, target = cells
    if not is_valid_cell(source) or not is_valid_cell(target):
        return False
    piece = get_piece_at(source)
    if not piece:
        return False

    # TODO Verify that `target` is reachable from `source` by `piece`.

    return True

def print_board():
    print("   +--------+")
    rank = 8
    for row in board:
        print(" {} |{}|".format(rank, ''.join(row)))
        rank -= 1
    print("   +--------+")
    print("    abcdefgh ")

def prompt_move():
    return input("Enter a move for {}: ".format(current_player))

def set_piece_at(cell, piece):
    """Overwrite the specified location with the specified value."""
    row, col = decode_cell(cell)
    board[row][col] = piece

def update_board(move):
    source, target = move.split()
    set_piece_at(target, get_piece_at(source))
    set_piece_at(source, ' ')

# +---------------------------------------------------------------------------+
# | Main                                                                      |
# +---------------------------------------------------------------------------+
# The program repeatedly prints the board, prompts the current player for their
# move, and updates the board.  Each move must be a pair of cells separated by
# a space, indicating the "from" and "to" positions of some piece or pawn.

if __name__ == '__main__':

    game_over = False

    while not game_over:
        print_board()
        move = get_next_move()
        update_board(move)

        if is_checkmate():
            print(current_player, "wins!")
            game_over = True
        elif is_stalemate():
            print("Stalemate!")
            game_over = True
        else:
            current_player = NEXT_PLAYER[current_player]
