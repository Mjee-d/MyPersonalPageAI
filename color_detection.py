import cv2
import numpy as np

cap = cv2.VideoCapture(0)

colors_to_track = {
    "Blue": {
        "lower": np.array([90, 50, 50]),
        "upper": np.array([130, 255, 255]),
        "bgr_color": (255, 0, 0)
    },
    "Orange": {
        "lower": np.array([5, 100, 100]),
        "upper": np.array([15, 255, 255]),
        "bgr_color": (0, 165, 255)
    },
    "Red": {
        "lower": np.array([170, 120, 70]),
        "upper": np.array([180, 255, 255]),
        "bgr_color": (0, 0, 255)
    }
}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Video file not found, incompatible format, or finished.")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, color_data in colors_to_track.items():
        mask = cv2.inRange(hsv_frame, color_data["lower"], color_data["upper"])
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 800:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_data["bgr_color"], 2)
                label = f"{color_name} Detected"
                cv2.putText(frame, label, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_data["bgr_color"], 2)

    cv2.imshow('Multi-Color Tracking Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()