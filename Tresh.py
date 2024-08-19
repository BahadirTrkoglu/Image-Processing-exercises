# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:54:41 2024

@author: Bahadır Türkoğlu
"""

"""
    Bu fonksiyon ile basit eşikleme işlemi yapılabilir
    src = image
    thresh = 0...255
    maxval = 0..255

"""   

def  threshold(src,thresh,maxval):

    img = src.copy()
    rows, cols = img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if img[i,j] < thresh:
                img[i,j] = 0
            else:
                img[i,j] =maxval
    return thresh, img              