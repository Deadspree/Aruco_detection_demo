## Aruco_detection_demo
### Install dependencies
```bash
pip install -r requirements.txt
```



### My local environment(for preference):
* Os: Windows 11
* CPU: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz   2.59 GHz
* python version: 3.10.0
* Detection time(for an image with 5 aruco marker): 0.0157 seconds

### Run the detection
```bash
python detection.py input_image_path output_image_path
```

### Run real-time detection
```bash
python realtime_detect.py input_video_path output_video_path
```