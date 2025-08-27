import cv2
import numpy as np
import time
# Load the image
start = time.time()
image = cv2.imread(r'C:\Users\Admin_PC\Desktop\robot\aruco_marker\singlemarkersoriginal.jpg')


# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()


# Create the ArUco detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# Detect the markers
corners, ids, rejected = detector.detectMarkers(gray)
end = time.time()
# Print the detected markers
print("Detected markers:", ids)
print("Detection time: {:.4f} seconds".format(end - start))
if ids is not None:
    cv2.aruco.drawDetectedMarkers(image, corners, ids)
    cv2.imshow('Detected Markers', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()