import cv2
import os
import pandas as pd
from ultralytics import YOLO
import easyocr
from sort import Sort
import numpy as np

# ----------------------------
# LOAD MODELS
# ----------------------------

helmet_model = YOLO("best.pt")
plate_model = YOLO("best.pt")

reader = easyocr.Reader(['en'])

# ----------------------------
# TRACKER
# ----------------------------

tracker = Sort()

# ----------------------------
# VIDEO INPUT
# ----------------------------

video_path = "input_video.mp4/4887861-uhd_3840_2160_30fps.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video")
    exit()

print("Video loaded successfully")

# ----------------------------
# OUTPUT VIDEO
# ----------------------------

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (width, height))

# ----------------------------
# OUTPUT FOLDERS
# ----------------------------

os.makedirs("violations/images", exist_ok=True)
os.makedirs("violations/plates", exist_ok=True)

data = []
frame_id = 0

# ----------------------------
# PROCESS VIDEO
# ----------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_id += 1

    detections = []

    results = helmet_model(frame)

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])
            label = helmet_model.names[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            detections.append([x1, y1, x2, y2, conf])

    detections = np.array(detections)

    tracks = tracker.update(detections)

    for track in tracks:

        x1, y1, x2, y2, track_id = map(int, track)

        rider = frame[y1:y2, x1:x2]

        label = "rider"

        # ------------------------
        # HELMET CHECK
        # ------------------------

        helmet_results = helmet_model(rider)

        for hr in helmet_results:

            for box in hr.boxes:

                cls = int(box.cls[0])
                label = helmet_model.names[cls]

        # ------------------------
        # DEBUG PRINT
        # ------------------------

        print("Checking label:", label)

        # ------------------------
        # NO HELMET VIOLATION
        # ------------------------

        if label == "no_helmet":

            print("Violation detected!")

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

            cv2.putText(frame,
                        f"No Helmet ID:{track_id}",
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,0,255),
                        2)

            # ------------------------
            # NUMBER PLATE DETECTION
            # ------------------------

            plate_results = plate_model(rider)

            plate_text = ""

            for pr in plate_results:

                for pbox in pr.boxes:

                    px1, py1, px2, py2 = map(int, pbox.xyxy[0])

                    plate_crop = rider[py1:py2, px1:px2]

                    ocr = reader.readtext(plate_crop)

                    if len(ocr) > 0:

                        plate_text = ocr[0][-2]

                        cv2.imwrite(
                            f"violations/plates/{frame_id}_{track_id}.jpg",
                            plate_crop
                        )

            cv2.imwrite(
                f"violations/images/{frame_id}_{track_id}.jpg",
                frame
            )

            data.append([frame_id, track_id, plate_text])

        else:

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            cv2.putText(frame,
                        f"Helmet ID:{track_id}",
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)

    out.write(frame)

# ----------------------------
# SAVE CSV
# ----------------------------

df = pd.DataFrame(data,
                  columns=["Frame","Track_ID","Plate_Number"])

df.to_csv("violations.csv", index=False)

# ----------------------------
# RELEASE
# ----------------------------

cap.release()
out.release()

print("Processing completed")
print("Advanced detection video saved")