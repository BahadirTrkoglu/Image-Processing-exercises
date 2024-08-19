# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:40:38 2024

@author: Bahadır Türkoğlu
"""
import cv2
import numpy as np


img = cv2.imread("1.jpeg")

print(img.shape)
#--------------------------------------------------------
#görüntü yeniden boyutlandırma
#res = cv2.resize(img, (300,300)) #yeniden boyutlandırdık

#res  = cv2.resize(img, None,fx=1.4,fy=1) #farklı şekilde yenideen boyutlandırdı x i 1.4 le çarptı y yi 1 le



#cv2.imshow("img",img)
#cv2.imshow("res",res)
#---------------------------------------------------
#yer değişrtirme
#row,cols = img.shape[:2]

#translation_matrix = np.float32([
#    [1,0,50], #x ekseninde öteler
#    [0,1,40]  #y ekseninde öteler        #50 piksel sağa ve 50 piksel aşağı öteledik
#    ])
#img_translation = cv2.warpAffine(img, translation_matrix, (cols+50,row+50)) #resmin kendi görüntüs bozumasın diye 50 ekledik
#
#cv2.imshow("img",img)
#cv2.imshow("img_translations",img_translation)
#---------------------------------------------------------
#Resim döndürme
#row,cols = img.shape[:2]
#rotation_matrix = cv2.getRotationMatrix2D((cols/2,row/2), 30, 0.8) #cols ve row u 2 ye bölerek merkezini almış olduk , 30 derece döndürdük,resmi %20 küçültmüş olduk

#img_rotation = cv2.warpAffine(img, rotation_matrix, (int(cols*1.3),int(row*1.3))) #x ve y boyutlarını %130 arttırmış oldu

#cv2.imshow("img",img)
#cv2.imshow("img_rotation",img_rotation)
#-----------------------------------------------------------
#ölçeklendirme
row,cols = img.shape[:2]
#src_points =np.float32([
#    [0,0],
#    [cols-1,0],
#    [0,row-1],
#    
#    ]) #resmimizin üzerinden matrixle 3 piksel seçiyoruz
#
#dst_points = np.float32([
#
#    [0,0],
#    [int(0.6*(cols-1)),0], #src deki bu noktayı %60 sola aldık
#    [int(0.4*(row-1)),row-1], # src deki bu noktayı  %40 sağa kaydırdık x i
# 
#    ]) # yeni resimdenerede olmasını seçtiğmiz piksellerin konumunu tanımlayan matrixler
#
#affine_matrix = cv2.getAffineTransform(src_points, dst_points)
#
#img_output = cv2.warpAffine(img,affine_matrix,(cols,row))

#Farklı Bir yöntem #4 nokta seçimi yaptırdığı için daha kullanışlı

src_points = np.float32([
   
    [80,100], 
    [400,90],
    [50,400], #
    [400,400] #
    ])
dst_points =np.float32([
   
    [0,0], 
    [cols-1,0],
    [0,row-1], #
    [cols-1,row-1] #
    ])

prjective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

img_output = cv2.warpPerspective(img, prjective_matrix, (cols,row))


cv2.imshow("img",img)
cv2.imshow("img_output",img_output)

cv2.waitKey()
cv2.destroyAllWindows()