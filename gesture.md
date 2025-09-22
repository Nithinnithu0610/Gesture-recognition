# Gesture Recognition Module

## Overview
This module detects hand gestures in live video feed using **MediaPipe Hands**.

## Functions
- count_fingers(hand_landmarks, handedness) → returns integer (0–5)  
- recognize_gesture(hand_landmarks, handedness) → returns "Thumbs Up", "Thumbs Down", or None  
- process_frame(frame) → processes one frame and returns annotated frame + detections  

## Outputs
Each detection has:
- Hand Type: Left or Right
- Finger Count
- Gesture (if recognized)
