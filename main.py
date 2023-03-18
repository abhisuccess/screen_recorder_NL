import cv2
from win32api import GetSystemMetrics
import numpy as np
import time
import pyautogui

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
dim=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("test3.mp4",f,30.0,dim)
s_t=time.time()
dur=10+4
e_t=s_t+dur

while True:
    img=pyautogui.screenshot()
    f1=np.array(img)
    clr=cv2.cvtColor(f1,cv2.COLOR_BGR2RGB)
    output.write(clr)
    n_t=time.time()
    if n_t > e_t:
        break
output.release()
print("ok")
