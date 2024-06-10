from robots.test_robot import TestRobot
from robots.niryo_robot import NiryoRobot
from moviment_path.game_logic import JogoDaVelha


def main():
    robot = None
    print('[1] - TestRobot')
    print('[2] - NiryoRobot')
    choice = int(input("Escolha o robô: "))
    if choice == 1:
        robot = TestRobot()
    if choice == 2:
        robot = NiryoRobot()
    game = JogoDaVelha(robot)
    game.play_game()


if __name__ == '__main__':
    main()
