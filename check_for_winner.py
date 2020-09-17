
def check_x(game_board, grid_size, symbol):
    """Checking x for winner"""

    for row in game_board:
        points_in_row = 0
        for element in row:
            if element == symbol:
                points_in_row += 1
                if points_in_row == grid_size:
                    return True


def check_y(game_board, grid_size, symbol):
    """Checking y for winner"""

    y = 0
    x = 0
    points_in_row = 0
    while x < grid_size:
        if y > grid_size - 1:
            x += 1
            y = 0
            points_in_row = 0
        else:
            if game_board[y][x] == symbol:
                points_in_row += 1
            y += 1

        if points_in_row == grid_size:
            return True


def check_diagonal_1(game_board, grid_size, symbol):
    """Checking first diagonal for winner"""
    #
    i = 0
    points_in_row = 0
    while i < grid_size:
        if game_board[i][i] == symbol:
            points_in_row += 1
            if points_in_row == grid_size:
                return True
        i += 1


def check_diagonal_2(game_board, grid_size, symbol):
    """Checking second diagonal for winner"""

    y = grid_size-1
    x = 0
    points_in_row = 0
    while y >= 0:
        if game_board[y][x] == symbol:
            points_in_row += 1
            if points_in_row == grid_size:
                return True
        y -= 1
        x += 1


def check_for_winner(game_board, grid_size, symbol):
    """Checks the grid's x, y and diagonals for winner """

    if check_x(game_board, grid_size, symbol):
        return True
    if check_y(game_board, grid_size, symbol):
        return True
    if check_diagonal_1(game_board, grid_size, symbol):
        return True
    if check_diagonal_2(game_board, grid_size, symbol):
        return True

