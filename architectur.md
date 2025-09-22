# System Architecture

## Overview
The system handles live video frames from a webcam and performs:
- Face Recognition (existing system)
- Gesture Recognition (new Task 3 feature)

## Components
- Camera Input
- Face Recognition Module (encodings, attendance manager)
- Gesture Recognition Module (MediaPipe Hands)
- Logger & CSV storage
- Display / UI (annotated frames)

## Gesture Recognition specifics
- Detect hand presence, handedness (Left/Right), finger count (0-5), and recognize thumbs up/down.
