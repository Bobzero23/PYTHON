from ultralytics import YOLO
import cv2
# cvzone displaying all the detection
import cvzone

# this is actually the id number of your camera
# if you have multiple cameras connected you can use (1, 2, etc.)
cap = cv2.VideoCapture(0)

# setting the width of the cam
cap.set(3, 680)
# setting the height of the cam
cap.set(4, 720)

model = YOLO("")

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break