import csv
import cv2
import numpy as np
#from sklearn.model_selection import train_test_split

def getData(path='./data/', csv_file='./data/driving_log.csv'):#, test_ratio=0.25):
    steering_angles = []
    car_frames = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            steering_angle = float(row['steering'])

            # read in images from center, left and right cameras
            frame = []
            frame.append(cv2.imread(path + row['left'].strip()))
            frame.append(cv2.imread(path + row['center'].strip()))
            frame.append(cv2.imread(path + row['right'].strip()))

            # add images and angles to data set
            car_frames.append(np.array(frame))
            steering_angles.append(steering_angle)

            rev_frame = []
            rev_frame.append(np.fliplr((cv2.imread(path + row['left'].strip())))
            rev_frame.append(np.fliplr((cv2.imread(path + row['center'].strip())))
            rev_frame.append(np.fliplr((cv2.imread(path + row['right'].strip())))

            car_frames.append(np.array(rev_frame))
            steering_angles.append(-steering_angle)
    return np.array(car_frames), np.array(steering_angles)
