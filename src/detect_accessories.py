from ultralytics import YOLO
import cv2
from collections import Counter
print("start")

def detect_accessories(image_path):
    model = YOLO("../yolov8n.pt")

    results = model(image_path, conf=0.3)

    names = model.names
    detected = []

    for r in results:
        for c in r.boxes.cls:
            detected.append(names[int(c)])

    counts = Counter(detected)
    return counts


if __name__ == "__main__":
    image = "../pole_project/test_images/test2.jpeg"
    accessories = detect_accessories(image)

    print("Detected accessories:")
    for name, count in accessories.items():
        print(f"{name}: {count}")