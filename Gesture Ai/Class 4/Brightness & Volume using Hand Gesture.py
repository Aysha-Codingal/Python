'''Capture webcam frame

Detect hands

Find thumb & index finger

Measure distance

Map distance to:

Volume (left hand)

Brightness (right hand)

Draw visual feedback

Repeat
OpenCV – for webcam and drawing

MediaPipe – for hand tracking

PyCaw – for controlling system volume

screen_brightness_control – for controlling screen brightness

It controls:
It controls:

🎵 Volume using left Hand

💡 Brightness using right Hand '''

import cv2, mediapipe as mp, numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands 
hands = Hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
draw = mp.solutions.drawing_utils

TH,IX = Hands.HandLandmark.THUMS_TIP, Hands.HandLandmark.IDEX_FINGER_TIP

try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Pycaw Error: {e}"); exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened(): print("Error: Webcam Not Accessible.");

WIN = "Hand Gesture Control"; cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1); h, w = img.shape[:2]
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks and res.multi_handeness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handeness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTONS)
            lm = hand.landmark
            tp = (int(lm[TH].x*w), int(lm[TH].y*h)); ip = (int(lm[IX].x*w), int(lm[IX].y*h))


