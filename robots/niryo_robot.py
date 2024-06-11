from robots.base_robot import BaseRobot
from pyniryo2 import NiryoRobot as Niryo

from robots.pose import Pose


ROBOT_IP = "169.254.200.200"


class NiryoRobot(BaseRobot):

    @property
    def robot(self) -> Niryo:
        return self.__robot

    @robot.setter
    def robot(self, robot_obj: Niryo) -> None:
        self.__robot = robot_obj

    def __init__(self) -> None:
        self.robot = Niryo(ROBOT_IP)
        super().__init__()
        self.robot.arm.calibrate_auto()
        self.move_to_pose_(self.position)

    def move_to_pose(self, pose_: dict[str, float] | list[float]) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        pose_list = []
        if isinstance(pose_, dict):
            pose_list = [j for j in pose_.values()]
        if isinstance(pose_, list):
            pose_list = pose_
        self.robot.arm.move_joints(pose_list)
        super().move_to_pose(pose_)

    def move_to_pose_(self, pose_: Pose) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        pose_list = pose_.joint_list()
        self.robot.arm.move_joints(pose_list)
        super().move_to_pose_(pose_)

    def grip(self) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        if not self.grip_closed:
            self.robot.tool.close_gripper()
            self.grip_closed = True

    def release(self) -> None:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        if self.grip_closed:
            self.robot.tool.open_gripper()
            self.grip_closed = False

    def close_connection(self) -> bool:
        if not self.connected:
            raise ConnectionError("Robot is not connected")
        print('Closing connection...')
        self.robot.end()
        self.connected = False
