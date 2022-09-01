import cv2
import numpy as np
import pyautogui


cap = cv2.VideoCapture(0)

blue_lower = np.array([100,150,0],np.uint8)
blue_upper = np.array([140,255,255],np.uint8)


prev_x = 100
prev_y = 100

while True:
    ret, frame = cap.read()
    frame_flip = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame_flip, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_lower, blue_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame_flip, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if (prev_x, prev_y) != (x, y):
                pyautogui._mouseMoveDrag("move",prev_x,prev_y,x,y,duration=0.1)
                prev_x = x
                prev_y = y
                #if test.test() == "Key.shift pressed":
                #    pyautogui.mouseDown(prev_x, prev_y)
                #    prev_x = x
                #    prev_y = y


    cv2.imshow("frame", frame_flip)
    k = cv2.waitKey(1)
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()


'''
k = cv2.waitKey(0)
print(k)
if k == 27:  # close on ESC key
    cv2.destroyAllWindows()
k = cv2.waitKey(0) & 0xFF
    print(k)
    if k == 27:
        cv2.destroyAllWindows()
        break
'''