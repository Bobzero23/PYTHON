from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
result = model("Images/1.jpg", show=True)
# run it here so it downloads the dependencies

cv2.waitKey(0)
