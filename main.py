from cv2 import CAP_PROP_FPS, VideoCapture, imshow, waitKey, destroyAllWindows
from time import sleep

cap = VideoCapture('trolol.mp4')
assert cap.isOpened()

wait = int(1/cap.get(CAP_PROP_FPS)*1000)


read, frame = cap.read()
while read:
    imshow('Frame', frame)
    read, frame = cap.read()
    if waitKey(wait) & 0xFF == ord('q'):
        break