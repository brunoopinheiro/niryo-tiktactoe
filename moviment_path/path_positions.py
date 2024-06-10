import time
from pyniryo2 import *
from calibrador import CalibratedPositions

class PoseCoordinates():
    
    def __init__(self, pose_claibrated: CalibratedPositions):
        
        # Posição 5 do teclado (Center)
        grid_center = {"j1": -0.025, "j2": -0.817,
                       "j3": -0.186, "j4": -0.133,
                       "j5": -0.477, "j6": -0.074}
        
        self.positions = pose_claibrated(grid_center)
        
        # Grip! Deve ser um valor entre 100 e 1000
        # self.speed = 100 

        # self.e1_pose_grip_base = {"j1": -1.577, "j2": -0.496,
        #                     "j3": -0.703, "j4": 0.000,
        #                     "j5": -0.009, "j6": -0.186}

        # self.e1_pose_intermediate_tray = {"j1": -1.577, "j2": 0.306,
        #                             "j3": -0.538, "j4": 0.000,
        #                             "j5": -0.907, "j6": -0.181}

        # self.e1_pose_intermediate_board = {"j1": 0.000, "j2": 0.306,
        #                             "j3": -0.538, "j4": 0.000,
        #                             "j5": -0.907, "j6": -0.191}

        # self.e1_pose_parallel_grip = {"j1": 0.000, "j2": -0.635,
        #                         "j3": -0.036, "j4": -0.133,
        #                         "j5": -0.907, "j6": -0.079}

        # coord = ["j1","j2","j3","j4","j5","j6"]
        # dist_horiz = {}
        # dist_vert = {}
        # for i in coord:
        #     dist_horiz[i] = round(self.e1_pose_board_bottom_right_corner[i] - self.e1_pose_board_bottom_center[i],3) #0.141
        #     dist_vert[i] = round(self.e1_pose_board_bottom_center[i] - self.e1_pose_board_center[i],3) #0.007
        # # Posição 1 do teclado numérico (Bottom left corner)
        # self.e1_pose_board_bottom_left_corner = {}
        # for i in coord:
        #     self.e1_pose_board_bottom_left_corner[i] = round(self.e1_pose_board_center[i] - dist_horiz[i] + dist_vert[i],3)


        # # Posição 2 do teclado numérico (Bottom center)
        # self.e1_pose_board_bottom = {"j1": -0.018, "j2": -1.042,
        #                         "j3": 0.255, "j4": -0.132,
        #                         "j5": -0.749, "j6": -0.084}

        # # Posição 3 do teclado numérico (Bottom right corner)
        # self.e1_pose_board_corner = {"j1": 0.123, "j2": -1.062,
        #                         "j3": 0.272, "j4": -0.058,
        #                         "j5": -0.730, "j6": 0.095}

        # # Posição 4 do teclado numérico (Left center)
        # self.e1_pose_board_left_center = {}
        # for i in coord:
        #     self.e1_pose_board_left_center[i] = round(self.e1_pose_board_center[i] - dist_horiz[i],3)

        # # Posição 6 do teclado numérico (Right center)
        # self.e1_pose_board_right_center = {}
        # for i in coord:
        #     self.e1_pose_board_right_center[i] = round(self.e1_pose_board_center[i] + dist_horiz[i],3)

        # # Posição 7 do teclado numérico (Top left corner)
        # self.e1_pose_board_top_left_corner = {}
        # for i in coord:
        #     self.e1_pose_board_top_left_corner[i] = round(self.e1_pose_board_center[i] - dist_horiz[i] - dist_vert[i],3)

        # # Posição 8 do teclado numérico (Top center)
        # self.e1_pose_board_top_center = {}
        # for i in coord:
        #     self.e1_pose_board_top_center[i] = round(self.e1_pose_board_center[i] - dist_vert[i],3)

        # # Posição 9 do teclado numérico (Top right corner)
        # self.e1_pose_board_top_right_corner = {}
        # for i in coord:
        #     self.e1_pose_board_top_right_corner[i] = round(self.e1_pose_board_center[i] + dist_horiz[i] - dist_vert[i],3)


        self.paths_of_each_grid_position = {
            1: self.e1_pose_board_bottom_left_corner,
            2: self.e1_pose_board_bottom, #Sugestão de mudança: e1_pose_board_bottom_center,
            3: self.e1_pose_board_corner, #Sugestão de mudança: e1_pose_board_bottom_right_corner,
            4: self.e1_pose_board_left_center,
            5: self.e1_pose_board_center,
            6: self.e1_pose_board_right_center,
            7: self.e1_pose_board_top_left_corner,
            8: self.e1_pose_board_top_center,
            9: self.e1_pose_board_top_right_corner
            
        }
        
    def get_game_piece(self):
        self.robot.arm.move_joints(self.e1_pose_intermediate_tray)
        self.robot.arm.move_joints(self.e1_pose_grip_base)
        self.robot.arm.close_gripper(self.speed)
        time.sleep(2) # Botei só pra a gente testar as velocidades e ver se precisa ou não
        self.robot.arm.move_joints(self.e1_pose_intermediate_tray)
        self.robot.arm.move_joints(self.e1_pose_intermediate_board)
        self.robot.arm.move_joints(self.e1_pose_parallel_grip)

