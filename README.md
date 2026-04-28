📌 Project Overview:
The Smart Helmet Violation Detection System is an AI-based project that detects traffic rule violations such as:

❌ Riding without a helmet

🔢 Automatic number plate recognition (OCR)

📸 Evidence generation (images/videos)

📄 Violation report generation

*This system helps improve road safety by automating monitoring and reducing manual effort.


🎯 Objectives:

1.Detect helmet violations using deep learning

2.Recognize vehicle number plates automatically

3.Generate violation evidence and reports

4.Provide a simple dashboard for monitoring


🛠️ Technologies Used

1.🐍 Python

2.🤖 YOLOv8 (Object Detection)

3.🧠 OpenCV

4.🔤 OCR (EasyOCR / Tesseract

5.📊 Streamlit (UI Dashboard)


📂 Project Structure

Finalyear_project/

│── app.py                  # Main Streamlit application

│── detect_advanced.py      # Detection logic

│── ocr_reader.py           # Number plate OCR

│── tracker.py              # Object tracking

│── utils.py                # Helper functions

│── violations/             # Stored violation images & reports

│── input_videos/           # Input test videos

│── output_videos/          # Output processed videos

│── runs/                   # YOLO results

│── .gitignore


🚀 Features:

✅ Real-time helmet detection

✅ License plate extraction

✅ Violation image capture

✅ CSV report generation

✅ Simple admin login dashboard


🔐 Login Credentials:

Username: Kutty 

Password: 2923


▶️ How to Run the Project:

1️⃣ Clone the Repository:

git clone https://github.com/sravanikuruva29/Sravani.git
cd Finalyear_project

2️⃣ Create Virtual Environment:

python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies:

pip install -r requirements.txt

4️⃣ Run Application:

streamlit run app.py


📊 Output:

1.Detected violations saved in /violations

2.Reports generated as CSV

3.Processed videos saved in /output_videos


⚠️ Note:

Due to size limitations of GitHub, the following files are not included:

1.Trained model (.pt)

2.Dataset (.zip)

3.Large video files

👉 These are available here:https://drive.google.com/drive/folders/1H8BDYKHKGubwL1jtobR_bAh9AYEz2onf?usp=sharing


📸 Screenshots:

Dashboard UI

<img width="1600" height="649" alt="image" src="https://github.com/user-attachments/assets/a0583345-92c8-4f63-9066-6f73bf3ed17a" />
<img width="1600" height="708" alt="image" src="https://github.com/user-attachments/assets/47d780be-17c7-4164-aa9f-d67613e7f6b0" />

Detection results

<img width="1600" height="730" alt="image" src="https://github.com/user-attachments/assets/bf6617df-e9cf-4d28-963b-2c61ba800c6e" />
<img width="296" height="163" alt="image" src="https://github.com/user-attachments/assets/e007878d-0479-49fc-b229-6a1946fb5154" />

Reports

<img width="1600" height="713" alt="image" src="https://github.com/user-attachments/assets/d99d5f32-3f5b-4c4f-ab60-11a6a3b375e2" />


🎓 Academic Info:

👩‍🎓 Student: Sravani Kuruva

🎓 Course: B.Tech

📅 Year: Final Year Project

🏫 College: Rajeev Gandhi Memorial College of Engineering & Technology


🔮 Future Improvements:

1.Live CCTV integration

2.Cloud deployment

3.Mobile app integration

4.Multi-violation detection


📬 Contact:

For queries or collaboration:
📧 Email: sravanikuruva2923@gmail.com


⭐ Acknowledgment:
Thanks to open-source libraries and research in computer vision and deep learning.


⭐ If you like this project:
Give a ⭐ on GitHub!
