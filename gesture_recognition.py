import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

finger_tips = [
    mp_hands.HandLandmark.INDEX_FINGER_TIP,
    mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
    mp_hands.HandLandmark.RING_FINGER_TIP,
    mp_hands.HandLandmark.PINKY_TIP
]
finger_dips = [
    mp_hands.HandLandmark.INDEX_FINGER_DIP,
    mp_hands.HandLandmark.MIDDLE_FINGER_DIP,
    mp_hands.HandLandmark.RING_FINGER_DIP,
    mp_hands.HandLandmark.PINKY_DIP
]

def count_fingers(hand_landmarks, handedness_str):
    count = 0
    for tip, dip in zip(finger_tips, finger_dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            count += 1
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if handedness_str == "Left":
        if thumb_tip.x < thumb_ip.x:
            count += 1
    else:
        if thumb_tip.x > thumb_ip.x:
            count += 1
    return count

def recognize_gesture(hand_landmarks, handedness_str):
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    for tip, dip in zip(finger_tips, finger_dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            return None
    if thumb_tip.y < wrist.y - 0.1:
        return "Thumbs Up"
    elif thumb_tip.y > wrist.y + 0.1:
        return "Thumbs Down"
    return None

def process_frame(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    detections = []
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            label = handedness.classification[0].label
            fingers = count_fingers(hand_landmarks, label)
            gesture = recognize_gesture(hand_landmarks, label)
            detections.append((label, fingers, gesture))
    return frame, detections
