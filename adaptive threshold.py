# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:09:20 2024

@author: Bahadır Türkoğlu
"""
#Adaptif Treshold
import cv2
import matplotlib.pyplot as plt


resim = cv2.imread("sudoku.jpeg",0)


thresh = cv2.adaptiveThreshold(resim, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                    cv2.THRESH_BINARY, 33, 4) #33 matris boyutu


thresh2 = cv2.adaptiveThreshold(resim, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY, 33, 4)


cv2.imshow("adaptive mean", resim)
cv2.imshow("adaptive gaussian", thresh)

cv2.waitKey()
cv2.destroyAllWindows()
