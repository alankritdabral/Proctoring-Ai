from mss import mss
import numpy as np
import cv2
import datetime

# Define the screen capture area
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}  # Adjust the width and height based on your screen resolution

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(filename, fourcc, 20.0, (monitor["width"], monitor["height"]))

webcam = cv2.VideoCapture(0)

with mss() as sct:
    while True:
        # Capture screen
        img = sct.grab(monitor)
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        # Capture webcam
        ret, frame = webcam.read()
        if not ret:
            print("Failed to capture image from webcam")
            break
        frame_h, frame_w, _ = frame.shape
        if frame_h > monitor["height"] or frame_w > monitor["width"]:
            print("Webcam frame size exceeds screen size")
            continue
        img_final[0:frame_h, 0:frame_w, :] = frame[0:frame_h, 0:frame_w, :]  # Overlay webcam on screen

        cv2.imshow('Capture', img_final)
        captured_video.write(img_final)

        if cv2.waitKey(10) == ord('q'):
            break

webcam.release()
captured_video.release()
cv2.destroyAllWindows()
