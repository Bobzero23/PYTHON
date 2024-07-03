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

model = YOLO("../yolo_weights/yolov8n.pt")

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # trying to get the value of the boxes
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # if you don't get the first index only it will not be able to unpack every box that is coming
            x1, y1, x2, y2 = box.xyxy[0]
            # converting the values to integer so that is more readable
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break