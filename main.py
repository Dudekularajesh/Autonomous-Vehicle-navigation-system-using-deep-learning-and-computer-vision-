import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *
import time
import csv
from collections import defaultdict

# Load YOLO model
model = YOLO('yolov8s.pt')

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', lambda e, x, y, f, p: print([x, y]) if e == cv2.EVENT_MOUSEMOVE else None)

cap = cv2.VideoCapture('rajesh.mp4')

# Load COCO class names
with open("coco.txt", "r") as f:
    class_list = f.read().split("\n")

count = 0
tracker = Tracker()

# Setup output files
csv_file = open("object_speeds.csv", mode="w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Frame", "Object ID", "Class", "Speed (km/h)"])

vh_time = {}  # Object ID → last seen time
high_speed_cars = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    px = pd.DataFrame(results[0].boxes.data).astype("float")

    detections = []
    object_counts = defaultdict(int)

    for _, row in px.iterrows():
        x1, y1, x2, y2, _, class_id = map(int, row[:6])
        class_name = class_list[class_id]
        detections.append([x1, y1, x2, y2, class_name])
        object_counts[class_name] += 1

    bbox_id = tracker.update([d[:4] for d in detections])

    for i, bbox in enumerate(bbox_id):
        x3, y3, x4, y4, obj_id = bbox
        cx, cy = (x3 + x4) // 2, (y3 + y4) // 2
        class_name = detections[i][4]

        cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)
        cv2.putText(frame, f"{class_name}-{obj_id}", (x3, y3 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        # Speed detection only for 'car'
        speed_kmh = ""
        if class_name == "car":
            current_time = time.time()
            if obj_id in vh_time:
                elapsed_time = current_time - vh_time[obj_id]
                if elapsed_time > 0.1:
                    speed_mps = 10 / elapsed_time  # Assume fixed distance
                    speed_kmh = speed_mps * 3.6
                    color = (0, 255, 0) if speed_kmh < 40 else (0, 0, 255)
                    cv2.putText(frame, f"{int(speed_kmh)} Km/h", (x4, y4), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                    csv_writer.writerow([count, obj_id, class_name, f"{speed_kmh:.2f}"])
                    if speed_kmh > 40 and obj_id not in high_speed_cars:
                        high_speed_cars.append(obj_id)
                        with open("over_speeding_cars_ID.txt", "a") as f:
                            f.write(f"{obj_id}\n")
            vh_time[obj_id] = current_time
        else:
            csv_writer.writerow([count, obj_id, class_name, ""])

    # Show object counts on screen
    y_pos = 30
    for cls, cnt in object_counts.items():
        cv2.putText(frame, f"{cls}: {cnt}", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1)
        y_pos += 20

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

csv_file.close()
cap.release()
cv2.destroyAllWindows()
