from collections import Counter
import glob
import os

counter = Counter()

# Absolute path (safer)
base_path = os.path.join(os.getcwd(), "merged_dataset", "train", "labels")

print("Checking folder:", base_path)

label_files = glob.glob(os.path.join(base_path, "*.txt"))

print("Total label files found:", len(label_files))

for file in label_files:
    with open(file, "r") as f:
        for line in f:
            cls = line.split()[0]
            counter[cls] += 1

print("Class distribution:", counter)