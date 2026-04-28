import streamlit as st
import cv2
import pandas as pd
import easyocr
import re
import os
import tempfile
import numpy as np
import time
from ultralytics import YOLO
from datetime import datetime
from reportlab.pdfgen import canvas

# ---------------- PAGE ----------------
st.set_page_config(page_title="Smart Traffic AI", layout="wide")

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 Admin Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "Kutty" and pwd == "2923":
            st.session_state.logged_in = True
            st.success("Login Successful ✅")
        else: 
            st.error("Invalid Credentials ❌")

    st.stop()

# ---------------- MAIN ----------------
st.title("🚦 Smart Helmet Violation System")

menu = st.sidebar.radio(
    "Navigation",
    [
        "👥 Team",
        "🔄 Flowchart",
        "🎥 Detection",
        "📉 Dashboard",
        "📈 Analytics"
    ]
)

# ---------------- FOLDERS ----------------
os.makedirs("violations", exist_ok=True)
os.makedirs("challans", exist_ok=True)

# ---------------- SESSION ----------------
if "violations" not in st.session_state:
    st.session_state.violations = []

# ---------------- MODEL ----------------
model = YOLO("best.pt")
reader = easyocr.Reader(['en'])

# ---------------- OCR ----------------
def read_plate(img):
    results = reader.readtext(img)
    for r in results:
        text = r[1].upper()
        text = re.sub(r'[^A-Z0-9]', '', text)
        if len(text) >= 5:
            return text
    return ""

# ---------------- CHALLAN ----------------
def generate_challan(plate, time):
    path = f"challans/{plate}_{time}.pdf"
    c = canvas.Canvas(path)
    c.drawString(200,800,"Traffic Violation Challan")
    c.drawString(100,740,f"Vehicle: {plate}")
    c.drawString(100,710,"Violation: No Helmet")
    c.drawString(100,680,f"Time: {time}")
    c.drawString(100,650,"Fine: ₹500")
    c.save()
    return path

# =========================
# 👥 TEAM
# =========================
if menu == "👥 Team":

    st.header("Project Team")

    st.markdown("""
    ### 👨‍💻 Team Members:
    - Kuruva Sravani (22091A32E2)
    - Dasari Sujitha (22091A32E8)
    - Mangali Umarani (22091A32F7)

    ### 👨‍🏫 Mentor:
    - Supervisor - Dr. M. Suleman Basha 
    - Co-Supervisor - Ms. K. Rathi 
                
    ### 🎓 College:
    - Rajeev Gandhi Memorial College of Engineering and Technology  
    """)

# =========================
# 🔄 FLOWCHART
# =========================
elif menu == "🔄 Flowchart":

    st.header("System Flow")

    st.code("""
    Video Input
        ↓
    YOLO Detection
        ↓
    Helmet?
     ├─ Yes → Ignore
     └─ No
          ↓
    Plate Region Extraction
          ↓
    OCR Processing
          ↓
    Save Image + Generate Challan
    """)

# =========================
# 🎥 DETECTION
# =========================
# =========================
# 🎥 DETECTION (LIVE SAVE + TABLE)
# =========================
elif menu == "🎥 Detection":

    mode = st.radio("Select Mode", ["Upload Video", "Webcam"])

    frame_box = st.empty()
    fps_box = st.empty()
    table_box = st.empty()   # 🔥 LIVE TABLE
    log_box = st.empty()     # 🔥 SAVE MESSAGE

    if mode == "Upload Video":

        video = st.file_uploader("Upload Video")

        if video:
            temp = tempfile.NamedTemporaryFile(delete=False)
            temp.write(video.read())
            cap = cv2.VideoCapture(temp.name)

    else:
        cap = cv2.VideoCapture(0)

    if st.button("Start Detection"):

        seen_plates = set()  # 🔥 avoid duplicates

        while True:

            ret, frame = cap.read()
            if not ret:
                break

            start = time.time()

            results = model(frame)[0]
            no_helmet_boxes = []

            for box in results.boxes:

                cls = int(box.cls[0])
                label = model.names[cls]
                conf = float(box.conf[0])

                x1,y1,x2,y2 = map(int, box.xyxy[0])

                if label == "helmet":
                    color = (0,255,0)

                elif label == "no_helmet":
                    color = (0,0,255)
                    no_helmet_boxes.append((x1,y1,x2,y2))

                else:
                    color = (255,0,0)

                cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
                cv2.putText(frame,f"{label} {conf:.2f}",
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)

            # -------- PLATE DETECTION --------
            for (x1,y1,x2,y2) in no_helmet_boxes:

                h,w,_ = frame.shape

                px1 = max(0, x1-60)
                px2 = min(w, x2+60)
                py1 = y2
                py2 = min(h, y2+250)

                crop = frame[py1:py2, px1:px2]

                if crop.size == 0:
                    continue

                cv2.rectangle(frame,(px1,py1),(px2,py2),(255,255,0),2)

                gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray,None,fx=2,fy=2)

                plate = read_plate(gray)

                # 🔥 VALIDATION
                if plate != "" and plate not in seen_plates:

                    seen_plates.add(plate)

                    time_now = datetime.now().strftime("%H-%M-%S")

                    img_path = f"violations/{plate}_{time_now}.jpg"
                    cv2.imwrite(img_path, frame)

                    pdf = generate_challan(plate,time_now)

                    st.session_state.violations.append({
                        "Plate": plate,
                        "Time": time_now,
                        "Image": img_path,
                        "PDF": pdf
                    })

                    # 🔥 LIVE MESSAGE
                    log_box.success(f"✅ Saved: {plate}")

                    # 🔥 LIVE TABLE UPDATE
                    df = pd.DataFrame(st.session_state.violations)
                    table_box.dataframe(df)

            # -------- FPS --------
            fps = 1/(time.time()-start)
            fps_box.write(f"FPS: {int(fps)}")

            frame_box.image(frame, channels="BGR")

        cap.release()

# =========================
# 📉 DASHBOARD
# =========================
elif menu == "📉 Dashboard":

    if len(st.session_state.violations)>0:

        df = pd.DataFrame(st.session_state.violations)
        st.dataframe(df)

        for v in st.session_state.violations:
            st.image(v["Image"], width=300)

            with open(v["PDF"], "rb") as f:
                st.download_button(
                    f"Download {v['Plate']}",
                    f,
                    file_name=v["PDF"]
                )

    else:
        st.warning("No violations yet")

# =========================
# 📈 ANALYTICS
# =========================
elif menu == "📈 Analytics":

    if len(st.session_state.violations)>0:

        df = pd.DataFrame(st.session_state.violations)

        st.metric("Total Violations", len(df))
        st.bar_chart(df["Plate"].value_counts())

    else:
        st.info("No data")