import game_functions
from class_statistics import Statistics, Player
from check_for_winner import check_for_winner
from statistic_table import create_terminal_table, print_table, stat_gui
from check_input import get_valid_coordinates


def create_players():
    """Creates and returns two player objects"""

    print('\n' + 'TIC TAC TOE'.center(23, '-'))
    name_1 = input('Enter name of Player 1: ').title()
    print('\nEnter "Skynet" to play against a computer.')
    name_2 = input('Enter name of Player 2: ').title()
    return Player(name_1, 'X'), Player(name_2, 'O'), Statistics()


def print_menu():
    """Prints out a menu"""

    print('\n' + 'TIC TAC TOE'.center(23, '-'))
    print('[1] - Play Tic Tac Toe\n[2] - View scoreboard\n[3] - View game history')
    print('[4] - Clear game history\n[5] - Quit')
    return input('\nEnter a menu number: ')


def menu_choices():
    """Program menu choices"""

    while True:

        users_choice = print_menu()

        # Play a game
        if users_choice == '1':

            grid_size = game_functions.get_grid_size()
            game_board = game_functions.create_board(grid_size)
            game_functions.reset_move_count(player_1, player_2, total)

            play_game = True
            while play_game:

                for player in player_list:

                    if player.name != 'Skynet':
                        game_functions.print_board(game_board, grid_size, player_1, player_2)

                    if game_functions.check_for_available_moves(game_board, grid_size):

                        # Get coordinates from players
                        while True:
                            try:
                                if player.name == 'Skynet':
                                    coordinates = game_functions.get_computer_coordinates(player, grid_size, game_board)
                                else:
                                    player_input = game_functions.get_input(player)
                                    coordinates = get_valid_coordinates(game_board, grid_size, player_input,
                                                                        player.name)

                                game_functions.place_mark(game_board, coordinates, player.symbol)
                                player.add_last_game_moves()
                                break

                            except ValueError as error_message:
                                print(error_message)

                        if check_for_winner(game_board, grid_size, player.symbol):
                            game_functions.print_board(game_board, grid_size, player_1, player_2)
                            print(f'\nCongratulations {player.name}! You are the winner!')

                            # Update statistics
                            player.add_win()
                            player.total_moves_winning_games += player.last_game_moves
                            game_functions.update_stats(player_1, player_2, total)

                            # Save game board
                            game_was_won = True
                            game_functions.save_game_result(game_board, player, player_1, player_2, grid_size,
                                                            game_was_won)

                            play_game = False
                            break

                    else:  # If it's a draw
                        print('\nThe game is a tie! No one is a loser today!')

                        # Update statistics when it's a draw
                        game_functions.update_stats_tie(player_1, player_2, total)
                        game_functions.update_stats(player_1, player_2, total)

                        # Save game board
                        game_was_won = False
                        game_functions.save_game_result(game_board, player, player_1, player_2, grid_size, game_was_won)

                        play_game = False

        # View statistics
        elif users_choice == '2':

            # Open gui-table
            stat_gui(player_1, player_2, total)

            # Print the statistics table
            table = create_terminal_table(player_1, player_2, total)
            print_table(table)

        # Print game history
        elif users_choice == '3':

            print('\n' + 'TIC TAC TOE'.center(23, '-'))
            print_game_history()

        # Clear game history
        elif users_choice == '4':

            print('\n' + 'TIC TAC TOE'.center(23, '-'))
            clear_game_history()

        # Close game
        elif users_choice == '5':
            print('Good bye!')
            break

        else:
            print('Please use a number from the menu.')


def print_game_history():
    """Prints all played games"""

    with open('game_history.txt', 'r', encoding='utf-8') as saved_games:
        for line in saved_games.readlines():
            print(line.rstrip('\n'))

        input('\n-Press enter to continue-')


def clear_game_history():
    """Clears the game history text-file"""

    with open('game_history.txt', 'w', encoding='utf-8') as saved_games:
        saved_games.write('')
    print('\nGame history cleared!')


if __name__ == '__main__':

    (player_1, player_2, total) = create_players()
    player_list = [player_1, player_2]

    menu_choices()