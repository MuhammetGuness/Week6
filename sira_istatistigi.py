#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

image = cv2.imread("pythondeneme.png")
median = cv2.medianBlur(image, 5)
compare = cv2.concatenate((image, median), axis=1)
cv2.imshow('Image',compare)

cv2.waitKey(0)
cv2.destroyAllWindows()

