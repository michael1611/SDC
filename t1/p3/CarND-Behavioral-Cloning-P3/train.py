import csv
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def getData(path='./data', csv_file='./data/driving_log.csv', test_ratio=0.25):
    steering_angles = []
    car_frames = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
            for row in reader:
                steering_angle = float(row[3])

                # read in images from center, left and right cameras
                frame = []
                frame.append(cv2.imread(path + row[0]))
                frame.append(cv2.imread(path + row[1]))
                frame.append(cv2.imread(path + row[2]))

                # add images and angles to data set
                car_frames.append(frame)
                steering_angles.append(steering_angle)
    return train_test_split(car_frames, steering_angles, test_ratio=test_ratio)
