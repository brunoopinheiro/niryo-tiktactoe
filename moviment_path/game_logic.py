import time
from robots.abstract_robot import AbstractRobot
import random
from path_positions import PoseCoordinates

from robots.pose import Pose

class JogoDaVelha():
    def __init__(self, game_bot: AbstractRobot):
        self.game_robot = game_bot
        self.coord = PoseCoordinates()
        
        self.posicao_campos = [[7, 8, 9],
                               [4, 5, 6],
                               [1, 2, 3]]
        self.grid = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
        self.player_move_list = {"Human": [], "Robot": []}
        self.available_positions = {7: [0,0], 8: [0,1], 9: [0,2],
                                    4: [1,0], 5: [1,1], 6: [1,2],
                                    1: [2,0], 2: [2,1], 3: [2,2]}
        
        
    def valida_jogada(self, jogada) -> int:
        """
        Valida se o valor digitado é um inteiro, mantendo o usuário em loop até digitar um valor válido
            return: jogada (int)
        """
        while ((jogada < 1) or (jogada > 9)):
            jogada = int(input('[WARNING] Valor inválido! Digite um número entre 1 e 9 para realizar sua jogada: '))
        return jogada
    
    def get_grid_positions(self, jogada) -> int|int:
        """
        Pega as posições cartesianas (x, y) de acordo com a chave passada (jogada)
            return: posicao_x (int)
            return: posicao_y (int)
        """
        positions = {
            1 : (0, 0),
            2 : (0, 1),
            3 : (0, 2),
            4 : (1, 0),
            5 : (1, 1),
            6 : (1, 2),
            7 : (2, 0),
            8 : (2, 1),
            9 : (2, 2),
        }
        play_position = positions[jogada]
        return play_position[0], play_position[1]
        
    # Acho que essa parte talvez seja deletada com a interface que bruno ta implementando.. Ou aproveitada pra imprimir a cada loop
    def print_game_grid(self) -> list:
        """
        Apresenta o grid do jogo da velha, com as posições jogadas preenchidas pelo
        símbolo respectivo à cada jogador
            return: grid (matriz)
        """
        grid = (f' {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n' 
                f'---+---+---\n'
                f' {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n'
                f'---+---+---\n'
                f' {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} \n')
        return grid
    
    def block_played_position(self, move, player) -> bool:
        """
        Verifica se a jogada passada pelo player já não foi jogada, caso não, adiciona
        a jogada à lista do player para bloquear outras jogadas naquela posição e em
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
        Verifica se na lista de jogadas de cada player, se há uma combinação de valores
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
        self.game_robot.arm.move_joints(self.robo.e1_pose_intermediate_board) #move to pose
        HUMANO = 'X'
        ROBOT = 'O'
        turn = [HUMANO, ROBOT]
        players = ['Human', 'Robot']
        turns = 0
        while turns < 9:
            cont_jogador = turns%2
            player = players[cont_jogador]
            if player == 'Human':
                pos_jogada = self.valida_jogada(int(input('Digite um número entre 1 e 9 para realizar sua jogada: ')))
                while not self.block_played_position(pos_jogada, player):
                    pos_jogada = self.valida_jogada(int(input('[WARNING] Posição ja foi escolhida! Digite outro número entre 1 e 9 para realizar sua jogada: ')))
            else:
                self.game_robot.get_game_piece() # verificar através de controlador
                self.game_robot.trajectory_move(
                    Pose.pose_from_dict(self.coord.e1_pose_intermediate_tray),
                    Pose.pose_from_dict(self.coord.e1_pose_grip_base),
                    self.game_robot.grip(),
                    Pose.pose_from_dict(self.coord.e1_pose_intermediate_tray),
                    Pose.pose_from_dict(self.coord.e1_pose_intermediate_board),
                    Pose.pose_from_dict(self.coord.e1_pose_parallel_grip)
                )
                pos_jogada = random.choice(list(self.available_positions.keys()))
                self.game_robot.paths_of_each_grid_position(pos_jogada)
                time.sleep(2)
                self.game_robot.arm.open_gripper(self.speed)
                self.game_robot.arm.move_joints(self.robo.e1_pose_intermediate_board)
                self.block_played_position(pos_jogada, player)
                
            linha, coluna = self.get_grid_positions(pos_jogada)
            self.grid[linha][coluna] = turn[cont_jogador]
            print(self.print_game_grid())
            winner = self.check_winner(self.plays[player])
            if winner:
                print(f"{players[cont_jogador]}, Você Venceu!")
                break
            turns += 1
            
        if not winner:
            print("Velha!!")
            
# Teste da classe JogoDaVelha
if __name__ == "__main__":
    # Testando a inicialização com valores válidos
    game = JogoDaVelha()
    game.play_game() # Saída: print com o vencedor ou com a msg "Empate"
            
