from abc import ABC, abstractmethod
from robots.pose import Pose
from functools import singledispatchmethod


class AbstractRobot(ABC):

    @property
    def connected(self) -> bool:
        return self.__connected

    @property
    def calibrated(self) -> bool:
        return self.__calibrated

    @property
    def learning(self) -> bool:
        return self.__learning

    @property
    def velocity(self) -> int:
        return self.__velocity

    @property
    def grip_closed(self) -> bool:
        return self.__closed

    @property
    def position(self) -> Pose:
        return self.__position

    @connected.setter
    def connected(self, value: bool) -> None:
        self.__connected = value

    @calibrated.setter
    def calibrated(self, value: bool) -> None:
        self.__calibrated = value

    @learning.setter
    def learning(self, value: bool) -> None:
        self.__learning = value

    @velocity.setter
    def velocity(self, value: int) -> None:
        """Sets the arm max velocity

        Args:
            value (float): a percentage value
        """
        if value < 1 or value > 100:
            raise ValueError('Velocity not supported')
        self.__velocity = value

    @grip_closed.setter
    def grip_closed(self, value: bool) -> None:
        self.__closed = value

    @singledispatchmethod
    @position.setter
    def position(self, new_pos: object) -> None:
        raise NotImplementedError('Unsupported Type')

    @position.register
    def _(self, new_pos: dict[str, float]) -> None:
        self.position = Pose.pose_from_dict(new_pos)

    @position.register
    def _(self, new_pos: list[float]) -> None:
        self.position = Pose(*new_pos)

    @abstractmethod
    def __calibrate_robot() -> None:
        raise NotImplementedError

    @abstractmethod
    def printpose() -> str:
        raise NotImplementedError

    @abstractmethod
    def move_to_pose(pose_: Pose) -> bool:
        # should be used with robot joints
        raise NotImplementedError

    @abstractmethod
    def grip() -> None:
        raise NotImplementedError

    @abstractmethod
    def release() -> None:
        raise NotImplementedError

    @abstractmethod
    def trajectory_move(poses: list[Pose]) -> None:
        """With a given list of poses, executes a
        series of movements in the given order.

        Args:
            poses (list[Pose]): a list of Poses
        """
        raise NotImplementedError

    @abstractmethod
    def close_connection() -> bool:
        raise NotImplementedError
