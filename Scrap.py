import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import pandas as pd
import serial
# import threading
# import time
import csv
# from datetime import datetime

# Demo 3 lol

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

ser = serial.Serial("COM5", baudrate=115200)
ser.flushInput()

# df = pd.DataFrame({"Root Angle": [],
#                    "Angle 1/2": [],
#                    "Angle 2/3": []})

with open("Angle_Three_sensor.csv", "a") as f:
    label = []
    writer = csv.writer(f)
    print("Start reading")
    for i in range(5):
        i += 1
        label.append(i)
    writer.writerow(label)

    while True:
        def move_arrow(pos1, direction1, direction2, direction3, direction4, direction5,
                       trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,
                       length_trunk,
                       ):
            # Converting directional inputs into arrays
            pos1 = np.asarray(pos1)
            direction1 = np.asarray(direction1)
            direction2 = np.asarray(direction2)
            direction3 = np.asarray(direction3)
            direction4 = np.asarray(direction4)
            direction5 = np.asarray(direction5)

            # Normalizing
            direction1 = direction1 / np.linalg.norm(direction1)
            direction2 = direction2 / np.linalg.norm(direction2)
            direction3 = direction3 / np.linalg.norm(direction3)
            direction4 = direction4 / np.linalg.norm(direction4)
            direction5 = direction5 / np.linalg.norm(direction5)

            # Shifting vectors
            shift1 = direction1 * length_trunk[0]
            end1 = pos1 + shift1
            shift2 = direction2 * length_trunk[1]
            end2 = end1 + shift2
            shift3 = direction3 * length_trunk[2]
            end3 = end2 + shift3
            shift4 = direction4 * length_trunk[3]
            end4 = end3 + shift4
            shift5 = direction5 * length_trunk[4]
            end5 = end4 + shift5

            axis = np.array([0, 0, 1])
            ang1 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction1, axis), -1.0, 1.0))), 2)
            ang2 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction2, direction1), -1.0, 1.0))), 2)
            ang3 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction3, direction2), -1.0, 1.0))), 2)
            ang4 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction4, direction3), -1.0, 1.0))), 2)
            ang5 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction5, direction4), -1.0, 1.0))), 2)
            #print("Root angle: ", ang1, "Angle 1/2", ang2, "Ang 2/3", ang3, "Ang 3/4", ang4, "Ang 4/5", ang5)
            writer.writerow([ang1, ang2, ang3, ang4, ang5])
            # df.loc[len(df)] = [ang1, ang2, ang3]

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


        def update(i):
            data = ser.readline().decode()[0:][:-2].split(",")  # 2-1-0/5-4-3/8-7-6
            print(data)
            dir_shift1 = np.array([float(data[2]) - error1[0], float(data[1]) - error1[1], float(data[0]) - error1[2]])
            dir_shift2 = np.array([float(data[5]) - error2[0], float(data[4]) - error2[1], float(data[3]) - error2[2]])
            dir_shift3 = np.array([float(data[8]) - error3[0], float(data[7]) - error3[1], float(data[6]) - error3[2]])
            dir_shift4 = np.array([float(data[11]) - error3[0], float(data[10]) - error3[1], float(data[9]) - error3[2]])
            dir_shift5 = np.array([float(data[14]) - error3[0], float(data[13]) - error3[1], float(data[12]) - error3[2]])
            move_arrow(pos1,dir1 + dir_shift1,dir2 + dir_shift2,dir3 + dir_shift3,dir4 + dir_shift4,dir5 + dir_shift5,
                       trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,
                       length_trunk)
            return [trunk_plt1, trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,]


        ani = animation.FuncAnimation(fig, update, frames=None, interval=10     , repeat=True, blit=True)

        plt.show()

        # df.to_excel("output.xlsx")
        
