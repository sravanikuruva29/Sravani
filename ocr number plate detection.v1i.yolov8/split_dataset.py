import os
import shutil
import random
from glob import glob

base_path = "."

images = glob("train/images/*")
random.shuffle(images)

split_index = int(len(images) * 0.8)

train_imgs = images[:split_index]
val_imgs = images[split_index:]

os.makedirs("valid/images", exist_ok=True)
os.makedirs("valid/labels", exist_ok=True)

for img in val_imgs:
    shutil.move(img, "valid/images")
    label = img.replace("images", "labels").replace(".jpg", ".txt").replace(".png", ".txt")
    if os.path.exists(label):
        shutil.move(label, "valid/labels")

print("Validation created successfully ✅")