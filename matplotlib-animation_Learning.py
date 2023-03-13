# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import pandas as pd

error1 = np.array([12.52-9.8, -0.5, -1.05])
error2 = np.array([10.34-9.8, -0.56, -1.5])
error3 = np.array([10.05-9.8, -0.71, -0.14])
error4 = np.array([9.39-9.8, -0.35, -1.65])
error5 = np.array([15.12-9.8, 1.96, -0.68])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

pos1 = [0, 0, 0]
dir1 = [0, 0, 0]
dir2 = [0, 0, 0]
dir3 = [0, 0, 0]
dir4 = [0, 0, 0]
dir5 = [0, 0, 0]

length_trunk = [2, 2, 2, 2, 2]
trunk_plt1 = ax.plot3D([], [], [], c='g', linewidth=3)[0]  # c='aquamarine'
trunk_plt2 = ax.plot3D([], [], [], c='r', linewidth=3)[0]  # c='bisque'
trunk_plt3 = ax.plot3D([], [], [], c='g', linewidth=3)[0]  # c='antiquewhite'
trunk_plt4 = ax.plot3D([], [], [], c='r', linewidth=3)[0]  # c='bisque'
trunk_plt5 = ax.plot3D([], [], [], c='g', linewidth=3)[0]  # c='antiquewhite'

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fileName = "Angle_Three_sensor.csv"
df = pd.read_csv(fileName)


def move_arrow(pos1, direction1, direction2, direction3, direction4,
                trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4,length_trunk,):
    # Converting directional inputs into arrays
    pos1 = np.asarray(pos1)
    direction1 = np.asarray(direction1)
    direction2 = np.asarray(direction2)
    direction3 = np.asarray(direction3)
    direction4 = np.asarray(direction4)
    # direction5 = np.asarray(direction5)

    # Normalizing
    direction1 = direction1 / np.linalg.norm(direction1)
    direction2 = direction2 / np.linalg.norm(direction2)
    direction3 = direction3 / np.linalg.norm(direction3)
    direction4 = direction4 / np.linalg.norm(direction4)
    # direction5 = direction5 / np.linalg.norm(direction5)

    # Shifting vectors
    shift1 = direction1 * length_trunk[0]
    end1 = pos1 + shift1

    shift2 = direction2 * length_trunk[1]
    end2 = end1 + shift2

    shift3 = direction3 * length_trunk[2]
    end3 = end2 + shift3

    shift4 = direction4 * length_trunk[3]
    end4 = end3 + shift4

    ang1 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction1, direction2), -1.0, 1.0))), 3)
    ang2 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction2, direction3), -1.0, 1.0))), 3)
    ang3 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction3, direction4), -1.0, 1.0))), 3)
    # ang4 = round(np.rad2deg(np.arccos(np.clip(np.dot(dir4, dir5), -1.0, 1.0))), 3)
    print("Angle 1: ", ang1, ", Angle 2 :", ang2, ", Angle 3 :", ang3)

    # shift5 = dir5 * length_trunk[4]
    # end5 = end4 + shift5

    # Set line data
    trunk_plt1.set_data([pos1[0], end1[0]], [pos1[1], end1[1]])  # Set data
    trunk_plt1.set_3d_properties([pos1[2], end1[2]])  # Set properties
    trunk_plt2.set_data([end1[0], end2[0]], [end1[1], end2[1]])
    trunk_plt2.set_3d_properties([end1[2], end2[2]])
    trunk_plt3.set_data([end2[0], end3[0]], [end2[1], end3[1]])
    trunk_plt3.set_3d_properties([end2[2], end3[2]])
    trunk_plt4.set_data([end3[0], end4[0]], [end3[1], end4[1]])
    trunk_plt4.set_3d_properties([end3[2], end4[2]])
    # trunk_plt5.set_data([end4[0], end5[0]], [end4[1], end5[1]])
    # trunk_plt5.set_3d_properties([end4[2], end5[2]])

    line_plt.set_data([pos1[0], end4[0]], [pos1[1], end4[1]])
    line_plt.set_3d_properties([pos1[2], end4[2]])


def sample_frame(i):
    # ser = serial.Serial("COM5", baudrate=115200)
    # ser.write("1")
    dir_shift1 = df[['Z1', 'Y1', 'X1']].iloc[i].to_numpy()
    dir_shift2 = df[['Z2', 'Y2', 'X2']].iloc[i].to_numpy()
    dir_shift3 = df[['Z3', 'Y3', 'X3']].iloc[i].to_numpy()
    dir_shift4 = df[['Z4', 'Y4', 'X4']].iloc[i].to_numpy()

    # direction3 = np.array(dir3 + dir_shift3)
    # direction3 = direction3 / np.linalg.norm(direction3)
    # direction4 = np.array(dir4 + dir_shift4)
    # direction4 = direction4 / np.linalg.norm(direction4)
    # ang = np.rad2deg(np.arccos(np.clip(np.dot(direction3, direction4), -1.0, 1.0)))
    # annotation(1, 1, 2, ang)
    # print(ang)

    move_arrow(pos1, dir1 + dir_shift1, dir2 + dir_shift2, dir3 + dir_shift3, dir4 + dir_shift4,
                trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4,
                length_trunk)
    return [trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, line_plt]


ani = animation.FuncAnimation(fig, sample_frame, 250, interval=400, repeat=True, blit=True)

plt.show()
