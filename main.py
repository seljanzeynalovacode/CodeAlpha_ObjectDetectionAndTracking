import cv2
import time
from ultralytics import YOLO

# Load the model from the 'models' folder
model = YOLO('models/yolov8s.pt') 

# Initialize video capture (DSHOW for Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Get frame dimensions for saving the video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Setup VideoWriter to save the result in the 'output' folder
out = cv2.VideoWriter('output/tracking_result.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (frame_width, frame_height))

prev_time = 0

print("Video stream started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Calculate FPS
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if (curr_time - prev_time) > 0 else 0
    prev_time = curr_time

    # Object detection and tracking (conf=0.5 for better accuracy)
    results = model.track(frame, persist=True, conf=0.5)

    # Plot bounding boxes and IDs on the frame
    annotated_frame = results[0].plot()

    # Display FPS on the screen
    cv2.putText(annotated_frame, f"FPS: {fps}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Save the annotated frame to the output video
    out.write(annotated_frame)

    # Show the final frame
    cv2.imshow("YOLOv8 Object Tracking", annotated_frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all resources (camera and video writer)
cap.release()
out.release()
cv2.destroyAllWindows()