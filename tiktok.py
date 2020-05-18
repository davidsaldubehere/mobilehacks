from pyautogui import scroll
from time import sleep

delay = .5
viewCount = 500
#starts the scrolling which gives double the amount of views
#specified in viewCount
def beginScrolling():
    for i in range(viewCount):
        sleep(delay)
        scroll(1)
        sleep(delay)
        scroll(-1)
sleep(5)
beginScrolling()