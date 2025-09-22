import cv2
import time
from gesture_recognition import process_frame

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError('Could not open webcam.')
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            # Placeholder: merge your face recognition code here
            cv2.putText(frame, 'FaceRecognition: merge your code here', (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,0),1)

            try:
                frame, detections = process_frame(frame)
            except Exception as e:
                detections = []
                cv2.putText(frame, 'Gesture module error: ' + str(e), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),1)

            y = 60
            for label, fingers, gesture in detections:
                cv2.putText(frame, f"{label} Hand", (10,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2); y += 25
                cv2.putText(frame, f"Fingers: {fingers}", (10,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2); y += 25
                if gesture:
                    cv2.putText(frame, f"{gesture}", (10,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2); y += 30

            cv2.imshow('Face + Gesture Recognition', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
