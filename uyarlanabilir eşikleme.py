# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:15:12 2024

@author: Bahadır Türkoğlu
"""

import cv2
import matplotlib.pyplot as plt


resim = cv2.imread("shape_noise.png",0)

# global thresholding
_, th1 = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY)

#Otsu's  thresholding
_, th2 = cv2.threshold(resim, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU) #eşik değeri kendisi seçsin istiyoruz

#Otsu's thresholding after Gaussian filtering
blur =  cv2.GaussianBlur(resim, (15, 15),0) #blurlaştırma görüntüyü gürültüden arındırır
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU) #eşik değeri kendisi seçsin istiyoruz

#gürültülü görsellerde etkin çalışmıyor
#print(ret) #eşik değer olarak hangi değeri aldığını yazdırıyorıuz #_ yerine ret değişkeni kullandığımızda

plt.subplot(3,3,1),plt.imshow(resim,"gray"),plt.title("orijinal resim")
plt.subplot(3,3,2),plt.hist(resim.ravel(),256),plt.title("histogram") #histogramını gösteriyor
plt.subplot(3,3,3),plt.imshow(th1,"gray"),plt.title(" th1")
plt.subplot(3,3,4),plt.imshow(resim,"gray"),plt.title("orijinal resim")
plt.subplot(3,3,5),plt.hist(resim.ravel(),256),plt.title("histogram")
plt.subplot(3,3,6),plt.imshow(th2,"gray"),plt.title(" th2")
plt.subplot(3,3,7),plt.imshow(blur,"gray"),plt.title(" blur")
plt.subplot(3,3,8),plt.hist(blur.ravel(),256),plt.title(" histogram")
plt.subplot(3,3,9),plt.imshow(th3,"gray"),plt.title(" th3")


plt.show()