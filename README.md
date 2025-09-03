# Aruco_detection_demo
## Install dependencies
```bash
pip install -r requirements.txt
```



## My local environment(for preference):
* Os: Windows 11
* CPU: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz   2.59 GHz
* python version: 3.10.0
* Detection time(for an image with 5 aruco marker): 0.0157 seconds

## Run realtime pose_estimation
```bash
python script/pose_estimation.py input_image_path output_image_path
```

## Run real-time detection
```bash
python realtime_detect.py input_video_path output_video_path
```

## Guidance on how to build images and run pose_estimation.py code in the container using Docker
* Build the Docker images, install all dependencies and run the container
```bash
docker-compose build
docker-compose up -d
docker exec -it aruco_marker_container bash
```
* Run the script for pose_estimation
```bash
python3 scripts/pose_estimation.py input/pose_input.mp4 output/pose_output.mp4
```