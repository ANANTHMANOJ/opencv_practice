# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:57:13 2019

@author: AmNayak
"""

import cv2
import numpy as np
from matplotlib import pyplot as pt




inputi=cv2.imread(r"C:\Users\AmNayak\Desktop\PassportPhoto.jpg")
h,w=inputi.shape[:2]
qh,qw=h/4,w/4
#transition_matrix=np.float32([[1,0,qw],[0,1,qh]])
#rotation_matrix=cv2.getRotationMatrix2D((w/2,h/2),45,.75)
#img_trans=cv2.warpAffine(inputi,rotation_matrix,(w,h))

#
#in_scale=cv2.resize(inputi,None,fx=.25,fy=.25)
#in_scale1=cv2.resize(inputi,(900,400),interpolation=cv2.INTER_LANCZOS4)
##cv2.imshow("transition",in_scale1)

#small=cv2.pyrDown(inputi)
#large=cv2.pyrUp(small) 
#cv2.imshow("small",small)
#cv2.imshow("large",large)



cv2.waitKey()
cv2.destroyAllWindows()

#img=np.zeros([500,500,3],np.uint8)
#cv2.line(img,(0,0),(0,256),(255,127,0),10)
#cv2.putText(img,"Ananthmanoj",(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,5,(255,100,90),100)
#cv2.imshow("img",img)

#inputi=cv2.imread(r"C:\Users\AmNayak\Desktop\Aadhar.jpg")
##cv2.imshow("aadhar",inputi)
#color=('b','g','r')
#
#
#for i,col in enumerate(color):
#    histo=cv2.calcHist([inputi],[i],None,[256],[0,256])
#    #pt.hist(inputi.ravel(),256,[0,256])
#    pt.plot(histo,color=col)
#    pt.xlim([0,256])
#    print(col) 
#pt.show()
#print(str(inputi.raval()))
#gray=cv2.cvtColor(inputi,cv2.COLOR_BGR2GRAY)
#cv2.imshow('AMN',gray)
#
#print(inputi.shape)
#cv2.imwrite('AMN.png',inputi)
#
#b,g,r=inputi[255,55]
#print(b,g,r)
#
#hsv_image=cv2.cvtColor(inputi,cv2.COLOR_BGR2HSV)
#cv2.imshow('hsv_normal',hsv_image)
#cv2.imshow('hsv_hue',hsv_image[:,:,0])
#cv2.imshow('hsv_sat',hsv_image[:,:,1])
#cv2.imshow('hsv_val',hsv_image[:,:,2])
#
#b,g,r=cv2.split(inputi)
#cv2.imshow('red',r)
#cv2.imshow('green',g)
#cv2.imshow('blue',b)


cv2.waitKey()
cv2.destroyAllWindows()