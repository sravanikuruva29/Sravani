import cv2

cap = cv2.VideoCapture("input_video.mp4/4887861-uhd_3840_2160_30fps.mp4")

print("Video opened:", cap.isOpened())

ret, frame = cap.read()
print("Frame read:", ret)

cap.release()