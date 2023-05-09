
# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project


#Importing custom library
from setup import setup
from robot_comands import *
from import_plan import import_plan


# Forward and backwards compatible use of the RoboDK API:
# Remove these 2 lines to follow python programming guidelines

#Important Observation: to the code to work, the reference frame of the robot must be the wall not the RobotBase 

if __name__ == '__main__':
    
    print('Initiating robot position:')
    [RDK, robot] = ini_robot()#Iniciating Robot and RoboDK comunication
    [w,h,points_lists] = import_plan('C:\\Users\Fernando\Documents\Challenge\Imagine_Make\essaiim.csv')#Importing Plan


    print('Initiating Calibration Routine, please follow the intructions:')
    RobotHeadFrame = setup(w,h,robot)#Calibration Function

    print('End of calibration')
    print(f"Position to Robot's head in relation to the wall lower left corner: {RobotHeadFrame}\n")
    set_robot_frame(RDK,robot,RobotHeadFrame)#Updating Robot Frame

    print(f'Starting service...{len(points_lists)} operations to do')
    counter = 1

    for point in points_lists:#Pointing to all points
        print(f'Targenting {counter}° point {point} in wall')
        point_2_wall(RDK,robot, point)
        print('Press Enter to go to the next point\n')
        input()
        counter += 1
    
    print('Work done!! Congratulations =)')


    