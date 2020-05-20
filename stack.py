#Used for the stack Ketchapp app.
from pyautogui import click
from time import sleep
#Waits 3 seconds before beginning
sleep(3)
delay=.7
for i in range(100):
    click()
    sleep(delay)