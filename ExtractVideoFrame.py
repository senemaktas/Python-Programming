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
