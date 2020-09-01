# pip/pip3 install opencv-python

import cv2
import math
import matplotlib.pyplot as plt 
import pandas as ps
import numpy as np

count=0
videofile="/home/..../VideoName.mp4"
cap=cv2.VideoCapture(videofile)
frameRate=cap.get(5)
x=1
while(cap.isOpened()):
    frameId=cap.get(1)
    ret,frame=cap.read()
    if(ret != True):
        break
    if(frameId%math.floor(frameRate)==0):
        filename="/home/...../frame%d.jpg" % count;count+=1
        cv2.imwrite(filename,frame)
cap.release()
print("Done!")

# Second way to do that  ------------------------------------------------------

import cv2
videocap = cv2.VideoCapture('input.mp4')
success,image = videocap.read()
count = 0 

while success:
  cv2.imwrite("frame%d.jpg" % count, image)
  success,image = videocap.read()
  print('Read a new frame: ', success)
  count += 1

# This would capture only one frame per second.
videocap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
