# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 13:58:48 2024

@author: Bahadır Türkoğlu
"""

import cv2
import matplotlib.pyplot as plt 

resim = cv2.imread("r.jpg")

kirp = resim[100:300,100:300]


resim[100:300,400:600] = kirp

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.imshow()