from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("image.jpeg", save=True)