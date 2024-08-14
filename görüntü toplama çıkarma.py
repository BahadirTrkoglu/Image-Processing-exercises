# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:42:58 2024

@author: Bahadır Türkoğlu
"""

import cv2

import numpy as np


#x = np.uint8([250])

#y = np.uint8([10])


#sonuc1 = x+y # 8 bit olduğu için 256 ile mod (%) alma işlemi yapıyor

#sonuc2 = cv2.add(x,y) # max değer 255 olduğu için 255 değerini verir

#------------------------------------------------------------------------
#img1 = cv2.imread("cv2.png")
#img2 = cv2.imread("d.jpg")

#toplam = cv2.addWeighted(img1, 0.3, img2, 0.7, 0) #ilk resim(kaynak) , yüzde ne kadar kullanılacağı, ikinci resim(kaynak) , birincinin ikincinni yüzde ne kadar kullanılacağı, alfa değeri

#cv2.imshow("resim1",toplam)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#--------------------------------------------------------------------------
#Bitsel işlemler

img3 = cv2.imread("cv2.png")
img4 = cv2.imread("r - Kopya.jpg")

x,y,z = img3.shape #img3 ün büyüklük değerlerini x y z ye eşitledik
roi = img4[0:x,0:y] #sıfırdan başlasın ve img3 ün büyüklüğü kadar kırpsın

img3_gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY) #renk tonlamalarını değiştiren fonksiyon
ret, mask = cv2.threshold(img3_gray, 10, 255, cv2.THRESH_BINARY) # eşikleme işlemi 10 pikselin üstünü alsın beyaz yapsın gerisi beyaz olsun


mask_inv =cv2.bitwise_not(mask) #tersleme işlemi


img3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #ÖNEMLİ ! fonksiyon özelliği gereği ilk iki çarpıldığı için binary andlemade yanlış sonuç almamak için kendisini kendisiyle andliyoruz daha sonra mask ın üzerine ekliyoruz

img4_fg = cv2.bitwise_and(img3,img3,mask=mask)

toplam = cv2.add(img3_bg,img4_fg)


img4[0:x,0:y] = toplam # küçük resimde çalıştık ve işimiz bitince tekrardan kırptığımız resmi büyük resme ekledik


cv2.namedWindow("resim", cv2.WINDOW_NORMAL) #pencerenin boyutlarını değitirebilmemize yarar
cv2.imshow("resim", img4)
cv2.imshow("resim2", toplam )
cv2.waitKey(0)
cv2.destroyAllWindows()

