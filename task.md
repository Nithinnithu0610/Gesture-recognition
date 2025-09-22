# Interview Assessment – Tasks

## Task 3 – Extend Attendance Repo with Gesture Recognition

### Objective
Enhance the existing Face Recognition Attendance System by adding **Hand Gesture Detection** features.

### Features Implemented
- Detect presence of hand in camera feed  
- Identify Left Hand or Right Hand  
- Count number of fingers extended  
- Recognize gestures: 👍 Thumbs Up, 👎 Thumbs Down  

### Dependencies
- mediapipe
- opencv-python

### How to Run
```bash
pip install mediapipe opencv-python
python execute.py
```

### Output
- Face recognition + attendance logging (as before)  
- Overlay of hand type, finger count, and recognized gesture  
- Press `q` to exit  
