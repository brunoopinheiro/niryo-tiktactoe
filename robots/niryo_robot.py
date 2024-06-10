from base_robot import BaseRobot
from pyniryo2 import (NiryoRobot, RobotErrors)

from robots.pose import Pose


ROBOT_IP = "169.254.200.200"


class NiryoRobot_(BaseRobot):

    @property
    def robot(self) -> NiryoRobot:
        return self.__robot

    @robot.setter
    def robot(self, robot_obj: NiryoRobot) -> None:
        self.__robot = robot_obj

    @staticmethod
    def __calibration_callback(result) -> None:
        if result["status"] < RobotErrors.SUCCESS.value:
            return False
        else:
            return True

    def __calibrate_robot(self) -> bool:
        result = self.robot.arm.calibrate_auto(
            self.__calibration_callback
        )
        return result

    def __init__(self) -> None:
        self.robot = NiryoRobot(ROBOT_IP)
        super().__init__()
        result = False
        while result is not True:
            result = self.__calibrate_robot()
            self.calibrated = result

    def move_to_pose(self, pose_: dict[str, float] | list[float]) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        pose_list = []
        if isinstance(pose_, dict):
            pose_list = [j for j in pose_.values()]
        if isinstance(pose_, list):
            pose_list = pose_
        print(f'Moving to point: {pose_list}')
        self.robot.arm.move_joints(pose_list)
        super().move_to_pose(pose_)

    def move_to_pose_(self, pose_: Pose) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        pose_list = pose_.joint_list()
        print(f'Moving to point: {pose_list}')
        self.robot.arm.move_joints(pose_list)
        super().move_to_pose_(pose_)

    def grip(self) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        if not self.grip_closed:
            print("Grasping")
            self.robot.tool.close_gripper()
            self.grip_closed = True

    def release(self) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        if self.grip_closed:
            print("Releasing")
            self.robot.tool.open_gripper()
            self.grip_closed = False

    def close_connection(self) -> bool:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        print('Closing connection...')
        self.robot.end()
        self.connected = False
