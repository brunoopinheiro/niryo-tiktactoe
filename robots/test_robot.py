from base_robot import BaseRobot
from pose import Pose


class TestRobot(BaseRobot):

    def __calibrate_robot(self) -> None:
        print('Calibrating...')
        print('Calibrated')

    def __init__(self) -> None:
        super().__init__()
        self.__calibrate_robot()
        self.calibrated = True

    def move_to_pose(
        self,
        pose_: dict[str, float] | list[float] | Pose,
    ) -> bool:
        try:
            print(f'Moving to position: {pose_}')
            super().move_to_pose(pose_)
            print('Successfully moved.')
            return True
        except ValueError as err:
            print(err)
            return False

    def grip(self) -> None:
        print('Closing grip')
        return super().grip()

    def release(self) -> None:
        print('Opening grip')
        return super().release()

    def close_connection(self) -> bool:
        print('Closing connection...')
        self.connected = False
        return self.connected


def main():
    e1_pose_grip_base = {"j1": -1.577, "j2": -0.496,
                         "j3": -0.703, "j4": 0.000,
                         "j5": -0.009, "j6": -0.186}

    e1_pose_intermediate_tray = {"j1": -1.577, "j2": 0.306,
                                 "j3": -0.538, "j4": 0.000,
                                 "j5": -0.907, "j6": -0.181}

    e1_pose_intermediate_board = {"j1": 0.000, "j2": 0.306,
                                  "j3": -0.538, "j4": 0.000,
                                  "j5": -0.907, "j6": -0.191}

    e1_pose_parallel_grip = {"j1": 0.000, "j2": -0.635,
                             "j3": -0.538, "j4": 0.000,
                             "j5": -0.907, "j6": -0.191}

    e1_pose_intermediate_board = {"j1": 0.000, "j2": 0.306,
                                  "j3": -0.538, "j4": 0.000,
                                  "j5": -0.907, "j6": -0.191}

    # Posição 3 do teclado numérico (Bottom right corner)
    e1_pose_board_corner = {"j1": 0.123, "j2": -1.062,
                            "j3": 0.272, "j4": -0.058,
                            "j5": -0.730, "j6": 0.095}

    test_robot = TestRobot()
    test_robot.printpose()
    test_robot.move_to_pose(e1_pose_intermediate_tray)
    test_robot.move_to_pose(e1_pose_grip_base)
    test_robot.grip()
    test_robot.trajectory_move([
        Pose.pose_from_dict(e1_pose_intermediate_tray),
        Pose.pose_from_dict(e1_pose_intermediate_board),
        Pose.pose_from_dict(e1_pose_parallel_grip),
        Pose.pose_from_dict(e1_pose_board_corner),
    ])
    test_robot.release()
    test_robot.move_to_pose(e1_pose_parallel_grip)
    test_robot.reset_state()
    test_robot.close_connection()


if __name__ == '__main__':
    main()
