import glob

mapping = {
    0: 0,  # 1-2-helmet → helmet
    1: 0,  # 3-4-helmet → helmet
    2: 1,  # Bald → no_helmet
    3: 1,  # Cap → no_helmet
    4: 1,  # Face and Hair → no_helmet
    5: 0   # Full-face-helmet → helmet
}

label_files = glob.glob("train/labels/*.txt") + glob.glob("valid/labels/*.txt")

for file in label_files:
    new_lines = []
    with open(file, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.split()
        old_class = int(parts[0])
        parts[0] = str(mapping[old_class])
        new_lines.append(" ".join(parts))

    with open(file, "w") as f:
        f.write("\n".join(new_lines))

print("Dataset 2 remapped successfully ✅")