"""
Aruco Marker detection

Usage:
    detection.py INPUT_PATH OUTPUT_PATH

Options:

-h --help             show this screen
"""
# Standard Library
import time
# External Library
import cv2
import numpy as np
from docopt import docopt

def main():
    args = docopt(__doc__)
    input = args['INPUT_PATH']
    output = args['OUTPUT_PATH']
    start = time.time()
    image = cv2.imread(input)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()

    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    corners, ids, rejected = detector.detectMarkers(gray)
    end = time.time()

    print("Detected markers:", ids)
    print("Detection time: {:.4f} seconds".format(end - start))
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(image, corners, ids)
        cv2.imshow('Detected Markers', image)
        cv2.imwrite(output, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()