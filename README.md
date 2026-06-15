# 🍎 Apple Quality Detection using YOLOv8

Detects and classifies apples as **ripe**, **rotten**, or **unripe** 
using YOLOv8 object detection model.

## Results
- Precision: 99.3%
- Recall: 96.9%
- mAP50: 98.4%

## Classes
- 🍎 ripe_apple
- 🍂 rotten_apple  
- 🟢 unripe_apple

## How to run
pip install ultralytics opencv-python
python detect.py

## Dataset
3800+ images from Roboflow Universe
Trained on Google Colab with T4 GPU
