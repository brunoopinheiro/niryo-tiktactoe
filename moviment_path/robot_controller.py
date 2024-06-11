from robots.base_robot import BaseRobot
from coordinates.pose_calibration import CalibratedPositions
from robots.pose import Pose


class RobotController:

    @property
    def robot(self) -> BaseRobot:
        return self.__robot

    @property
    def calibrator(self) -> CalibratedPositions:
        return self.__calibrator

    @property
    def board_mapper(self) -> dict[Pose]:
        return {
            1: self.calibrator.board_bottom_left_corner,
            2: self.calibrator.board_bottom_center,
            3: self.calibrator.board_bottom_right_corner,
            4: self.calibrator.board_left_center,
            5: self.calibrator.board_center,
            6: self.calibrator.board_right_center,
            7: self.calibrator.board_top_left_corner,
            8: self.calibrator.board_top_center,
            9: self.calibrator.board_top_right_corner,
        }

    @robot.setter
    def robot(self, robot_: BaseRobot) -> None:
        self.__robot = robot_

    @calibrator.setter
    def calibrator(self, calibrator_: CalibratedPositions) -> None:
        self.__calibrator = calibrator_

    def __init__(
        self,
        robot: BaseRobot,
    ) -> None:
        self.robot = robot
        self.calibrator = CalibratedPositions()
        self.calibrator.calibration()
        self.__home: Pose = self.calibrator.intermediate_board

    def __go_to_tray(self) -> None:
        route = [
            self.calibrator.intermediate_tray,
            self.calibrator.grip_base
        ]
        self.robot.trajectory_move(route)

    def __tray_to_home(self) -> None:
        route = [
            self.calibrator.intermediate_tray,
            self.calibrator.intermediate_board,
        ]
        self.robot.trajectory_move(route)

    def __finish_turn(self) -> None:
        route = [
            self.calibrator.parallel_board,
            self.calibrator.intermediate_board,
        ]
        self.robot.trajectory_move(route)

    def __get_piece(self) -> None:
        self.__go_to_tray()
        self.robot.grip()
        self.__tray_to_home()

    def play_piece(self, board_position: int) -> None:
        self.__get_piece()
        route = [self.calibrator.parallel_board]
        pos = self.board_mapper[board_position]
        route.append(pos)
        self.robot.trajectory_move(route)
        self.robot.release()

        self.__finish_turn()

    def go_iddle(self) -> None:
        self.robot.move_to_pose_(
            self.calibrator.intermediate_board
        )
