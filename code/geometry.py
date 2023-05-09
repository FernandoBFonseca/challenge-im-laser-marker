#Custom geometry library to do all math  

import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from math import sqrt
from scipy.optimize import fsolve
from mpl_toolkits import mplot3d

class RefFrame:
    
    def __init__(self, X,Y,Z):
        self.X = X
        self.Y = Y
        self.Z = Z
    def __str__(self) -> str:
        return  f'Frame(X: {self.X:.2f}, Y: {self.Y:.2f}, Z: {self.Z:.2f})'
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getZ(self):
        return self.Z



def system3d(p,n1,n2,n3,n4,w,h):#System of equations to find position in relation to the wall
  X_est, Y_est, Z_est= p
  
  F=[0,0,0]
  F[0] =n1[1]*sqrt(X_est**2 + Y_est**2 + Z_est**2) + Y_est
  F[1] =n2[2]*sqrt(X_est**2 + Y_est**2 + (Z_est-h)**2) + Z_est - h
  F[2] =n3[0]*sqrt((X_est-w)**2 + Y_est**2 + (Z_est-h)**2) + X_est - w

  return F


def Calculate_Coord_Base(n1,n2,n3,n4,w,h):

    X_est,Y_est,Z_est = fsolve(system3d, (w/2,h/2,h/2), args=(n1,n2,n3,n4,w,h))

    return RefFrame(X_est,Y_est,Z_est)

def quaternion_rotation_matrix(Q): #Do a rotaion matrix given the quartenion of rotation
  # Extract the values from Q
  q0 = Q[0]
  q1 = Q[1]
  q2 = Q[2]
  q3 = Q[3]
     
  # First row of the rotation matrix
  r00 = 2 * (q0 * q0 + q1 * q1) - 1
  r01 = 2 * (q1 * q2 - q0 * q3)
  r02 = 2 * (q1 * q3 + q0 * q2)
     
  # Second row of the rotation matrix
  r10 = 2 * (q1 * q2 + q0 * q3)
  r11 = 2 * (q0 * q0 + q2 * q2) - 1
  r12 = 2 * (q2 * q3 - q0 * q1)
     
  # Third row of the rotation matrix
  r20 = 2 * (q1 * q3 - q0 * q2)
  r21 = 2 * (q2 * q3 + q0 * q1)
  r22 = 2 * (q0 * q0 + q3 * q3) - 1
     
  # 3x3 rotation matrix
  rot_matrix = np.array([[r00, r01, r02],
                           [r10, r11, r12],
                           [r20, r21, r22]])
                            
  return rot_matrix