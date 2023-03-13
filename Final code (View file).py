# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
Angle1 = ax.text(0, 0, 1, "", fontsize=10, ha='left', va='center')
Angle2 = ax.text(0, 0, 3, "", fontsize=10, ha='left', va='center')
Angle3 = ax.text(0, 0, 5, "", fontsize=10, ha='left', va='center')
Angle4 = ax.text(0, 0, 7, "", fontsize=10, ha='left', va='center')
Angle5 = ax.text(0, 0, 9, "", fontsize=10, ha='left', va='center')

pos1 = [0, 0, 0]
dir1 = [0, 0, 0]
dir2 = [0, 0, 0]
dir3 = [0, 0, 0]
dir4 = [0, 0, 0]
dir5 = [0, 0, 0]

length_trunk = [2, 2, 2, 2, 2]
trunk_plt1 = ax.plot3D([], [], [], c='b', linewidth=3)[0]  # c='aquamarine'
trunk_plt2 = ax.plot3D([], [], [], c='r', linewidth=3)[0]  # c='bisque'
trunk_plt3 = ax.plot3D([], [], [], c='b', linewidth=3)[0]  # c='antiquewhite'
trunk_plt4 = ax.plot3D([], [], [], c='r', linewidth=3)[0]  # c='bisque'
trunk_plt5 = ax.plot3D([], [], [], c='b', linewidth=3)[0]  # c='antiquewhite'
line_plt = ax.plot3D([], [], [], c='k', linestyle='-.', linewidth=0.7)[0]  # cyan

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fileName = "angle_three_sensor.csv"
df = pd.read_csv(fileName)

try:
    def move_arrow(pos, direction1, direction2, direction3, direction4, direction5,
                   trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,
                   length_trunk, ang_array
                   ):
        # Converting directional inputs into arrays
        pos = np.asarray(pos)
        direction1 = np.asarray(direction1)
        direction2 = np.asarray(direction2)
        direction3 = np.asarray(direction3)
        direction4 = np.asarray(direction4)
        direction5 = np.asarray(direction5)
        ang_array = np.asarray(ang_array)
        # Normalizing
        direction1 = direction1 / np.linalg.norm(direction1)
        direction2 = direction2 / np.linalg.norm(direction2)
        direction3 = direction3 / np.linalg.norm(direction3)
        direction4 = direction4 / np.linalg.norm(direction4)
        direction5 = direction5 / np.linalg.norm(direction5)

        # Shifting vectors
        shift1 = direction1 * length_trunk[0]
        end1 = pos + shift1

        shift2 = direction2 * length_trunk[1]
        end2 = end1 + shift2

        shift3 = direction3 * length_trunk[2]
        end3 = end2 + shift3

        shift4 = direction4 * length_trunk[3]
        end4 = end3 + shift4

        shift5 = direction5 * length_trunk[4]
        end5 = end4 + shift5
        # ang1 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction1, direction2), -1.0, 1.0))), 3)
        # ang2 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction2, direction3), -1.0, 1.0))), 3)
        # ang3 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction3, direction4), -1.0, 1.0))), 3)
        # ang4 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction4, direction5), -1.0, 1.0))), 3)
        # print("Angle 1: ", ang1, ", Angle 2 :", ang2, ", Angle 3 :", ang3)

        # Set line data
        trunk_plt1.set_data([pos1[0], end1[0]], [pos1[1], end1[1]])  # Set data
        trunk_plt1.set_3d_properties([pos1[2], end1[2]])  # Set properties
        trunk_plt2.set_data([end1[0], end2[0]], [end1[1], end2[1]])
        trunk_plt2.set_3d_properties([end1[2], end2[2]])
        trunk_plt3.set_data([end2[0], end3[0]], [end2[1], end3[1]])
        trunk_plt3.set_3d_properties([end2[2], end3[2]])
        trunk_plt4.set_data([end3[0], end4[0]], [end3[1], end4[1]])
        trunk_plt4.set_3d_properties([end3[2], end4[2]])
        trunk_plt5.set_data([end4[0], end5[0]], [end4[1], end5[1]])
        trunk_plt5.set_3d_properties([end4[2], end5[2]])

        line_plt.set_data([pos1[0], end5[0]], [pos1[1], end5[1]])
        line_plt.set_3d_properties([pos1[2], end5[2]])
        Angle1.set_text("")
        Angle1.set_text("H/1: {:.2f}".format(ang_array[0]))
        Angle1.set_position((end1[0] + 2, end1[1]))
        Angle2.set_text("")
        Angle2.set_text("1/2: {:.2f}".format(ang_array[1]))
        Angle2.set_position((end2[0] + 2, end2[1]))
        Angle3.set_text("")
        Angle3.set_text("2/3: {:.2f}".format(ang_array[2]))
        Angle3.set_position((end3[0] + 2, end3[1]))
        Angle4.set_text("")
        Angle4.set_text("3/4: {:.2f}".format(ang_array[3]))
        Angle4.set_position((end4[0] + 2, end4[1]))
        Angle5.set_text("")
        Angle5.set_text("4/5: {:.2f}".format(ang_array[4]))
        Angle5.set_position((end5[0] + 2, end5[1]))


    def sample_frame(i):
        dir_shift1 = df[['X1', 'Y1', 'Z1']].iloc[i].to_numpy()
        dir_shift2 = df[['X2', 'Y2', 'Z2']].iloc[i].to_numpy()
        dir_shift3 = df[['X3', 'Y3', 'Z3']].iloc[i].to_numpy()
        dir_shift4 = df[['X4', 'Y4', 'Z4']].iloc[i].to_numpy()
        dir_shift5 = df[['X5', 'Y5', 'Z5']].iloc[i].to_numpy()
        ang_array = df[['Angle1', 'Angle1/2', 'Angle2/3', 'Angle3/4', 'Angle4/5']].iloc[i].to_numpy()

        # direction3 = np.array(dir3 + dir_shift3)
        # direction3 = direction3 / np.linalg.norm(direction3)
        # direction4 = np.array(dir4 + dir_shift4)
        # direction4 = direction4 / np.linalg.norm(direction4)
        # ang = np.rad2deg(np.arccos(np.clip(np.dot(direction3, direction4), -1.0, 1.0)))
        # annotation(1, 1, 2, ang)
        # print(ang)

        move_arrow(pos1, dir1 + dir_shift1, dir2 + dir_shift2, dir3 + dir_shift3, dir4 + dir_shift4, dir5 + dir_shift5,
                   trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,
                   length_trunk, ang_array)
        return [trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5, line_plt,
                Angle1, Angle2, Angle3, Angle4, Angle5]

    ani = animation.FuncAnimation(fig, sample_frame, frames=None, interval=10, repeat=True, blit=True)

    plt.show()

except:
    print("Keyboard Interupt")
