from abstract_robot import AbstractRobot
from pose import Pose

# same as e1_pose_intermediate_board
BASEPOSE = {
    "j1": 0.000,
    "j2": 0.306,
    "j3": -0.538,
    "j4": 0.000,
    "j5": -0.907,
    "j6": -0.191,
}


class BaseRobot(AbstractRobot):

    @property
    def last_position(self) -> Pose:
        return self.__lastpose

    @last_position.setter
    def last_position(self, pose: Pose) -> None:
        self.__lastpose = pose

    def __init__(
        self,
    ) -> None:
        self.connected = True
        self.calibrated = False
        self.grip_closed = False
        self.learning = False
        # basepose = Pose.pose_from_dict(BASEPOSE)
        self.position = Pose(**BASEPOSE)
        self.last_position = self.position
        self.velocity = 80

    def printpose(self) -> str:
        print(self.position)

    def move_to_pose(
        self,
        pose_: dict[str, float] | list[float],
    ) -> bool:
        self.position.update_(pose_)

    def grip(self) -> None:
        if not self.grip_closed:
            self.grip_closed = True

    def release(self) -> None:
        if self.grip_closed:
            self.grip_closed = False

    def trajectory_move(self, poses: list[Pose]) -> None:
        try:
            for pose in poses:
                self.last_position.update_(pose)
                self.move_to_pose(pose)
        except ValueError as err:
            print(err)

    def reset_state(self) -> None:
        self.move_to_pose(BASEPOSE)
        self.release()
