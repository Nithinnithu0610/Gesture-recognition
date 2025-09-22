import cv2
import mediapipe as mp
import json
from datetime import datetime

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

FINGER_TIPS = [
    mp_hands.HandLandmark.INDEX_FINGER_TIP,
    mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
    mp_hands.HandLandmark.RING_FINGER_TIP,
    mp_hands.HandLandmark.PINKY_TIP
]
FINGER_DIP = [
    mp_hands.HandLandmark.INDEX_FINGER_DIP,
    mp_hands.HandLandmark.MIDDLE_FINGER_DIP,
    mp_hands.HandLandmark.RING_FINGER_DIP,
    mp_hands.HandLandmark.PINKY_DIP
]

LOG_FILE = 'gesture.log'

def log_gesture(entry: dict):
    """Append gesture event to gesture.log as JSON."""
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass

def count_fingers(hand_landmarks, handedness_str):
    """Count number of extended fingers (0–5)."""
    count = 0
    for tip, dip in zip(FINGER_TIPS, FINGER_DIP):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            count += 1

    # Thumb detection depends on Left/Right hand
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    if handedness_str.lower().startswith('l'):  # Left hand
        if thumb_tip.x < thumb_ip.x:
            count += 1
    else:  # Right hand
        if thumb_tip.x > thumb_ip.x:
            count += 1
    return count

def recognize_gesture(hand_landmarks, handedness_str):
    """Recognize Thumbs Up / Thumbs Down gestures."""
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

    # Ensure other fingers are folded
    for tip, dip in zip(FINGER_TIPS, FINGER_DIP):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            return None

    if thumb_tip.y < wrist.y - 0.08:  # Thumb above wrist
        return 'Thumbs Up'
    if thumb_tip.y > wrist.y + 0.08:  # Thumb below wrist
        return 'Thumbs Down'
    return None

def process_frame(frame):
    """Process a frame: detect hands, count fingers, recognize gestures."""
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands_detector.process(img_rgb)
    detections = []

    if results.multi_hand_landmarks:
        for lm, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)
            label = handedness.classification[0].label  # Left / Right
            fingers = count_fingers(lm, label)
            gesture = recognize_gesture(lm, label)

            # Log event
            entry = {
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'hand': label,
                'fingers': int(fingers),
                'gesture': gesture
            }
            log_gesture(entry)

            detections.append((label, int(fingers), gesture))

    return frame, detections
