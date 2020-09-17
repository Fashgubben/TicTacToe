from class_statistics import Player
from random import randint
from datetime import datetime
import check_input


def get_grid_size():
    """Get the size of the game board from user"""

    while True:
        try:
            print('\nEnter board size with a number (e.g "3" will result in a 3x3 board)')
            grid_size = input('Enter a number: ').strip(" ")
            if int(grid_size) > 0:
                return int(grid_size)
        except ValueError:
            print('Error - Only enter numbers larger than 0')


def create_board(grid_size):
    """Creates a number x number grid based on input"""

    game_board = [['_' for number in range(grid_size)] for number in range(grid_size)]
    return game_board


def reset_move_count(p1, p2, total):
    """Resets players and totals last game move count to 0"""

    p1.last_game_moves = 0
    p2.last_game_moves = 0
    total.last_game_moves = 0


def print_board_titles(grid_size):
    """Creates column numbers for the game board"""

    column_number = 0
    column_number_list = ['    ']

    for number in range(grid_size):
        column_number_list.append(str(column_number))
        column_number_list.append('    ')
        column_number += 1

    string_column_number = "".join(column_number_list)
    return string_column_number


def print_board(game_board, grid_size, p1, p2):
    """Prints the current status of the game"""

    print('\n' + 'TIC TAC TOE'.center(23, '-'))
    print(f'{p1.name} vs. {p2.name}'.center(23, ' ') + '\n')
    print(print_board_titles(grid_size))

    row_number = 0
    for item in game_board:
        print(row_number, item)
        row_number += 1


def get_input(player):
    """Get's input from player"""

    print('\nEnter coordinates separated with space ("X Y")')
    return input(f"{player.name}'s turn: ")


# Computers turn only
def get_random_numbers(grid_size):
    """Generates and returns a list of two random numbers"""

    number_list = []
    for number in range(2):
        number_list.append(randint(0, grid_size-1))

    return number_list


# Computers turn only
def get_computer_coordinates(player, grid_size, game_board):
    """Gets valid random coordinates"""

    run_while = True
    while run_while:

        coordinates = get_random_numbers(grid_size)
        valid_coordinates = check_input.is_coordinates_occupied(coordinates, game_board, player)

        if valid_coordinates != False:
            return valid_coordinates


def check_for_available_moves(game_board, grid_size):
    """Checks if game board is full"""

    filled_box_counter = 0
    for row in game_board:
        for square in row:
            if square != '_':
                filled_box_counter += 1

    if filled_box_counter == grid_size * grid_size:
        return False
    else:
        return True


def place_mark(game_board, coordinates, symbol):
    """Places players mark on the game board"""

    game_board[coordinates[1]][coordinates[0]] = symbol


def update_stats(p1, p2, total):
    """Updates statistics"""

    p1.games += 1
    Player.update_player_moves(p1)
    p1.update_scoreboard()

    p2.games += 1
    Player.update_player_moves(p2)
    p2.update_scoreboard()

    total.games += 1
    total.update_total(p1, p2)
    total.update_scoreboard()


def update_stats_tie(p1, p2, total):
    """Updates tie stats"""

    p1.ties += 1
    p2.ties += 1
    total.ties += 1


def save_game_result(game_board, player, p1, p2, grid_size, win):
    """Saves all played games in text file"""

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    col_numbers = print_board_titles(grid_size)

    with open('game_history.txt', 'a', encoding='utf-8') as text_file:
        text_file.write('\n' + time + '\n')
        text_file.write(f'{p1.name} vs. {p2.name}\n')

        if win:
            text_file.write(f'Winner: {player.name}({player.symbol})\n')
        if win != True:
            text_file.write('This game was a tie\n')

        text_file.write('\n' + col_numbers + '\n')

        row_number = 0
        for item in game_board:
            text_file.write(str(row_number) + ' ' + str(item) + '\n')
            row_number += 1

        text_file.write('\n----------------------')

