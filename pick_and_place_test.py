from robots.pose import Pose
from robots.niryo_robot import NiryoRobot
from moviment_path.calibrador import CalibratedPositions


def main():
    grid_center = {"j1": -0.025, "j2": -0.817,
                                "j3": -0.186, "j4": -0.133,
                                "j5": -0.477, "j6": -0.074}
    
    # Trying with absolute positions
    # Should be replaced with relative poses
    # e1_pose_grip_base = {"j1": -1.577, "j2": -0.496,
    #                      "j3": -0.703, "j4": 0.000,
    #                      "j5": -0.009, "j6": -0.186}

    # e1_pose_intermediate_tray = {"j1": -1.577, "j2": 0.306,
    #                              "j3": -0.538, "j4": 0.000,
    #                              "j5": -0.907, "j6": -0.181}

    # e1_pose_intermediate_board = {"j1": 0.000, "j2": 0.306,
    #                               "j3": -0.538, "j4": 0.000,
    #                               "j5": -0.907, "j6": -0.191}

    # e1_pose_parallel_grip = {"j1": 0.000, "j2": -0.635,
    #                             "j3": -0.036, "j4": -0.133,
    #                             "j5": -0.907, "j6": -0.079}

    # e1_pose_intermediate_board = {"j1": 0.000, "j2": 0.306,
    #                               "j3": -0.538, "j4": 0.000,
    #                               "j5": -0.907, "j6": -0.191}

    # # Posição 3 do teclado numérico (Bottom right corner)
    # e1_pose_board_corner = {"j1": 0.123, "j2": -1.062,
    #                         "j3": 0.272, "j4": -0.058,
    #                         "j5": -0.730, "j6": 0.095}
    
    # e1_pose_board_bottom = {"j1": -0.018, "j2": -1.042,
    #                             "j3": 0.255, "j4": -0.132,
    #                             "j5": -0.749, "j6": -0.084}

    calibrated_pos = CalibratedPositions(grid_center)
    calibrated_pos.calibration()
    
    robot = NiryoRobot()
    robot.printpose()
    robot.move_to_pose_(calibrated_pos.e1_pose_intermediate_tray)
    robot.printpose()
    robot.move_to_pose_(calibrated_pos.e1_pose_grip_base)
    robot.printpose()
    robot.grip()
    robot.trajectory_move([
        Pose.pose_from_dict(calibrated_pos.e1_pose_intermediate_tray),
        Pose.pose_from_dict(calibrated_pos.e1_pose_intermediate_board),
        Pose.pose_from_dict(calibrated_pos.e1_pose_parallel_grip),
        Pose.pose_from_dict(calibrated_pos.e1_pose_board_bottom),
    ])
    robot.release()
    robot.move_to_pose_(calibrated_pos.e1_pose_parallel_grip)
    robot.reset_state()
    robot.close_connection()


if __name__ == '__main__':
    main()
