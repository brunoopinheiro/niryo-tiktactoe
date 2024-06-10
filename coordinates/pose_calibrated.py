from robots.pose import Pose
from abc import abstractmethod

class CalibratedPositions:
    def __init__(self,center_board) -> None:
        #Number 5 on keyboard (center of the board)
        self.e1_pose_board_center = Pose(**center_board)

    @abstractmethod
    def calibration(self):

        board_horizontal_distance = Pose(**{"j1": 0.141, "j2": -0.020,
                                    "j3": 0.017, "j4": 0.074,
                                    "j5": 0.019, "j6": 0.179})
        
        board_vertical_distance = Pose(**{"j1": -0.007, "j2": -0.225,
                                    "j3": 0.441, "j4": 0.001,
                                    "j5": -0.272, "j6": -0.010})
        
        #Number 1 on keyboard
        self.e1_pose_board_bottom_left_corner = self.e1_pose_board_center - board_horizontal_distance + board_vertical_distance
        
        #Number 2 on keyboard
        self.e1_pose_board_bottom_center = self.e1_pose_board_center + board_vertical_distance
        
        #Number 3 on keyboard
        self.e1_pose_board_bottom_right_corner = self.e1_pose_board_center + board_horizontal_distance + board_vertical_distance
        
        #Number 4 on keyboard
        self.e1_pose_board_left_center = self.e1_pose_board_center - board_horizontal_distance
        
        #Number 6 on keyboard
        self.e1_pose_board_right_center = self.e1_pose_board_center + board_horizontal_distance
        
        #Number 7 on keyboard
        self.e1_pose_board_top_left_corner = self.e1_pose_board_center - board_horizontal_distance - board_vertical_distance
        
        #Number 8 on keyboard
        self.e1_pose_board_top_center = self.e1_pose_board_center - board_vertical_distance
        
        #Number 9 on keyboard
        self.e1_pose_board_top_right_corner = self.e1_pose_board_center + board_horizontal_distance - board_vertical_distance

        #Pose to get bead
        self.e1_pose_grip_base = self.e1_pose_board_center + Pose(**{"j1": -1.552, "j2": 0.321,
                                                                    "j3": -0.517, "j4": 0.133,
                                                                    "j5": 0.468, "j6": -0.112})
        
        #Pose above tray
        self.e1_pose_intermediate_tray = self.e1_pose_board_center + Pose(**{"j1": -1.552, "j2": 1.123,
                                                                    "j3": -0.352, "j4": 0.133,
                                                                    "j5": -0.430, "j6": -0.107})
        
        #Pose above board
        self.e1_pose_intermediate_board = self.e1_pose_board_center + Pose(**{"j1": 0.025, "j2": 1.123,
                                                                    "j3": -0.352, "j4": 0.133,
                                                                    "j5": -0.430, "j6": -0.117})
        
        #Pose closer to the board
        self.e1_pose_parallel_board = self.e1_pose_board_center + Pose(**{"j1": 0.025, "j2": 0.182,
                                                                    "j3": -0.352, "j4": 0.133,
                                                                    "j5": -0.430, "j6": -0.117})