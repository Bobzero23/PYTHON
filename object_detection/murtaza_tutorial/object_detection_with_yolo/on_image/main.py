from ultralytics import YOLO
import cv2

model = YOLO('../yolo_weights/yolov8n.pt')
# show=True means that it will show everything (frames, names, etc.)
result = model("../Images/2.jpg", show=True)
# run it here so it downloads the dependencies

cv2.waitKey(0)
