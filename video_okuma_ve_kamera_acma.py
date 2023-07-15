import time
import cv2
import mediapipe as mp

def video_capture(bfr):
    capture = cv2.VideoCapture(bfr)

    while True:
        kontrol,frame = capture.read()
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord("q"): # q ile çıkış yapıyor
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    bfr = 0
    # bfr =  "data/ornek.mp4"
    video_capture(bfr)

