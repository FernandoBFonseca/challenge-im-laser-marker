
import numpy as np
#Importing custom librarys
from geometry import *
from robot_comands import *



def setup(w,h,robot):
    #Functions that calibrates the position of the robot's head in relation to the wall
    #Given the manual input of the direction of each corner
    print('Point to lower left corner')
    move_robot_rotation(robot)
    n1 = get_point_direction(robot)
    sleep(0.5)
    print(f'Vector lower left corner: {n1}\n')

    print('Point to upper left corner')
    move_robot_rotation(robot)
    n2 = get_point_direction(robot)
    sleep(0.5)
    print(f'Vector upper left corner: {n2}\n')

    print('Point to upper right corner')
    move_robot_rotation(robot)
    n3 = get_point_direction(robot)
    sleep(0.5)
    print(f'Vector upper right corner: {n3}\n')

    print('Point to lower right corner')
    move_robot_rotation(robot)
    n4 = get_point_direction(robot)
    sleep(0.5)
    print(f'Vector lower right corner: {n4}\n')

    #Solving the equations
    HeadCord = Calculate_Coord_Base(n1,n2,n3,n4,w,h) #X,Y,Z base 

    return HeadCord










