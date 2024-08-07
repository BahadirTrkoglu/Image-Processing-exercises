# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:05:51 2024

@author: BahadırTürkoğlu
"""

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#Çizgi çizme
#cv2.line(img,(0,0),(511,511),(255,0,0),5) #şekil çizdik 255 koyu maviyi temsilen sondaki 5 piksel boyutu kalınlık
#cv2.line(img,(50,400),(400,50),(0,0,255),5) # sıeayla bailangiç konumu bitiş konumu renk kodları ve piksel (kalınlık) boyutu
#-------------------------------------------------------------------------------------------------------------------------------

#Dikdörtgen çizme

#cv2.rectangle(img,(50,50),(300,300),(0,255,0),5) #içi boş dikdörgen

#cv2.rectangle(img,(300,300),(511,511),(0,255,0),-1) #içi dolu
#--------------------------------------------------------------------------------------

#Daire çizme
#cv2.circle(img, (255,255), 60, (80,300,200),5) #içi boş

#cv2.circle(img, (100,100), 60, (300,200,100),-1) #içi dolu
#------------------------------------------------------------------------------------------------

#Elips çizme
#cv2.ellipse(img, (256,256),(100,50),0,0,180,(0,300,0),4) #içi boş

#cv2.ellipse(img, (100,100),(100,50),0,0,180,(0,300,0),-1) #içi boş

#-------------------------------------------------------------------------------------------------

#Çokgenler

#pts = np.array ([[20,30],[100,120],[255,255],[10,400]],np.int32) #noktaların kordinatları 
#pts2= pts.reshape(-1,1,2)

#cv2.polylines(img, [pts], True, (255,255,255),3)

#--------------------------------------------------------------------------------------------------

#Yazı yazma

font= cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'openCv', (50,150), font,3, (0,155,255),2,cv2.LINE_AA)


cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

