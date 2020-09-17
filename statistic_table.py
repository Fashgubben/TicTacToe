import pandas as pd
import numpy as np
from appJar import gui


def stat_gui(player_1, player_2, total):
    """Creates and opens a gui data frame with all the player stats"""

    app = gui()
    app.setBg('darkgray')
    app.startFrame('top', 0, 0)
    app.startLabelFrame("")
    app.setPadding(5, 5)
    app.setBg('silver')
    app.setSticky('e')

    # Titles
    app.addLabel('empty_0', '', 0, 0)
    column_titles = ['Win', 'Win %', 'Tie', 'Tie %', 'Tot. Games', 'Tot. Moves', 'Avg. Win Moves', 'Avg. Moves']
    row_titles = [f'Player 1 ({player_1.name}): ', f'Player 2 ({player_2.name}): ', 'Total: ']

    column_counter = 1
    for title in column_titles:
        app.addLabel(title, title, 0, column_counter).config(font="Courier 13 bold underline")
        column_counter += 1

    row_counter = 1
    for title in row_titles:
        app.addLabel(title, title, row_counter, 0).config(font="Courier 13 bold")
        row_counter += 1

    # Statistic values
    stats = [('p1_win', player_1.wins), ('p1_win_%', player_1.win_percent), ('p1_tie', player_1.ties),
             ('p1_tie_%', player_1.tie_percent), ('p1_games', player_1.games), ('p1_moves', player_1.total_moves),
             ('p1_avg_win_moves', player_1.average_win_moves), ('p1_avg_moves', player_1.total_average_moves),
             ('p2_win', player_2.wins), ('p2_win_%', player_2.win_percent), ('p2_tie', player_2.ties),
             ('p2_tie_%', player_2.tie_percent), ('p2_games', player_2.games), ('p2_moves', player_2.total_moves),
             ('p2_avg_win_moves', player_2.average_win_moves), ('p2_avg_moves', player_2.total_average_moves),
             ('total_win', total.wins), ('total_win_%', total.win_percent), ('total_tie', total.ties),
             ('total_tie_%', total.tie_percent), ('total_games', total.games), ('total_moves', total.total_moves),
             ('total_avg_win_moves', total.average_win_moves), ('total_avg_moves', total.total_average_moves)]

    column_counter = 1
    row_counter = 1
    for value in stats:
        app.addLabel(value[0], value[1], row_counter, column_counter)
        column_counter += 1

        if column_counter == 9:
            column_counter = 1
            row_counter += 1

    app.stopLabelFrame()
    app.stopFrame()

    # Button
    app.startFrame('bottom', 1, 0)
    app.addLabel('left_filler1', '', 1, 0)
    app.addLabel('left_filler2', '', 1, 1)
    app.addLabel('left_filler3', '', 1, 2)
    app.addButton('OK', app.stop, 1, 3)
    app.setButtonBg('OK', 'silver')
    app.addLabel('right_filler1', '', 1, 4)
    app.addLabel('right_filler2', '', 1, 5)
    app.addLabel('right_filler3', '', 1, 6)
    app.stopFrame()

    app.go()


def create_terminal_table(player_1, player_2, total):
    """Creates a data frame with all the player stats"""

    pd.set_option('display.max_columns', 8)
    pd.set_option('display.width', 100)

    column_title = ['| Win', '| Win %', '| Tie', '| Tie %', '| Tot.Games',
                    '| Tot.moves', '| Avg.win moves', '| Avg.moves']

    row_title = [f'P1 ({player_1.name}):', f'P2 ({player_2.name}):', '--------', 'Total:']

                        # Player 1's score
    all_score_values = [player_1.wins, player_1.win_percent, player_1.ties, player_1.tie_percent,
                        player_1.games, player_1.total_moves, player_1.average_win_moves,
                        player_1.total_average_moves,

                        # Player 2's score
                        player_2.wins, player_2.win_percent, player_2.ties, player_2.tie_percent,
                        player_2.games, player_2.total_moves, player_2.average_win_moves,
                        player_2.total_average_moves,

                        # Seperator
                        '-', '-', '-', '-', '-', '-', '-', '-',

                        # Total score
                        total.wins, total.win_percent, total.ties, total.tie_percent, total.games,
                        total.total_moves, total.average_win_moves, total.total_average_moves]

    numpy_array = np.asarray(all_score_values).reshape(4, 8)
    statistics_table = pd.DataFrame(numpy_array, index=row_title, columns=column_title)

    return statistics_table


def print_table(stats_table):
    """Prints the data frame with all the player stats"""

    print('\n' + 'TIC TAC TOE'.center(23, '-'))
    print('STATS'.center(23, ' ') + '\n')
    print(stats_table)
    input('\n-Press enter to continue-')


