import cv2
import time

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
resolution = "{}x{}".format(width, height)
print("Resolution:", resolution)

frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()

    cv2.imshow('Webcam Tester', frame)

    frame_count += 1

    elapsed_time = time.time() - start_time

    if elapsed_time >= 1.0:
        fps = frame_count / elapsed_time
        print("FPS:","{:.2f}".format(fps)+ ", Resolution:", resolution)
        frame_count = 0
        start_time = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
