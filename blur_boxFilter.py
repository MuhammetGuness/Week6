#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

image = cv2.imread("pythondeneme.png")
img1 = cv2.blur(image,(5,5))
img2 = cv2.boxFilter(image,-1,(2,2), normalize=True)
cv2.imshow("Fotolar",np.hstack((img1,img2)))

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

