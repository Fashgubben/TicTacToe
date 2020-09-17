import unittest
import check_input
import check_for_winner
import game_functions
from class_statistics import Statistics, Player
from random import randint


class TestCases(unittest.TestCase):

    """Test "check_input" functions"""

    def test_strip_spaces(self):

        test_value1 = '1 1   '
        test_value2 = '   1 1'
        test_value3 = '   1 1    '
        expected_value = '1 1'

        function_value = check_input.strip_spaces(test_value1)
        self.assertEqual(expected_value, function_value)

        function_value = check_input.strip_spaces(test_value2)
        self.assertEqual(expected_value, function_value)

        function_value = check_input.strip_spaces(test_value3)
        self.assertEqual(expected_value, function_value)

    def test_splits_on_space(self):
        test_value = '1 2'
        expected_result = ['1', '2']

        function_value = check_input.splits_on_space(test_value)
        self.assertEqual(expected_result, function_value)

    def test_convert_to_int(self):

        test_value1 = ['1', '2']
        test_value2 = ['1', 'a']
        expected_result = [1, 2]

        function_value = check_input.convert_to_int(test_value1)
        self.assertEqual(expected_result, function_value)

        with self.assertRaises(ValueError):
            check_input.convert_to_int(test_value2)

    def test_check_coordinates_count(self):

        test_value1 = [randint(0, 10), randint(0, 10)]
        test_value2 = [1, 2, 3]
        test_value3 = [1]
        expected_result = 2

        function_value = check_input.check_coordinates_count(test_value1)
        self.assertEqual(expected_result, len(function_value))

        with self.assertRaises(ValueError):
            check_input.check_coordinates_count(test_value2)
        with self.assertRaises(ValueError):
            check_input.check_coordinates_count(test_value3)

    def test_check_coordinates_range(self):

        grid_size = 4
        test_value1 = [randint(0, 3), randint(0, 3)]
        test_value2 = [8, 9]

        function_value = check_input.check_coordinates_range(test_value1, grid_size)
        self.assertIn(function_value[0] and function_value[1], range(grid_size))

        with self.assertRaises(ValueError):
            check_input.check_coordinates_range(test_value2, grid_size)

    def test_is_coordinates_occupied(self):

        test_coordinates = [0, 1]
        name1 = 'Name'
        name2 = 'Skynet'
        game_board1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        game_board2 = [['_', '_', '_'], ['X', '_', '_'], ['_', '_', '_']]
        expected_value1 = [0, 1]

        function_value = check_input.is_coordinates_occupied(test_coordinates, game_board1, name1)
        self.assertEqual(expected_value1, function_value)

        function_value = check_input.is_coordinates_occupied(test_coordinates, game_board2, name2)
        self.assertFalse(function_value)

        with self.assertRaises(ValueError):
            check_input.is_coordinates_occupied(test_coordinates, game_board2, name1)

    def test_get_valid_coordinates(self):

        game_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        grid_size = 3
        user_input = "0 0"
        name = 'Name'
        expected_result = [0, 0]

        function_value = check_input.get_valid_coordinates(game_board, grid_size, user_input, name)
        self.assertEqual(expected_result, function_value)

    def test_check_x(self):

        game_board1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        game_board2 = [['_', '_', '_'], ['X', 'X', 'X'], ['_', '_', '_']]
        grid_size = 3
        symbol = 'X'

        function_value = check_for_winner.check_x(game_board1, grid_size, symbol)
        self.assertNotEqual(function_value, True)

        function_value = check_for_winner.check_x(game_board2, grid_size, symbol)
        self.assertTrue(function_value)

    def test_check_y(self):

        game_board1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        game_board2 = [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
        grid_size = 3
        symbol = 'X'

        function_value = check_for_winner.check_y(game_board1, grid_size, symbol)
        self.assertNotEqual(function_value, True)

        function_value = check_for_winner.check_y(game_board2, grid_size, symbol)
        self.assertTrue(function_value)

    def test_check_diagonal_1(self):

        game_board1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        game_board2 = [['X', '_', '_'], ['_', 'X', '_'], ['_', '_', 'X']]
        grid_size = 3
        symbol = 'X'

        function_value = check_for_winner.check_diagonal_1(game_board1, grid_size, symbol)
        self.assertNotEqual(function_value, True)

        function_value = check_for_winner.check_diagonal_1(game_board2, grid_size, symbol)
        self.assertTrue(function_value)

    def test_check_diagonal_2(self):

        game_board1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        game_board2 = [['_', '_', 'X'], ['_', 'X', '_'], ['X', '_', '_']]
        grid_size = 3
        symbol = 'X'

        function_value = check_for_winner.check_diagonal_2(game_board1, grid_size, symbol)
        self.assertNotEqual(function_value, True)

        function_value = check_for_winner.check_diagonal_2(game_board2, grid_size, symbol)
        self.assertTrue(function_value)

    """Test "class_statistics" functions"""

    def test_add_win(self):

        test_value = test_player.wins
        test_player.add_win()
        self.assertEqual(test_player.wins, test_value + 1)

    def test_add_total_move(self):

        test_value = test_player.total_moves
        test_player.add_total_move()
        self.assertEqual(test_player.total_moves, test_value + 1)

    def test_add_last_game_moves(self):

        test_value = test_player.last_game_moves
        test_player.add_last_game_moves()
        self.assertEqual(test_player.last_game_moves, test_value + 1)

    def test_calculate_total_average_moves(self):

        test_player.total_moves = 3
        test_player.games = 1

        test_player.calculate_total_average_moves()
        self.assertEqual(test_player.total_average_moves, round(test_player.total_moves / test_player.games, 2))

        test_player.total_moves = 0
        test_player.games = 0

        test_player.calculate_total_average_moves()
        self.assertEqual(test_player.total_average_moves, 0.0)

    def test_calculate_average_win_moves(self):

        test_player.total_moves_winning_games = 3
        test_player.wins = 1
        test_player.calculate_average_win_moves()
        self.assertEqual(test_player.average_win_moves,
                         round(test_player.total_moves_winning_games / test_player.wins, 2))

        test_player.total_moves_winning_games = 0
        test_player.wins = 0
        test_player.calculate_average_win_moves()
        self.assertEqual(test_player.total_moves_winning_games, 0.0)

    def test_update_player_moves(self):

        test_player.total_moves = 3
        test_player.last_game_moves = 3
        expected_result = test_player.total_moves + test_player.last_game_moves

        test_player.update_player_moves()
        self.assertEqual(expected_result, test_player.total_moves)

    def test_update_percent(self):

        test_player.games = 2
        test_player.wins = 1
        test_player.ties = 1
        expected_result = '50.0%'

        function_value = test_player.update_percent(test_player.wins, test_player.games)
        self.assertEqual(expected_result, function_value)

        function_value = test_player.update_percent(test_player.ties, test_player.games)
        self.assertEqual(expected_result, function_value)

        test_player.games = 0
        test_player.wins = 0
        expected_result = '0.0%'

        function_value = test_player.update_percent(test_player.wins, test_player.games)
        self.assertEqual(expected_result, function_value)

    def test_update_scoreboard(self):

        test_player.games = 2
        test_player.wins = 1
        test_player.ties = 1
        expected_result = '50.0%'

        test_player.update_scoreboard()
        self.assertEqual(expected_result, test_player.win_percent)
        self.assertEqual(expected_result, test_player.tie_percent)

    def test_get_total_win(self):

        test_player.wins = randint(0, 10)
        test_player2.wins = randint(0, 10)
        expected_result = test_player.wins + test_player2.wins

        total.get_total_win(test_player.wins, test_player2.wins)
        self.assertEqual(expected_result, total.wins)

    def test_get_total_last_moves(self):

        test_player.last_game_moves = randint(0, 10)
        test_player2.last_game_moves = randint(0, 10)
        expected_result = test_player.last_game_moves + test_player2.last_game_moves

        total.get_total_last_moves(test_player.last_game_moves, test_player2.last_game_moves)
        self.assertEqual(expected_result, total.last_game_moves)

    def test_get_total_moves(self):

        test_player.total_moves = randint(0, 10)
        test_player2.total_moves = randint(0, 10)
        expected_result = test_player.total_moves + test_player2.total_moves

        total.get_total_moves(test_player.total_moves, test_player2.total_moves)
        self.assertEqual(expected_result, total.total_moves)

    def test_get_total_winning_moves(self):

        test_player.total_moves_winning_games = randint(0, 10)
        test_player2.total_moves_winning_games = randint(0, 10)
        expected_result = test_player.total_moves_winning_games + test_player2.total_moves_winning_games

        total.get_total_winning_moves(test_player.total_moves_winning_games, test_player2.total_moves_winning_games)
        self.assertEqual(expected_result, total.total_moves_winning_games)

    """Test "game_turn" functions"""

    def test_create_board(self):

        test_value1 = 3
        test_value2 = 1
        expected_result1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        expected_result2 = [['_']]

        function_value = game_functions.create_board(test_value1)
        self.assertEqual(expected_result1, function_value)

        function_value = game_functions.create_board(test_value2)
        self.assertEqual(expected_result2, function_value)

    def test_reset_move_count(self):

        test_player.last_game_moves = 5
        test_player2.last_game_moves = 4
        total.last_game_moves = 3

        game_functions.reset_move_count(test_player, test_player2, total)
        self.assertEqual(test_player.last_game_moves, 0)
        self.assertEqual(test_player2.last_game_moves, 0)
        self.assertEqual(total.last_game_moves, 0)

    def test_get_random_numbers(self):

        grid_size = 3
        expected_list = game_functions.get_random_numbers(grid_size)

        self.assertIn(expected_list[0], range(0, grid_size))
        self.assertIn(expected_list[1], range(0, grid_size))

    def test_check_for_available_moves(self):

        grid_size = 3

        game_board1 = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        function_value1 = game_functions.check_for_available_moves(game_board1, grid_size)

        game_board2 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        function_value2 = game_functions.check_for_available_moves(game_board2, grid_size)

        self.assertFalse(function_value1)
        self.assertTrue(function_value2)

    def test_place_mark(self):

        game_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        coordinates = [0, 0]
        symbol = 'X'
        expected_result = [['X', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

        game_functions.place_mark(game_board, coordinates, symbol)
        self.assertEqual(expected_result, game_board)


test_player = Player('Test', 'T')
test_player2 = Player('Test2', 'T2')
total = Statistics()

unittest.main()
