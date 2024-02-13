from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("video.mp4", save=True)