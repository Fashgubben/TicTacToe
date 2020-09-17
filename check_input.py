
def strip_spaces(user_input):
    """Strips the spaces on the sides of the string"""

    return str(user_input).strip(" ")


def splits_on_space(user_input):
    """Splits user input on spaces and returns list of elements"""

    return user_input.split(" ")


def convert_to_int(coordinates):
    """Test if the input is digits only"""

    int_list = []
    for value in coordinates:
        if value.isdigit():
            int_list.append(int(value))
        else:
            raise ValueError('Error - Only digits allowed, please re-enter a valid input.')
    return int_list


def check_coordinates_count(coordinates):
    """Checks if input is two numbers"""

    if len(coordinates) == 2:
        return coordinates
    elif len(coordinates) > 2:
        raise ValueError('Error - Input contained too many values. Please retry with TWO numbers.')
    else:
        raise ValueError('Error - Input contained too few values. Please retry with TWO numbers.')


def check_coordinates_range(coordinates, grid_size):
    """Checks if the coordinates are within board range"""

    for value in coordinates:
        if value > grid_size-1 or value < 0:
            raise ValueError('Error - Give coordinates that are within the game board limit.')

    return coordinates


def is_coordinates_occupied(coordinates, game_board, name):
    """Raises a ValueError if the coordinates does not point to an empty box"""

    if game_board[coordinates[1]][coordinates[0]] != '_':
        if name == 'Skynet':
            return False
        else:
            raise ValueError('Error - Position already taken! Please choose another coordinate.')
    else:
        return coordinates


def get_valid_coordinates(game_board, grid_size, player_move, name):
    """Gets input and test if it's valid"""

    player_move = strip_spaces(player_move)
    list_of_input = splits_on_space(player_move)
    coordinates = convert_to_int(list_of_input)
    coordinates = check_coordinates_count(coordinates)
    coordinates = check_coordinates_range(coordinates, grid_size)
    coordinates = is_coordinates_occupied(coordinates, game_board, name)
    return coordinates
