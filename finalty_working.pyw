from threading import *
import cv2
import numpy as np
import pyautogui
from pynput import keyboard



class Camera_capture(Thread):
    def run(self):
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
                if area > 50:
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame_flip, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    
                    if (prev_x, prev_y) != (x, y):
                        pyautogui._mouseMoveDrag("move",prev_x,prev_y,x,y,duration=0.000001)
                        prev_x = x
                        prev_y = y
                
                
            cv2.imshow('frame',frame_flip)

            k = cv2.waitKey(1)
            if k == 27:
                break


        cap.release()
        cv2.destroyAllWindows()


class Keyboard_detection(Thread):
    def run(self):
        

        def on_press(key):
            if str(key) == "'x'":
                    pyautogui.mouseDown(_pause=None)


        def on_release(key):
            if str(key) == "'x'":
                pyautogui.mouseUp(_pause=None)



        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

t1 = Camera_capture()
t2 = Keyboard_detection()

if __name__ == "__main__":
    t1.start()
    t2.start()
