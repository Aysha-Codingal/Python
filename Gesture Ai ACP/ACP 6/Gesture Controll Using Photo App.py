import cv2
import mediapipe as mp
import time
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

filters = [None, 'GRAYSCALE', 'SEPIA', 'NEGATIVE', 'BLUR']
current_filter = 0
last_action_time = 0
debounce_time = 1

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    exit()

def apply_filter(frame, filter_type):
    if filter_type == 'GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'SEPIA':
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]]).T
        return np.clip(cv2.transform(frame, sepia_filter), 0, 255).astype(np.uint8)
    elif filter_type == 'NEGATIVE':
        return cv2.bitwise_not(frame)
    elif filter_type == 'BLUR':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            h, w, _ = img.shape
            tips = [hand_landmarks.landmark[i] for i in [4, 8, 12, 16, 20]]
            pts = [(int(pt.x * w), int(pt.y * h)) for pt in tips]

            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
            for pt, color in zip(pts, colors):
                cv2.circle(img, pt, 10, color, cv2.FILLED)

            current_time = time.time()
            tx, ty = pts[0]

            def is_touching(pt):
                return abs(tx - pt[0]) < 30 and abs(ty - pt[1]) < 30

            if is_touching(pts[1]):  # Index finger
                if current_time - last_action_time > debounce_time:
                    cv2.putText(img, "Picture Captured!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    last_action_time = current_time
                    cv2.imwrite(f"picture_{int(time.time())}.jpg", img)
                    print("Picture saved!")

            elif any(is_touching(pt) for pt in pts[2:]):  # Middle, Ring, or Pinky
                if current_time - last_action_time > debounce_time:
                    current_filter = (current_filter + 1) % len(filters)
                    last_action_time = current_time
                    print(f"Switched to filter: {filters[current_filter]}")

    filtered_img = apply_filter(img, filters[current_filter])

    if filters[current_filter] == 'GRAYSCALE':
        filtered_img = cv2.cvtColor(filtered_img, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Gesture-Controlled Photo App", filtered_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()