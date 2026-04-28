import glob

label_files = glob.glob("train/labels/*.txt") + glob.glob("valid/labels/*.txt")

for file in label_files:
    new_lines = []
    with open(file, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.split()
        parts[0] = "2"
        new_lines.append(" ".join(parts))

    with open(file, "w") as f:
        f.write("\n".join(new_lines))

print("Plate dataset converted to class 2 ✅")