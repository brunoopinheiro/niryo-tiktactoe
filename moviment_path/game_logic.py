import random
from robots.base_robot import BaseRobot
from moviment_path.robot_controller import RobotController


class JogoDaVelha():

    @property
    def board_positions(self) -> list[list[int]]:
        return self.__board_positions

    @property
    def game_robot(self) -> BaseRobot:
        return self.__robot

    @property
    def grid(self) -> list[list[str]]:
        return self.__grid

    @property
    def player_move_list(self) -> dict[str, list[str]]:
        return self.__playermoves

    @property
    def available_positions(self) -> dict[int, list[int]]:
        return self.__availablepositions

    @game_robot.setter
    def game_robot(self, game_bot: BaseRobot) -> None:
        self.__robot = game_bot

    @board_positions.setter
    def board_positions(self, board_pos: list[list[int]]) -> None:
        self.__board_positions = board_pos

    @grid.setter
    def grid(self, grid_pos: list[list[str]]) -> None:
        self.__grid = grid_pos

    @player_move_list.setter
    def player_move_list(self, move_list: dict[str, list[str]]) -> None:
        self.__playermoves = move_list

    @available_positions.setter
    def available_positions(self, available_pos: dict[int, list[int]]) -> None:
        self.__availablepositions = available_pos

    def __init__(self, game_bot: BaseRobot):
        self.game_robot = game_bot
        self.__controller = RobotController(self.game_robot)
        self.board_positions = [[7, 8, 9],
                                [4, 5, 6],
                                [1, 2, 3]]
        self.grid = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]
        self.player_move_list = {"Human": [], "Robot": []}
        self.available_positions = {7: [0, 0], 8: [0, 1], 9: [0, 2],
                                    4: [1, 0], 5: [1, 1], 6: [1, 2],
                                    1: [2, 0], 2: [2, 1], 3: [2, 2]}

    def valida_jogada(self, jogada) -> int:
        """
        Valida se o valor digitado é um inteiro,
        mantendo o usuário em loop até digitar um valor válido
            return: jogada (int)
        """
        msg = '''[WARNING] Valor inválido! Digite um número entre 1 e 9
        para realizar sua jogada: '''
        while ((jogada < 1) or (jogada > 9)):
            jogada = int(input(msg))
        return jogada

    def get_grid_positions(self, jogada) -> tuple[int, int]:
        """
        Pega as posições cartesianas (x, y)
        de acordo com a chave passada (jogada)
            return: posicao_x (int)
            return: posicao_y (int)
        """
        positions = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2),
        }
        play_position = positions[jogada]
        return play_position[0], play_position[1]

    def print_game_grid(self) -> str:
        """Apresenta o grid do jogo da velha,
        com as posições jogadas preenchidas pelo
        símbolo respectivo à cada jogador

        Returns:
            list: str (matriz)
        """
        grid = (
            f' {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]}\n'
            f'---+---+---\n'
            f' {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]}\n'
            f'---+---+---\n'
            f' {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]}\n'
            )
        print(grid)

    def block_played_position(self, move, player) -> bool:
        """
        Verifica se a jogada passada pelo player já não foi jogada,
        caso não, adiciona a jogada à lista do player
        para bloquear outras jogadas naquela posição e em
        seguida retira da lista de jogadas disponíveis
            return: bool
        """
        for player in self.player_move_list:
            if move in self.player_move_list[player]:
                return False
        self.player_move_list[player].append(move)
        self.available_positions.pop(move)
        return True

    def check_winner(self, player_move_list):
        """
        Verifica se na lista de jogadas de cada player,
        se há uma combinação de valores
        que dá match com alguma das sequências de vitória
            return: bool
        """
        winning_sequences = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Linhas
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Colunas
            [7, 5, 3], [1, 5, 9]  # Diagonais
        ]
        for sequence in winning_sequences:
            if all(item in player_move_list for item in sequence):
                return True
        return False

    def play_game(self):
        self.__controller.go_iddle()
        HUMANO = 'X'
        ROBOT = 'O'
        turn = [HUMANO, ROBOT]
        players = ['Human', 'Robot']
        turns = 0
        self.print_game_grid()
        while turns < 9:
            cont_jogador = turns % 2
            player = players[cont_jogador]
            if player == 'Human':
                msg = 'Digite um número entre 1 e 9 para realizar sua jogada: '
                pos_jogada = self.valida_jogada(int(input(msg)))
                while not self.block_played_position(pos_jogada, player):
                    warning = '[WARNING] Posição ja foi escolhida! '
                    pos_jogada = self.valida_jogada(int(input(warning)))
            else:
                pos_jogada = random.choice(
                    list(self.available_positions.keys())
                )
                self.__controller.play_piece(pos_jogada)
                self.block_played_position(pos_jogada, player)

            linha, coluna = self.get_grid_positions(pos_jogada)
            self.grid[linha][coluna] = turn[cont_jogador]
            self.print_game_grid()
            winner = self.check_winner(self.player_move_list[player])
            if winner:
                print(f"{players[cont_jogador]}, Você Venceu!")
                break
            turns += 1

        if not winner:
            print("Velha!!")
