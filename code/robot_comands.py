
import sys
sys.path.append('C:\\Users\\Fernando\\Documents\\Challenge\\Imagine_Make\\libs')

from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox

from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
from geometry import quaternion_rotation_matrix
import numpy as np
import keyboard
from time import sleep

def ini_robot(run_on_robot = False): 
    #Start Robot and Sincronize Simulation robot and the Real one
    '''
    RDK = Robolink()
    robot = RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)
    if not robot.Valid():
        raise Exception('No robot selected or available')
    '''
    RDK = Robolink()
    robot = RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)
    if not robot.Valid():
        raise Exception('No robot selected or available')


    RUN_ON_ROBOT = run_on_robot

    if RUN_ON_ROBOT:
        success = robot.Connect()
        status, status_msg = robot.ConnectedState()
        if status != ROBOTCOM_READY:
            print(status_msg)
            raise Exception("Failed to connect: " + status_msg)
    
        RDK.setRunMode(RUNMODE_RUN_ROBOT)

    robot.setPoseFrame(robot.PoseFrame())
    robot.setPoseTool(robot.PoseTool())

    robot.setZoneData(10)
    #robot.setSpeed(50,5)

    start_pose = robot.Pose() 
    pos_init = start_pose.Pos() 
    
    robot.MoveJ(start_pose) 
    
    robot_base = RDK.Item('RoboBase')
    frame_pose = robot_base.Pose()

    #Ajusting robot position in relation to the all
    frame_pose = robomath.TxyzRxyz_2_Pose([0,0,0,0,0,0])
    robot_base.setPose(frame_pose)

    robot.MoveJ(TxyzRxyz_2_Pose([500,0,800,0,pi/2,-180]))
    

    frame_pose = robomath.TxyzRxyz_2_Pose([0,0,0,0,0,pi/2])
    robot_base.setPose(frame_pose)
    

    return RDK, robot

def get_point_direction(robot:robolink.Item):#Gets the direction that the laser points

    pose = robot.Pose()

    Q = robomath.pose_2_quaternion(pose)

    Z_direction = np.array([0,0,1])

    n = quaternion_rotation_matrix(Q) @ Z_direction

    return n 


def move_robot_translation(robot:robolink.Item): #Move the robot in position maintaining the rotation

    print('Mode Move Robot in Translation')
    print('Use the arrow keys to control the moviment')
    print('Keys O and P to control decrease and increase precison respectively\n')

    speed = 5.0

    while not keyboard.is_pressed('enter'):
        pose = robot.Pose()
        pos = pose.Pos()
        sleep(0.01)

        if keyboard.is_pressed('o'):
            speed = speed/2
            sleep(0.25)
            print(f'Setting Speed to {speed}mm/s')
        elif keyboard.is_pressed('p'):
            speed = speed*2
            print(f'Setting Speed to {speed}mm/s')
            sleep(0.25)

        if keyboard.is_pressed('up arrow'):
            pos[2] += speed
        elif keyboard.is_pressed('down arrow'):
            pos[2] -= speed
            
        if keyboard.is_pressed('right arrow'):
            pos[0] += speed
        elif keyboard.is_pressed('left arrow'):
            pos[0] -= speed

        pose.setPos(pos)  # joga a pos pra dentro da pose
        robot.MoveL(pose) # move o robo linearmente

def move_robot_rotation(robot:robolink.Item): #Move the robot in rotation maintaining the position
    speed = 1.0
    print('Mode Move Robot in Rotation')
    print('Use the arrow keys to control the moviment')
    print('Keys O and P to control decrease and increase precison respectively\n')


    while not keyboard.is_pressed('enter'):
        pose = robot.Pose()
        pos = pose.VZ()
        sign = 1
        sleep(0.01)
        

        if keyboard.is_pressed('o'):
            speed = speed/2
            sleep(0.25)
            print(f'Setting Speed to {speed}deg/s')
        elif keyboard.is_pressed('p'):
            speed = speed*2
            print(f'Setting Speed to {speed}deg/s')
            sleep(0.25)

        if keyboard.is_pressed('up arrow'):
            #if(sign == 1 and (speed*0.01745329 + pos[4] => 0))
            pos[2] += speed*0.05
        elif keyboard.is_pressed('down arrow'):
            
            pos[2] -= speed*0.05
            
        if keyboard.is_pressed('right arrow'):
            pos[0] += speed*0.05
        elif keyboard.is_pressed('left arrow'):
            pos[0] -= speed*0.05

        pose.setVZ(pos)  # joga a pos pra dentro da pose
        robot.MoveJ(pose) # move o robo linearmente

         

def point_2_wall(RDK, robot:robolink.Item, point:list):
    #Point in a direction given the coordenate to the point in the wall

    pose = robot.Pose()

    goal  = np.array([point[0], 0, point[1]])

    head_position = np.array(pose.Pos())
   
    direction = (goal - head_position)/np.linalg.norm(goal - head_position)
  
    final_pose = point_Zaxis_2_pose(head_position, direction)
    
    robot.MoveJ(final_pose)

def set_robot_frame(RDK,robot,HeadFrame):
    #Ajust robot frame to the wall given the position of the head
    
    head_pos = np.array([HeadFrame.X,-HeadFrame.Y,HeadFrame.Z])
    
    head_relative_pos = robot.Pose().Pos()

    robot_base_pos = head_pos - head_relative_pos
    
    robot_base = RDK.Item('RoboBase')

    frame_pose = robot_base.Pose()
    frame_pose.setPos(robot_base_pos)
    robot_base.setPose(frame_pose)