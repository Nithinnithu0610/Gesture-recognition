# System Architecture Diagram

```mermaid
flowchart TD
    Camera[Camera Input] --> Preprocess[Frame Preprocessing]

    Preprocess --> FaceRecognition[Face Recognition Module]
    Preprocess --> GestureRecognition[Gesture Recognition Module]

    FaceRecognition --> Encoder[Face Encoding]
    Encoder --> AttendanceCheck[Attendance Manager]
    AttendanceCheck --> CSV[(Attendance.csv)]
    AttendanceCheck --> LogFile[(performance.log)]

    GestureRecognition --> HandSide[Hand Side Detection]
    GestureRecognition --> FingerCount[Finger Counting]
    GestureRecognition --> GestureType[Gesture Recognition]

    HandSide --> GestureLogger[Logger]
    FingerCount --> GestureLogger
    GestureType --> GestureLogger
    GestureLogger --> GestureLogFile[(gesture.log)]

    CSV --> Teacher[Teacher/Admin View]
    LogFile --> Developer[Developer]
    GestureLogFile --> Developer[Developer]
```
