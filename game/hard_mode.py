CORNERS = [1, 3, 7, 9]


class HardMode:

    def __init__(
        self,
        winning_combinations,
    ) -> None:
        self.win_comb = winning_combinations

    def check_win(self, player_moves):
        player = set(player_moves[1])
        robot = set(player_moves[2])
        for win_c in self.win_comb:
            count = 0
            best_play = None
            for pos in win_c:
                if pos in robot:
                    count += 1
                elif pos not in player:
                    best_play = pos
            if count == 2 and best_play is not None:
                return True, best_play
        return False, None

    def must_block(self, player_moves):
        revert_moves = {
            1: player_moves[2],
            2: player_moves[1],
        }
        win_in_1, best_play = self.check_win(revert_moves)
        return win_in_1, best_play

    def create_triangle(self, player_moves):
        pass

    def next_play(self, player_moves):
        # 1. create triangle
        # 1.1. from center
        # 1.2. from corner
        # 2. block triangle
        # 3. play in the center
        # 4. play in an empty corner
        win_in_1, best_play = self.check_win(player_moves)
        if win_in_1:
            return best_play
        block_next, best_play = self.must_block(player_moves)
        if block_next:
            return best_play
        pass
