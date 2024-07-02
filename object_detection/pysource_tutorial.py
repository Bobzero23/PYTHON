import cv2

cap = cv2.VideoCapture(0)

# opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn-model/yolov4.tiny.cfg")
model = cv2.dnn_DetectionModel();

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
