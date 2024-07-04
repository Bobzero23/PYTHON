import cv2
import torch
from yolov4 import YOLOv4
from deep_sort import DeepSORT

# Initialize YOLOv4
yolo = YOLOv4()
yolo.load_model()

# Initialize DeepSORT
tracker = DeepSORT()

# Initialize video capture
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    detections = yolo.detect(frame)

    # Update tracker
    tracked_objects = tracker.update(detections)

    # Draw bounding boxes and IDs
    for obj in tracked_objects:
        bbox = obj['bbox']
        id = obj['id']
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)
        cv2.putText(frame, str(id), (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
