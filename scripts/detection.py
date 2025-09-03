
# Standard Library
import time
import argparse
# External Library
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Aruco Marker Detection")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to output image")

    args = parser.parse_args()
   
    input = args.input
    output = args.output
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