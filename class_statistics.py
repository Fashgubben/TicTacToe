
class Statistics:
    def __init__(self):

        self.wins = 0
        self.win_percent = 0.0
        self.ties = 0
        self.tie_percent = 0.0
        self.games = 0

        self.last_game_moves = 0
        self.total_moves = 0
        self.total_moves_winning_games = 0
        self.average_win_moves = 0.0
        self.total_average_moves = 0.0

    def add_win(self):
        """Increments win attribute by 1"""

        self.wins += 1

    def add_total_move(self):
        """Increments total move attribute by 1"""

        self.total_moves += 1

    def add_last_game_moves(self):
        """Increments last game moves attribute by 1"""

        self.last_game_moves += 1

    def calculate_total_average_moves(self):
        """Calculates the average of moves per game"""

        if self.games == 0:
            self.total_average_moves = 0.0
        else:

            average_moves = self.total_moves / self.games
            self.total_average_moves = round(average_moves, 2)

    def calculate_average_win_moves(self):
        """Calculates the average moves per winning game"""

        if self.wins == 0:
            self.average_win_moves = 0.0
        else:
            average_moves = self.total_moves_winning_games / self.wins
            self.average_win_moves = round(average_moves, 2)

    def update_player_moves(self):
        """Adds last game's move to the total count"""

        self.total_moves += self.last_game_moves

    @staticmethod  # Static so it can handle both wins and ties
    def update_percent(number, games):
        """Calculates and returns a percent as a string"""

        if games > 0:
            percent = round(number / games * 100, 2)
            return f'{percent}%'
        else:
            return f'{0.0}%'

    def update_scoreboard(self):
        """Updates instance's score board"""

        self.calculate_total_average_moves()
        self.calculate_average_win_moves()
        self.win_percent = self.update_percent(self.wins, self.games)
        self.tie_percent = self.update_percent(self.ties, self.games)

    def get_total_win(self, p1_win, p2_win):
        """Sums the total win from both players"""

        self.wins = p1_win + p2_win

    def get_total_last_moves(self, p1_last_moves, p2_last_moves):
        """Sums the total tie from both players"""

        self.last_game_moves = p1_last_moves + p2_last_moves

    def get_total_moves(self, p1_moves, p2_moves):
        """Sums the total move count from both players"""

        self.total_moves = p1_moves + p2_moves

    def get_total_winning_moves(self, p1_moves, p2_moves):
        """Sums the moves in winning games from both players"""

        self.total_moves_winning_games = p1_moves + p2_moves

    def update_total(self, player_1, player_2):
        """Updates the total-instance to get the sum of both players"""

        self.get_total_win(player_1.wins, player_2.wins)
        self.get_total_last_moves(player_1.last_game_moves, player_2.last_game_moves)
        self.get_total_moves(player_1.total_moves, player_2.total_moves)
        self.get_total_winning_moves(player_1.total_moves_winning_games, player_2.total_moves_winning_games)


class Player(Statistics):
    def __init__(self, name, symbol):
        super().__init__()

        self.name = name
        self.symbol = symbol
