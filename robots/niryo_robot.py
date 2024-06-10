from base_robot import BaseRobot
from pyniryo2 import NiryoRobot

from robots.pose import Pose


ROBOT_IP = "169.254.200.200"


class NiryoRobot_(BaseRobot):

    @property
    def robot(self) -> NiryoRobot:
        return self.__robot

    @robot.setter
    def robot(self, robot_obj: NiryoRobot) -> None:
        self.__robot = robot_obj

    def __init__(self) -> None:
        self.robot = NiryoRobot(ROBOT_IP)
        super().__init__()
        self.robot.arm.calibrate_auto()
        self.calibrated = True

    def move_to_pose(self, pose_: dict[str, float] | list[float]) -> None:
        pose_list = []
        if isinstance(pose_, dict):
            pose_list = [j for j in pose_.values()]
        if isinstance(pose_, list):
            pose_list = pose_
        self.robot.arm.move_joints(pose_list)
        super().move_to_pose(pose_)

    def move_to_pose_(self, pose_: Pose) -> None:
        pose_list = pose_.joint_list()
        self.robot.arm.move_joints(pose_list)
        super().move_to_pose_(pose_)

    def grip(self) -> None:
        if not self.grip_closed:
            self.robot.tool.close_gripper()
            self.grip_closed = True

    def release(self) -> None:
        if self.grip_closed:
            self.robot.tool.open_gripper()
            self.grip_closed = False
