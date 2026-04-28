import cv2
from ultralytics import YOLO

# Load model
model = YOLO("best.pt")

# Test on a sample image (replace with your image path)
img_path = "C:\\Users\\kuruv\\Downloads\\Finalyear_project\\merged_dataset\\train\\images\\BikesHelmets354_png_jpg.rf.0ae86b8fdf8da51814d77211e85c801d.jpg"  # Update this
img = cv2.imread(img_path)
results = model(img)

# Print detections
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]
        print(f"Detected: {label} with confidence {conf:.2f}")

print("Test complete. Check detections above.")