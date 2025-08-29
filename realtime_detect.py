# Standard Library
import time
import argparse
import logging
from pathlib import Path
from typing import Tuple, Optional

# External Library
import cv2
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("video_loader.log"), 
        logging.StreamHandler()                   
    ]
)


def process_video(input_path: str, output_path: str) -> None:
     """
     ! Process a video stream frame-by-frame using aruco_deteciton().

     @input_path (str): Path to the input video
     @output_path (str): Path to the output video

     """

     input = Path(input_path)
     output = Path(output_path)

     if not input.exists():
         logging.error(f"Video file not found: {input}")
         raise FileNotFoundError(f"Video file not found: {input}")
     
     cap = cv2.VideoCapture(str(input))
     frame_count = 0
     logging.info("Starting video processing... Press 'q' to quit. ")

     out = None
     if output:
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output, fourcc, 30.0, (width, height))
        logging.info(f"Saving processed video to {output}")
     start_time = time.time()

     while True:
         ret, frame = cap.read()
         if not ret:
             break
         
         detected_frame, ids, corners = aruco_detection(frame)
         frame_count += 1

         elapsed_time = time.time() - start_time
         if elapsed_time > 0:
            fps_live = frame_count / elapsed_time
            cv2.putText(detected_frame, f"FPS: {fps_live:.2f}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 255, 0), 2)
         cv2.imshow("Aruco_detection_realtime", detected_frame)
         out.write(detected_frame)
         if cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info("User pressed 'q'. Exiting video loop.")
            break
    
     cap.release()
     if out:
         out.release()
     cv2.destroyAllWindows()         

def aruco_detection(frame: np.ndarray,
                    dictionary: int = cv2.aruco.DICT_6X6_250,
                    draw: bool = True) -> Tuple[np.ndarray, Optional[np.ndarray], Optional[list[np.ndarray]]]:
    """
    !Perform Aruco_detection on 1 frame and visualize

    @frame (np.ndarray): Input image (BGR format)
    @dictionary (int): AurUco dictionary type. 
    @draw (bool): Whether to draw markers on the frame. 

    """
    if frame is None:
        logging.error("Input frame is None.")
        return frame, None, None
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary)
    parameters = cv2.aruco.DetectorParameters()

    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    corners, ids, rejected = detector.detectMarkers(gray)
    output_frame = frame.copy()
    if draw and ids is not None:
        cv2.aruco.drawDetectedMarkers(output_frame, corners, ids)

    if ids is not None:
        logging.info(f"Detected {len(ids)} markers: {ids.flatten().tolist()}")
    else:
        logging.info("No markers detected in this frame.")


    return output_frame, ids, corners

def main():
    """
    !Aruco realtime detection pipeline

    Usage: realtime_detect.py input_path output_path

    """
    parser = argparse.ArgumentParser(description="Aruco Marker Detection")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to output image")

    args = parser.parse_args()
   
    input = args.input
    output = args.output
    process_video(input,output)



if __name__ == "__main__":
    main()