from __future__ import annotations
from functools import singledispatchmethod


class Pose:

    @property
    def j1(self) -> float:
        return self.__j1

    @property
    def j2(self) -> float:
        return self.__j2

    @property
    def j3(self) -> float:
        return self.__j3

    @property
    def j4(self) -> float:
        return self.__j4

    @property
    def j5(self) -> float:
        return self.__j5

    @property
    def j6(self) -> float:
        return self.__j6

    @j1.setter
    def j1(self, value: float) -> None:
        # target for refactor: better limit code
        j1l = -2.97
        j1u = 2.97
        if value <= j1l or value >= j1u:
            raise ValueError(f'Joint position not allowed. J-1[{j1l}, {j1u}]')
        self.__j1 = value

    @j2.setter
    def j2(self, value: float) -> None:
        j2l = -2.09
        j2u = 0.61
        if value <= j2l or value >= j2u:
            raise ValueError(f'Joint position not allowed. J-2[{j2l}, {j2u}]')
        self.__j2 = value

    @j3.setter
    def j3(self, value: float) -> None:
        j3l = -1.34
        j3u = 1.57
        if value <= j3l or value >= j3u:
            raise ValueError(f'Joint position not allowed. J-3[{j3l}, {j3u}]')
        self.__j3 = value

    @j4.setter
    def j4(self, value: float) -> None:
        j4l = -2.09
        j4u = 2.09
        if value <= j4l or value >= j4u:
            raise ValueError(f'Joint position not allowed. J-4[{j4l}, {j4u}]')
        self.__j4 = value

    @j5.setter
    def j5(self, value: float) -> None:
        j5l = -1.75
        j5u = 0.96
        if value <= j5l or value >= j5u:
            raise ValueError(f'Joint position not allowed. J-5[{j5l}, {j5u}]')
        self.__j5 = value

    @j6.setter
    def j6(self, value: float) -> None:
        j6l = -2.53
        j6u = 2.53
        if value <= j6l or value >= j6u:
            raise ValueError(f'Joint position not allowed. J-6[{j6l}, {j6u}]')
        self.__j6 = value

    def __init__(
        self,
        j1: float,
        j2: float,
        j3: float,
        j4: float,
        j5: float,
        j6: float,
    ) -> None:
        self.j1 = j1
        self.j2 = j2
        self.j3 = j3
        self.j4 = j4
        self.j5 = j5
        self.j6 = j6

    @staticmethod
    def pose_from_dict(pose_: dict[str, float]) -> Pose:
        new_pose = Pose(
            j1=pose_['j1'],
            j2=pose_['j2'],
            j3=pose_['j3'],
            j4=pose_['j4'],
            j5=pose_['j5'],
            j6=pose_['j6'],
        )
        return new_pose

    def __str__(self) -> str:
        return f'{self.j1},{self.j2},{self.j3},{self.j4},{self.j5},{self.j6}'

    def joint_list(self) -> list[float]:
        return [
            self.j1,
            self.j2,
            self.j3,
            self.j4,
            self.j5,
            self.j6,
        ]

    @singledispatchmethod
    def update(
        self,
        pose_: object
    ) -> None:
        raise NotImplementedError('Unsupported Type')

    @update.register
    def _(
        self,
        pose: dict,
    ) -> None:
        self.j1 = pose['j1']
        self.j2 = pose['j2']
        self.j3 = pose['j3']
        self.j4 = pose['j4']
        self.j5 = pose['j5']
        self.j6 = pose['j6']

    @update.register
    def _(
        self,
        pose: list,
    ) -> None:
        self.j1 = pose[0]
        self.j2 = pose[1]
        self.j3 = pose[2]
        self.j4 = pose[3]
        self.j5 = pose[4]
        self.j6 = pose[5]

    def update_(
        self,
        pose: Pose,
    ) -> None:
        self.j1 = pose.j1
        self.j2 = pose.j2
        self.j3 = pose.j3
        self.j4 = pose.j4
        self.j5 = pose.j5
        self.j6 = pose.j6

    def __sub__(self, other):
        if type(other) is dict:
            j1 = round(self.j1 - other['j1'], 3)
            j2 = round(self.j2 - other['j2'], 3)
            j3 = round(self.j3 - other['j3'], 3)
            j4 = round(self.j4 - other['j4'], 3)
            j5 = round(self.j5 - other['j5'], 3)
            j6 = round(self.j6 - other['j6'], 3)
        else:
            j1 = round(self.j1 - other.j1, 3)
            j2 = round(self.j2 - other.j2, 3)
            j3 = round(self.j3 - other.j3, 3)
            j4 = round(self.j4 - other.j4, 3)
            j5 = round(self.j5 - other.j5, 3)
            j6 = round(self.j6 - other.j6, 3)
        return Pose(j1, j2, j3, j4, j5, j6)

    def __add__(self, other):
        if type(other) is dict:
            j1 = round(self.j1 + other['j1'], 3)
            j2 = round(self.j2 + other['j2'], 3)
            j3 = round(self.j3 + other['j3'], 3)
            j4 = round(self.j4 + other['j4'], 3)
            j5 = round(self.j5 + other['j5'], 3)
            j6 = round(self.j6 + other['j6'], 3)
        else:
            j1 = round(self.j1 + other.j1, 3)
            j2 = round(self.j2 + other.j2, 3)
            j3 = round(self.j3 + other.j3, 3)
            j4 = round(self.j4 + other.j4, 3)
            j5 = round(self.j5 + other.j5, 3)
            j6 = round(self.j6 + other.j6, 3)
        return Pose(j1, j2, j3, j4, j5, j6)


if __name__ == '__main__':
    e1_pose_grip_base = {"j1": -1.577, "j2": -0.496,
                         "j3": -0.703, "j4": 0.000,
                         "j5": -0.009, "j6": -0.186}

    e1_pose_intermediate_tray = {"j1": -1.577, "j2": 0.306,
                                 "j3": -0.538, "j4": 0.000,
                                 "j5": -0.907, "j6": -0.181}

    e1_pose_parallel_grip = {"j1": 0.000, "j2": -0.635,
                             "j3": -0.538, "j4": 0.000,
                             "j5": -0.907, "j6": -0.191}

    # creating pose from dict
    pose1 = Pose(**e1_pose_grip_base)
    print(pose1)

    # creating pose from list
    j_list = list(e1_pose_grip_base.values())
    pose2 = Pose(*j_list)
    print(pose2)

    # updating pose from dict
    pose1.update(e1_pose_intermediate_tray)
    print(pose1)
    # updating pose from list
    j_list = list(e1_pose_intermediate_tray.values())
    pose2.update(j_list)
    print(pose2)
    # updating pose from Pose
    pose3 = Pose.pose_from_dict(e1_pose_parallel_grip)
    print('Pose1: ', pose1)
    print('Pose3: ', pose3)
    print('Updating pose from Pose obj')
    pose1.update_(pose3)
    print('Pose1: ', pose1)
