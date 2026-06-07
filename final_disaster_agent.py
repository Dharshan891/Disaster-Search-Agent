from ultralytics import YOLO
import cv2
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# -------------------------------
# Load Models
# -------------------------------
yolo_model = YOLO("yolov8n.pt")
classifier = tf.keras.applications.MobileNetV2(weights='imagenet')

# -------------------------------
# Load Image
# -------------------------------
img_path = r"C:\Users\himas\Downloads\DisasterSearchAgent\test.jpg\flood 1.jpg"
img_cv = cv2.imread(img_path)

if img_cv is None:
    print("Error: Image not found!")
    exit()

# -------------------------------
# YOLO Detection (Survivors)
# -------------------------------
results = yolo_model(img_cv)
annotated = results[0].plot()

# Count persons
person_count = 0
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        if yolo_model.names[cls] == "person":
            person_count += 1

# -------------------------------
# Disaster Type from YOLO Objects
# -------------------------------
detected_objects = []

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        detected_objects.append(yolo_model.names[cls])

print("Detected Objects:", detected_objects)  # DEBUG LINE

# Better logic
if "boat" in detected_objects:
    disaster = "Flood"
elif "person" in detected_objects and len(detected_objects) > 5:
    disaster = "Flood (Rescue Situation)"
elif "fire" in detected_objects:
    disaster = "Fire"
else:
    disaster = "Unknown Disaster"
    
# -------------------------------
# Print Results
# -------------------------------
print("\n===== FINAL OUTPUT =====")
print(f"Disaster Type: {disaster}")
print(f"Survivors Detected: {person_count}")

# -------------------------------
# Show Output
# -------------------------------
cv2.imshow("Final Disaster Search Agent", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output image
cv2.imwrite("output.jpg", annotated)