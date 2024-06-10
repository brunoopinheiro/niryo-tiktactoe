from robots.pose import Pose
from robots.test_robot import TestRobot
from coordinates.pose_calibration import CalibratedPositions


def main():
    grid_center = {"j1": -0.025, "j2": -0.817,
                    "j3": -0.186, "j4": -0.133,
                    "j5": -0.477, "j6": -0.074}
 
    calibrated_pos = CalibratedPositions(grid_center)
    calibrated_pos.calibration()
    
    robot = TestRobot()
    robot.printpose()
    robot.move_to_pose_(calibrated_pos.e1_pose_intermediate_tray)
    robot.printpose()
    robot.move_to_pose_(calibrated_pos.e1_pose_grip_base)
    robot.printpose()
    robot.grip()
    robot.trajectory_move([
        calibrated_pos.e1_pose_intermediate_tray,
        calibrated_pos.e1_pose_intermediate_board,
        calibrated_pos.e1_pose_parallel_board,
        calibrated_pos.e1_pose_board_bottom_center
    ])
    robot.release()
    robot.move_to_pose_(calibrated_pos.e1_pose_parallel_board)
    robot.reset_state()
    robot.close_connection()


if __name__ == '__main__':
    main()
