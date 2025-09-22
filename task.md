# Gesture Recognition Task

## Objective
Extend the current **Face Recognition Attendance System** by adding **Hand Gesture Detection** features.

The system should be able to:
1. Detect **if a hand is present** in the camera feed.
2. Identify **which hand it is** (Left Hand or Right Hand).
3. Count the **number of fingers** being shown.
4. Recognize **specific gestures** like:
   - 👍 Thumbs Up
   - 👎 Thumbs Down

---

## Inputs & Outputs

### Input
- **Live video frames** from the Camera (same input source as face recognition).
- Frames may contain **hands** with different poses and gestures.

### Output
- **Hand Presence**: "Hand Detected" or "No Hand".
- **Hand Side**: "Left Hand" or "Right Hand".
- **Finger Count**: Number of fingers shown (0–5).
- **Gesture Type**: "Thumbs Up", "Thumbs Down", or "Other".
