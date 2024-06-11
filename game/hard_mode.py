from random import choice


CORNERS = [1, 3, 7, 9]


class HardMode:

    @property
    def inverse_mapper(self) -> dict[tuple[int, int], int]:
        return {
            (2, 0): 1,
            (2, 1): 2,
            (2, 2): 3,
            (1, 0): 4,
            (1, 1): 5,
            (1, 2): 6,
            (0, 0): 7,
            (0, 1): 8,
            (0, 2): 9,
        }

    @property
    def corners(self) -> list[tuple[int, int]]:
        #         1       3        7       9
        return [(2, 0), (2, 2), (0, 0), (0, 2)]

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
        robot = set(player_moves[2])
        player = set(player_moves[1])
        for play in robot:
            if play in self.corners:
                if (play in (self.corners[0], self.corners[-1])):
                    next_play = (play[1], play[0])
                    if next_play not in player and next_play not in robot:
                        return True, next_play
                if play == self.corners[1]:
                    next_play = self.corners[2]
                    if next_play not in player and next_play not in robot:
                        return True, next_play
                if play == self.corners[2]:
                    next_play = self.corners[1]
                    if next_play not in play and next_play not in robot:
                        return True, next_play
        return False, None

    def block_triangle(self, player_moves):
        revert_moves = {
            1: player_moves[2],
            2: player_moves[1]
        }
        return self.create_triangle(revert_moves)

    def empty_center(self, player_moves):
        center = (1, 1)
        if center not in player_moves[1] and center not in player_moves[2]:
            return True, center
        return False, None

    def empty_corner(self, player_moves):
        robot = set(player_moves[2])
        player = set(player_moves[1])
        valid = False
        next_play = None
        for _ in range(len(self.corners)):
            next_play = choice(self.corners)
            if next_play not in robot and next_play not in player:
                valid = True
        return valid, next_play

    def best_choice(self, player_moves):
        win_in_1, best_play = self.check_win(player_moves)
        if win_in_1:
            print('Winning in next move')
            return best_play
        block_next, best_play = self.must_block(player_moves)
        if block_next:
            print('Blocking player win')
            return best_play
        # 1. create triangle
        triangle, next_play = self.create_triangle(player_moves)
        if triangle:
            print('Creating a triangle')
            return next_play
        # 2. block triangle
        blocK_triangle, next_play = self.block_triangle(player_moves)
        if blocK_triangle:
            print('Blocking a triangle')
            return next_play
        # 3. play in the center
        empty_center, next_play = self.empty_center(player_moves)
        if empty_center:
            print('Empty center')
            return next_play
        # 4. play in an empty corner
        empty_corner, next_play = self.empty_corner(player_moves)
        if empty_corner:
            print('Empty corner')
            return next_play
        print('Chosing a random position should not happen')
        return choice(list(self.inverse_mapper))

    def get_nextplay(self, player_moves):
        next_play = self.best_choice(player_moves)
        return self.inverse_mapper[next_play]
