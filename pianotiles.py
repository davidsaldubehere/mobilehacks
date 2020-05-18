from PIL import ImageOps 
import pyautogui 
import time 
import numpy as np  
time.sleep(3)
baseHeight = 235

corner1 = 472
corner2 = 581
corner3 = 694
corner4 = 809
points = [corner1, corner2, corner3, corner4]
def getCoordinates():
    for i in points:
        currentPoint = ImageOps.grayscale(pyautogui.screenshot('test.png', region=(i, baseHeight, 1, 1)))
        if np.array(currentPoint).sum() < 10:
            pyautogui.click(i, baseHeight)
        else:
            print('no')
for i in range(100):
    getCoordinates()