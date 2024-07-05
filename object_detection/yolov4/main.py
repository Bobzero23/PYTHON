import os.path

import cv2
import numpy as np
import cvzone
import math

# Load YOLO
net = cv2.dnn.readNet("", "")
names_path = "tek/tek.names"

# Load class names from tek.names
with open(names_path, "r") as f:
    if not os.path.exists(names_path):
        print("NAMES PATH NOT FOUND")
    classNames = f.read().strip().split("\n")

# Initialize the video capture (use 0 for webcam or provide video file path)
cap = cv2.VideoCapture(0)  # Use 0 for webcam

while True:
    success, img = cap.read()
    if not success:
        break

    height, width, channels = img.shape

    # Create a blob from the image
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Run forward pass to get the detections
    outs = net.forward(net.getUnconnectedOutLayersNames())

    # Initialize lists to hold detected bounding boxes, confidences, and class IDs
    class_ids = []
    confidences = []
    boxes = []

    # Process each detection
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # filter out weak detections
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-max suppression to remove redundant overlapping boxes with lower confidences
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes on the image
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classNames[class_ids[i]])
            conf = confidences[i]
            cvzone.cornerRect(img, (x, y, w, h))
            cvzone.putTextRect(img, f'{label} {conf:.2f}', (max(0, x), max(30, y)))

    # Display the resulting frame
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
