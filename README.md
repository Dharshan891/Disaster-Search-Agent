# Disaster-Search-Agent
An AI-powered Disaster Search Agent that detects survivors and identifies disaster types from disaster scene images using YOLOv8 object detection and computer vision techniques.

# Project Overview
Natural disasters such as floods, earthquakes, and fires make rescue operations difficult and time-consuming. This project uses Artificial Intelligence to automatically detect survivors and analyze disaster scenarios from images, helping rescue teams make faster and more informed decisions.

# 🎯 Features
Detects survivors in disaster images
Identifies disaster type (Flood, Fire, etc.)
Uses YOLOv8 for real-time object detection
Generates annotated images with bounding boxes
Provides survivor count and disaster classification
Fast and efficient image analysis

# 🛠️ Technologies Used
Python
YOLOv8 (Ultralytics)
OpenCV
Computer Vision
Deep Learning

# ⚙️ Workflow
Input disaster image
YOLO detects objects (people, boats, etc.)
Count detected survivors
Apply disaster classification logic
Generate annotated image
Display disaster type and survivor count

# 📁 Project Structure
```text
DISASTER_SEARCH_AGENT/
│
│
├── data/
│   ├── flood1.jpg            # Input disaster images
│
├── models/
│   └── yolov8n.pt            # YOLO model weights
│
├── src/
│   ├── detector.py           # YOLO object detection logic
│   ├── disaster_logic.py     # Disaster assessment & rescue logic
│   ├── main.py               # Application entry point
│   └── utils.py              # Helper functions
│
├── requirements.txt
├── README.md
└── .gitignore
```

# 📊 Sample Output
Input: Flood disaster image
Output:
Survivors Detected: 7
Disaster Type: Flood
