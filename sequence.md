# Sequence Flow

1. Start webcam and capture frame
2. Preprocess frame (flip, convert color)
3. Face Recognition path:
   - Detect faces
   - Encode and compare
   - Update attendance.csv
4. Gesture Recognition path:
   - Detect hands using MediaPipe
   - Determine handedness
   - Count fingers
   - Recognize thumbs up / thumbs down
5. Overlay face + gesture info on frame
6. Display frame
7. Loop until user exits (press 'q')
