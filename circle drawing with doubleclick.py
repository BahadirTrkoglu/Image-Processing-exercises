# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:02:05 2024

@author: Bahadır Türkoğlu
"""
import cv2

import numpy as np



def draw(event,x ,y ,flags, param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
         cv2.circle(img, (x,y), 50, (255,0,0),-1)
    
    
    
    
    
    
img = np.ones((512,512,3),np.uint8)

cv2.namedWindow("paint")

cv2.setMouseCallback("paint", draw)


while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cv2.destroyAllWindows()    