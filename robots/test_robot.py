from robots.base_robot import BaseRobot
from robots.pose import Pose
from time import sleep


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
            sleep(0.5)
            return True
        except ValueError as err:
            print(err)
            return False

    def move_to_pose_(self, pose_: Pose) -> None:
        print('Moving to pose: ', pose_)
        sleep(0.5)
        return super().move_to_pose_(pose_)

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
