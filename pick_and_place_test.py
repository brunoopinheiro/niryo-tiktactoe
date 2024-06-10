from robots.pose import Pose
from robots.niryo_robot import NiryoRobot


def main():
    # Trying with absolute positions
    # Should be replaced with relative poses
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

    robot = NiryoRobot()
    robot.printpose()
    robot.move_to_pose(e1_pose_intermediate_tray)
    robot.move_to_pose(e1_pose_grip_base)
    robot.grip()
    robot.trajectory_move([
        Pose.pose_from_dict(e1_pose_intermediate_tray),
        Pose.pose_from_dict(e1_pose_intermediate_board),
        Pose.pose_from_dict(e1_pose_parallel_grip),
        Pose.pose_from_dict(e1_pose_board_corner),
    ])
    robot.release()
    robot.move_to_pose(e1_pose_parallel_grip)
    robot.reset_state()
    robot.close_connection()


if __name__ == '__main__':
    main()
