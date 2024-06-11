from robots.base_robot import BaseRobot
from moviment_path.robot_controller import RobotController
from game.hard_mode import HardMode
from random import choice


class TicTacToe:

    @property
    def __boardmap(self) -> dict[int, tuple[int, int]]:
        return {
            1: (2, 0),
            2: (2, 1),
            3: (2, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (0, 0),
            8: (0, 1),
            9: (0, 2),
        }

    @property
    def __winning_combinations(self) -> list[list[tuple[int, int]]]:
        return [
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],  # diagonals
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],  # columns
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],  # rows
        ]

    @property
    def __sampleboard(self) -> list[list[int]]:
        return [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3],
        ]

    @property
    def __initialboard(self) -> list[list[str]]:
        return [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    @property
    def player_moves(self) -> dict[int, list[tuple[int, int]]]:
        return self.__playermoves

    @property
    def gamerobot(self) -> BaseRobot:
        return self.__robot

    @gamerobot.setter
    def gamerobot(self, robot: BaseRobot) -> None:
        self.__robot = robot

    @player_moves.setter
    def player_moves(self, moves: dict[int, list[tuple[int, int]]]) -> None:
        self.__playermoves = moves

    def __init__(self, robot: BaseRobot, first=None) -> None:
        self.__marks = [' ', 'X', 'O']
        self.__board = self.__initialboard
        self.__playermoves = {1: [], 2: []}
        self.gamerobot = robot
        self.__controller = RobotController(self.gamerobot)
        self.__available = self.__boardmap
        self.__count = 1
        if first is None:
            first = choice([1, 2])
        self.__play_mode = HardMode(self.__winning_combinations)
        self.__player = first

    @staticmethod
    def __printboard(board) -> None:
        print(' {} | {} | {} '.format(*board[0]))
        print('---+---+---')
        print(' {} | {} | {} '.format(*board[1]))
        print('---+---+---')
        print(' {} | {} | {} '.format(*board[2]))

    def __nextplayer(self):
        self.__count += 1
        self.__player = 2 if self.__player == 1 else 1

    def __getmovekey(self, move):
        for key, value in self.__available.items():
            if value == move:
                return key

    def __registerplay(self, move: tuple[int, int]):
        p = self.__player
        self.player_moves[p].append(move)
        key = self.__getmovekey(move)
        self.__available.pop(key)

    def __setboard(self, newboard):
        self.__board = newboard
        self.__nextplayer()

    def __getplay(self):
        playermark = self.__marks[self.__player]
        newboard = self.__board
        try:
            play = int(input('Digite sua jogada: '))
            i, j = self.__boardmap[play]
            if self.__board[i][j] != ' ':
                raise AssertionError
            newboard[i][j] = playermark
            return (True, newboard, (i, j))
        except (ValueError, AssertionError):
            print('Jogada Inválida')
            return (False, self.__board, (-1, -1))

    def __robotplay(self, play: int):
        playermark = self.__marks[self.__player]
        newboard = self.__board
        try:
            i, j = self.__available[play]
            if self.__board[i][j] != ' ':
                raise SystemError("This shouldn't have happened.")
            newboard[i][j] = playermark
            return (True, newboard, (i, j))
        except SystemError as err:
            print(err)
            return (False, self.__board, (-1, -1))

    def __assert_endgame(self) -> tuple[bool, int]:
        if self.__count == 10:
            return (True, None)
        p1_moves = self.player_moves[1]
        p2_moves = self.player_moves[2]

        for win_c in self.__winning_combinations:
            set_win_c = set(win_c)
            if set_win_c.issubset(p1_moves):
                return (True, 1)
            if set_win_c.issubset(p2_moves):
                return (True, 2)

        return (False, None)

    def play_game(self):
        print('TIC TAC TOE')
        print('As coordenadas do jogo são:\n')
        self.__printboard(self.__sampleboard)
        print('\n')

        stop = False
        while stop is False:
            print('======')
            print(f'Rodada: {self.__count}')
            self.__printboard(self.__board)
            stop, winner = self.__assert_endgame()

            if stop is False:
                if self.__player == 1:
                    print('Sua vez, Jogador!')
                    valid, newboard, move = self.__getplay()
                    if valid:
                        self.__registerplay(move)
                        self.__setboard(newboard)
                else:
                    # play = choice(list(self.__available.keys()))
                    play = self.__play_mode.get_nextplay(self.player_moves)
                    print(play)
                    print(f'AvailableMoves: {self.__available}')
                    print(play)
                    valid, newboard, move = self.__robotplay(play)
                    if valid:
                        # play_key = self.__getmovekey(move)
                        self.__controller.play_piece(play)
                        self.__registerplay(move)
                        self.__setboard(newboard)

            if stop is True:
                if winner is None:
                    print('Deu velha! Tente novamente!')
                elif winner == 1:
                    print('Parabéns, você venceu o robô!')
                else:
                    print('Eita, parace que não foi dessa vez...')
