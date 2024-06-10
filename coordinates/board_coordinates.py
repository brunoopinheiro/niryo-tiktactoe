import time
from pyniryo2 import *

robot = NiryoRobot("169.254.200.200")

robot.arm.calibrate_auto()

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

# Posição 2 do teclado numérico (Bottom center)
e1_pose_board_bottom_center = {"j1": -0.018, "j2": -1.042,
                        "j3": 0.255, "j4": -0.132,
                        "j5": -0.749, "j6": -0.084}

# Posição 3 do teclado numérico (Bottom right corner)
e1_pose_board_bottom_right_corner = {"j1": 0.123, "j2": -1.062,
                        "j3": 0.272, "j4": -0.058,
                        "j5": -0.730, "j6": 0.095}

# Posição 5 do teclado (Center)
e1_pose_board_center = {"j1": -0.025, "j2": -0.817,
                        "j3": -0.186, "j4": -0.133,
                        "j5": -0.477, "j6": -0.074}

coord = ["j1","j2","j3","j4","j5","j6"]
dist_horiz = {}
dist_vert = {}

for i in coord:
    dist_horiz[i] = round(e1_pose_board_bottom_right_corner[i] - e1_pose_board_bottom_center[i],3) #0.141
    dist_vert[i] = round(e1_pose_board_bottom_center[i] - e1_pose_board_center[i],3) #0.007

# Posição 1 do teclado numérico (Bottom left corner)
e1_pose_board_bottom_left_corner = {}
for i in coord:
    e1_pose_board_bottom_left_corner[i] = round(e1_pose_board_center[i] - dist_horiz[i] + dist_vert[i],3)

# Posição 4 do teclado numérico (Left center)
e1_pose_board_left_center = {}
for i in coord:
    e1_pose_board_left_center[i] = round(e1_pose_board_center[i] - dist_horiz[i],3)

# Posição 6 do teclado numérico (Right center)
e1_pose_board_right_center = {}
for i in coord:
    e1_pose_board_right_center[i] = round(e1_pose_board_center[i] + dist_horiz[i],3)

# Posição 7 do teclado numérico (Top left corner)
e1_pose_board_top_left_corner = {}
for i in coord:
    e1_pose_board_top_left_corner[i] = round(e1_pose_board_center[i] - dist_horiz[i] - dist_vert[i],3)

# Posição 8 do teclado numérico (Top center)
e1_pose_board_top_center = {}
for i in coord:
    e1_pose_board_top_center[i] = round(e1_pose_board_center[i] - dist_vert[i],3)

# Posição 9 do teclado numérico (Top right corner)
e1_pose_board_top_right_corner = {}
for i in coord:
    e1_pose_board_top_right_corner[i] = round(e1_pose_board_center[i] + dist_horiz[i] - dist_vert[i],3)

references_of_each_board_position = {
    1: e1_pose_board_bottom_left_corner,
    2: e1_pose_board_bottom_center, #Sugestão de mudança: e1_pose_board_bottom_center,
    3: e1_pose_board_bottom_right_corner, #Sugestão de mudança: e1_pose_board_bottom_right_corner,
    4: e1_pose_board_left_center,
    5: e1_pose_board_center,
    6: e1_pose_board_right_center,
    7: e1_pose_board_top_left_corner,
    8: e1_pose_board_top_center,
    9: e1_pose_board_top_right_corner
}

speed = 100 # Deve ser um valor entre 100 e 1000

grip_path = [
    robot.arm.move_joints(e1_pose_intermediate_board),
    robot.arm.move_joints(e1_pose_intermediate_tray),
    robot.arm.move_joints(e1_pose_grip_base),
    robot.arm.close_gripper(speed),
    time.sleep(2), # Botei só pra a gente testar as velocidades e ver se precisa ou não
    robot.arm.move_joints(e1_pose_intermediate_tray),
    robot.arm.move_joints(e1_pose_intermediate_board),
    robot.arm.move_joints(e1_pose_parallel_grip)
    ]

def play_path(p):
    grip_path
    robot.arm.move_joints(references_of_each_board_position[p])

# def evaluate_position(p,j):
#    evaluate = True
#    while evaluate:
#       if board[str(p)] == ' ':
#          board[str(p)] = player[j]
#          evaluate = False
#          printboard()
#       else:
#          p = input("Position not available. Choose another position: ")

# def evaluateVictory(p,j):
#    win = False
#    for comb in combinations:
#       if str(p) in comb:
#          row = 0
#          for i in list(comb):
#             if board[i] == player[j]:
#                row += 1
#          if row == 3:
#             win = True
#    return win

# def evaluate_draw():
#    draw = True
#    for i in range(9):
#       if board[str(i+1)] == ' ':
#          draw = False
#    return draw