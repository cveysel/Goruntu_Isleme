import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while (True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    kirmizi_alt = np.array([0,150,0])
    kirmizi_ust = np.array([20,255,255])
    sb_goruntu = cv2.inRange(frame,kirmizi_alt, kirmizi_ust)
    kare_rgb = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    kirmizi = cv2.bitwise_and(frame,frame, mask =sb_goruntu)

    cv2.imshow("kirmiziyi_beyaza",sb_goruntu)
    cv2.imshow("sadece_kirmizi",kirmizi)

    if cv2.waitKey(1) == ord('q'):
        break