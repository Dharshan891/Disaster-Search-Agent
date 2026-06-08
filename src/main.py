from src.detector import run_detection
from src.disaster_logic import get_disaster_type

img_path = "data/flood 1.jpg"

results, annotated, detected_objects, person_count = run_detection(img_path)

disaster = get_disaster_type(detected_objects)

print("\n===== FINAL OUTPUT =====")
print(f"Disaster Type: {disaster}")
print(f"Survivors Detected: {person_count}")s