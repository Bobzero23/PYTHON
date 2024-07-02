import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Try different camera indices if the current one doesn't work
video = cv2.VideoCapture(0)  # Try 0, 1, 2, etc.

if not video.isOpened():
    print("Error: Could not open video source.")
    exit()

while True:
    ret, frame = video.read()
    if not ret or frame is None:
        print("Error: Could not read frame.")
        break

    # Detect objects in the frame
    bbox, label, conf = cv.detect_common_objects(frame)

    # Draw bounding boxes on the frame
    output_image = draw_bbox(frame, bbox, label, conf)

    # Display the frame with bounding boxes
    cv2.imshow("Object detection", output_image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
