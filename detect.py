from ultralytics import YOLO

model = YOLO('best.pt')

results = model.predict(source='apple.jpeg', conf=0.5, save=True)

for result in results:
    for box in result.boxes:
        label = result.names[int(box.cls)]
        confidence = float(box.conf)
        print(f'Detected: {label} ({confidence:.2%} confidence)')

print('Done!')