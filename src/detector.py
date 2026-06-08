from ultralytics import YOLO
import cv2

yolo_model = YOLO("yolov8n.pt")

def run_detection(img_path):

    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError("Image not found")

    results = yolo_model(img)
    annotated = results[0].plot()

    detected_objects = []
    person_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = yolo_model.names[cls]

            detected_objects.append(label)

            if label == "person":
                person_count += 1

    return results, annotated, detected_objects, person_count