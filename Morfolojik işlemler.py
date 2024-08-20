
import cv2
import numpy as np
import matplotlib.pyplot as plt
resim = cv2.imread("opening.png",0)

#_,resim = cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #gri resmi siyah beyaz hale getirdik

kernel = np.ones((7,7),np.uint8) # 5 ler aşındırdığı veya çoğalttığı seviye
#kernel_rectangular = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) #yukarıdaki kernel ile aynı ancak farklı şekillerde kernel oluşturmamıza olanak sağlar elips gibi
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE(5,5)) #elips kernel oluşturur



erosion  = cv2.erode(resim, kernel,iterations=1) #iterations işlemin kaç kez tekrar edeceğini belirler
dilation = cv2.dilate(resim,kernel,iterations=1)
opening  = cv2.morphologyEx(resim,cv2.MORPH_OPEN,kernel) # önce erosin işlemi yapar ardından bu resme dilation işlemi uygular amaç gürültüden kurtulmaktır
closing  =cv2.morphologyEx(resim,cv2.MORPH_CLOSE,kernel) #içerideki gürültüleri engellemek istiyorsak closing, dışardaki gürültüleri engellemek istiyorsak opening
tophat = cv2.morphologyEx(resim, cv2.MORPH_TOPHAT, kernel) #orjinal resim ile opening in farkını alır
blackhat = cv2.morphologyEx(resim, cv2.MORPH_BLACKHAT, kernel) #orjinal resim ile closing in farkını alır
gradient = cv2.morphologyEx(resim, cv2.MORPH_GRADIENT, kernel) # erosion ve dilation işlemlerinin farkını alır


plt.subplot(241),plt.imshow(resim,"gray"),plt.title("orijinal") #241 2X4 LÜK MATRİSİN 1. Sİ OLDUĞUNU İFADE EDER
plt.subplot(242),plt.imshow(erosion,"gray"),plt.title("erosion")
plt.subplot(243),plt.imshow(dilation,"gray"),plt.title("dilation")
plt.subplot(244),plt.imshow(opening,"gray"),plt.title("opening")
plt.subplot(245),plt.imshow(closing,"gray"),plt.title("closing")
plt.subplot(245),plt.imshow(tophat,"gray"),plt.title("tophat")
plt.subplot(245),plt.imshow(blackhat,"gray"),plt.title("blackhat")
plt.subplot(245),plt.imshow(gradient,"gray"),plt.title("gradient")


plt.show()