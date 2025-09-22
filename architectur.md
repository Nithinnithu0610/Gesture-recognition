# System Architecture Diagram

```mermaid
graph TD

    %% Hardware
    subgraph Hardware
        Camera["📷 Camera
        Input: People showing faces & gestures
        Output: Live video (frames)"]

        Computer["💻 Computer
        Input: Video frames
        Output: Sends to Software"]
    end

    %% Software
    subgraph Software
        OpenCV["🖼️ OpenCV
        Input: Video frames
        Task: Preprocess frames (flip, resize, convert color)
        Output: Ready frames"]

        FaceRecognition["🙂 Face Recognition
        Input: Processed frames + Stored faces
        Task: Detect & recognize faces
        Output: Person's Name / Unknown"]

        GestureRecognition["🤚 Gesture Recognition
        Input: Processed frames
        Task: Detect hand, classify Left/Right, count fingers, recognize gestures
        Output: Hand side, finger count, gesture type"]

        AttendanceManager["📒 Attendance Manager
        Input: Person's Name / Unknown
        Task: Mark attendance for known people
        Output: Attendance record"]

        GestureLogger["📝 Gesture Logger
        Input: Hand info & gesture events
        Task: Record gestures with timestamp
        Output: Gesture logs"]

        Logger["📝 System Logger
        Input: System events & performance
        Task: Record errors,
