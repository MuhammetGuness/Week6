#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np

image = cv2.imread("pythondeneme.png")
kernel1 = np.ones((5,5), np.float32)/30
img = cv2.filter2D(src = image, ddepth = -1, kernel = kernel1)
cv2.imshow('Orjinal',image)
cv2.imshow('Kernel Blur',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




