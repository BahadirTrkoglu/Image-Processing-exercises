# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:35:18 2024

@author: Bahadır Türkoğlu
"""
import cv2
#import Tresh
import matplotlib.pyplot as plt #herbirisi için ayrı pencereler açmamak için kullandık


resim = cv2.imread("gradient.jpg",0)

_, resim_thresh1 = cv2.threshold(resim, 182, 255, cv2.THRESH_BINARY) # eşik değer 182 olarak belirledik , 182 üstündeki değerleri 255 e eşitler
_, resim_thresh2 = cv2.threshold(resim, 182, 255, cv2.THRESH_BINARY_INV)
_, resim_thresh3 = cv2.threshold(resim, 182, 255, cv2.THRESH_TRUNC)
_, resim_thresh5 = cv2.threshold(resim, 182, 255, cv2.THRESH_TOZERO_INV)
_, resim_thresh4 = cv2.threshold(resim, 182, 255, cv2.THRESH_TOZERO)

#ret2, resim_thresh2  = Tresh.threshold(resim, 182, 255)

resimler = [resim,resim_thresh1,resim_thresh2,resim_thresh3,resim_thresh4,resim_thresh5]

basliklar = ["original resim ","binary","binary_inv","trunc","to_zero","to_zero_inv"]

for i in range(6):
  plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray"),plt.title(basliklar[i])

plt.show()
#cv2.imshow("resim",resim)
#cv2.imshow("thresh", resim_thresh1)
##cv2.imshow("thresh2", resim_thresh2)
#cv2.waitKey()
#cv2.destroyAllWindows()
