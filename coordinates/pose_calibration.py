from robots.pose import Pose
import json


class CalibratedPositions:

    def calibration(self):

        with open('coordinates/ref_coordinates.json', 'r') as openfile:
            referenced_coordinates = json.load(openfile)
        
        board_horizontal_distance = Pose(*referenced_coordinates['board_horizontal_distance'])
        board_vertical_distance = Pose(*referenced_coordinates['board_vertical_distance'])

        # Number 1 on keyboard
        self.board_bottom_left_corner = (self.board_center
                                         - board_horizontal_distance
                                         + board_vertical_distance)
        # Number 2 on keyboard
        self.board_bottom_center = self.board_center + board_vertical_distance
        # Number 3 on keyboard
        self.board_bottom_right_corner = (self.board_center
                                          + board_horizontal_distance
                                          + board_vertical_distance)
        # Number 4 on keyboard
        self.board_left_center = self.board_center - board_horizontal_distance
        # Number 6 on keyboard
        self.board_right_center = self.board_center + board_horizontal_distance
        # Number 7 on keyboard
        self.board_top_left_corner = (self.board_center
                                      - board_horizontal_distance
                                      - board_vertical_distance)
        # Number 8 on keyboard
        self.board_top_center = self.board_center - board_vertical_distance
        # Number 9 on keyboard
        self.board_top_right_corner = (self.board_center
                                       + board_horizontal_distance
                                       - board_vertical_distance)
        # Pose to get bead
        self.grip_base = Pose(*referenced_coordinates['grip_base'])

        # Pose above tray
        self.intermediate_tray = (self.board_center
                                  + {'j1': -1.552, 'j2': 1.123,
                                     'j3': -0.352, 'j4': 0.133,
                                     'j5': -0.430, 'j6': -0.107})
        # Pose above board
        self.intermediate_board = (self.board_center
                                   + {'j1': 0.025, 'j2': 1.123,
                                      'j3': -0.352, 'j4': 0.133,
                                      'j5': -0.430, 'j6': -0.117})
        # Pose closer to the board
        self.parallel_board = (self.board_center
                               + {'j1': 0.025, 'j2': 0.182,
                                  'j3': 0.150, 'j4': 0.0,
                                  'j5': -0.430, 'j6': -0.005})

    def __init__(self, center_board) -> None:
        self.board_center = center_board
        self.calibration()
