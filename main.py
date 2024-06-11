from robots.test_robot import TestRobot
from robots.niryo_robot import NiryoRobot
from game.tictactoe import TicTacToe


def main():
    robot = None
    print('[1] - TestRobot')
    print('[2] - NiryoRobot')
    choice = int(input("Escolha o robô: "))
    if choice == 1:
        robot = TestRobot()
    if choice == 2:
        robot = NiryoRobot()
    hardmode = True
    mode = input('Hard mode? [S/N]')
    if mode == 'N' or mode == 'n':
        hardmode = False
    first = input('Quem começa? 1 - Jogador, 2 - Robô >>')
    if first not in ('1', '2'):
        first = None
    else:
        first = int(first)
    game = TicTacToe(robot, hardmode, first)
    game.play_game()


if __name__ == '__main__':
    main()
