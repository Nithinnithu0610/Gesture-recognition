import cv2
from gesture_recognition import process_frame

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        # Face Recognition block would go here (existing system)
        # ...

        # Gesture Recognition block
        frame, detections = process_frame(frame)
        y_pos = 30
        for label, fingers, gesture in detections:
            cv2.putText(frame, f"{label} Hand", (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            y_pos += 40
            cv2.putText(frame, f"Fingers: {fingers}", (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            y_pos += 40
            if gesture:
                cv2.putText(frame, f"{gesture}", (10, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                y_pos += 40

        cv2.imshow("Face + Gesture Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
