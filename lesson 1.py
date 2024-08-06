# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:33:18 2024

@author: Bahadır Türkoğlu
"""

import cv2
from matplotlib import pyplot as plt



resim = cv2.imread("Kizkulesi.jpg",0)#eklenen sıfır siyah beyaz yapar

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

cv2.imshow("resim",resim)



cv2.imshow("Resim Penceresi",resim)


plt.imshow(resim,cmap="gray")
plt.show()

k = cv2.waitKey(0)

if k ==27:
    print("Esc tuşuna basıldı")
    
elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi.") 
    cv2.imwrite("kizkulesigri.jpg", resim)




cv2.destroyWindow("Resim Penceresi")