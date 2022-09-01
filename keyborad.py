from pynput.keyboard import Listener
import pyautogui

p1 = True

def on_press(key):
    def p():
        print(str(key) + " is pressed")
        if (str(key)) == "'a'":
            print(pyautogui.position())
        elif p1 == True:
            print("#")

    p()

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()


if pyautogui.mouseDown():
    pass
elif pyautogui.mouseUp():
    pyautogui.mouseDown()