from ultralytics import YOLO
import cv2
# cvzone displaying all the detection
import cvzone

# for rounding the confidence value
import math

# this is for webcam
# this is actually the id number of your camera
# if you have multiple cameras connected you can use (1, 2, etc.)
# cap = cv2.VideoCapture(0)

# this is for videos
cap = cv2.VideoCapture("../media/jaywalking.mp4")

# for the webcam
# setting the width of the cam
# cap.set(3, 1280)
# setting the height of the cam
# cap.set(4, 1020)

model = YOLO("../yolo_weights/yolov8n.pt")

classNames = ["person", "bycycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dot", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "dinningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

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

            # calculating the width and the height
            w, h = x2 - x1, y2 - y1

            # now we create a rectangle for each object we can detect
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            # to put some fancy box we can use binding box (bbx)
            cvzone.cornerRect(img, (x1, y1, w, h))

            # print(x1, y1, x2, y2) this will print the result of the normal method which is not the (cvzone)

            # getting the confidence value (estimated value of the object)
            conf = math.ceil(box.conf[0] * 100) / 100
            print(conf)
            # putting the text of confidence zone to the frame
            # we used max incase the object overflows the frame dimension, and we want to see the 'conf'

            # finding the classes
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(30, y1)))

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
