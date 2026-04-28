import os
import shutil
import glob

datasets = [
    "Bike Helmet Detection.v1i.yolov8",
    "Helmet - No helmet detection.v1i.yolov8",
    "Indian Number Plates.v7i.yolov8",
    "License-Plate-OCR.v1i.yolov8",
    "ocr number plate detection.v1i.yolov8"
]

os.makedirs("merged_dataset/train/images", exist_ok=True)
os.makedirs("merged_dataset/train/labels", exist_ok=True)
os.makedirs("merged_dataset/valid/images", exist_ok=True)
os.makedirs("merged_dataset/valid/labels", exist_ok=True)

for ds in datasets:
    print(f"Processing {ds}...")

    # TRAIN
    for img in glob.glob(f"{ds}/train/images/*.*"):
        shutil.copy(img, "merged_dataset/train/images")

    for lbl in glob.glob(f"{ds}/train/labels/*.txt"):
        shutil.copy(lbl, "merged_dataset/train/labels")

    # VALID
    for img in glob.glob(f"{ds}/valid/images/*.*"):
        shutil.copy(img, "merged_dataset/valid/images")

    for lbl in glob.glob(f"{ds}/valid/labels/*.txt"):
        shutil.copy(lbl, "merged_dataset/valid/labels")

print("All datasets merged successfully ✅")