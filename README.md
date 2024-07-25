# Proctoring System with Audio and Head Pose Detection

This project implements a proctoring system that detects suspicious behavior using both audio and head pose data. The system monitors audio levels and head movements to identify potential cheating in real-time. It uses various tools and libraries for audio processing, head pose estimation, and data visualization.

## Components

- **Audio Detection**: Monitors audio input to detect suspicious noise patterns.
- **Head Pose Estimation**: Analyzes head movements to determine if the subject is looking away from the screen.
- **Cheating Probability Calculation**: Combines data from audio and head pose detection to estimate the probability of cheating.
- **Visualization**: Plots the cheating probability over time using Matplotlib.
- **User Interface**: Provides a basic GUI (optional) for interacting with the system.

## Tools and Libraries

- **sounddevice**: For real-time audio capturing and processing.
- **numpy**: For numerical operations on audio data and mathematical calculations.
- **mediapipe**: For face detection and head pose estimation.
- **cv2 (OpenCV)**: For video capture and image processing.
- **matplotlib**: For data visualization and plotting.
- **threading**: For running different components concurrently.
- **tkinter**: For creating a graphical user interface (optional).

### Prerequisites
To run the programs in this repo, do the following:
- create a virtual environment using the command:
  - `python -m venv venv`
- activate the virtual environment
  - `cd ./venv/Scripts/activate` (windows users)
  - `source ./venv/bin/activate` (mac and linux users)
- install the requirements
  - `pip install --upgrade pip` (to upgrade pip)
  - `pip install -r requirements.txt`

Once the requirements have been installed, the programs will run successfully.
To run the software use: 
```python 
python run.py
```