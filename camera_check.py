
# coding: utf-8

# In[1]:

import cv2
import numpy
import time


# In[66]:

def checkCams():
    '''enumerate the connected and readable video devices'''
    cameraList = []
    for i in range(0, 10):
        try:
            connected, _ = cv2.VideoCapture(i).read()
        except Excpetion, e:
            print 'video device', i, 'not avaialble - this is OK!'
        cv2.VideoCapture(i).release()
        if connected:
            cameraList.append(i)
    return cameraList

#cams = checkCams()
#print 'found camera devices at:', cams

cap = cv2.VideoCapture(1)

cap.set(3, 960)
cap.set(4, 544)
cap.set(5, 60)

for i in range(0, 200):
    
    _, frame = cap.read()
    cv2.imshow('foo' , frame)
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)


# 640x480
# 
# 

# In[24]:

help(cap.get)


# In[2]:

cap = cv2.VideoCapture(0)


# In[4]:

cap.set(3, 640)
cap.set(4, 480)
cap.set(5, 15)
_, frame = cap.read()
cv2.imshow('foo', frame)
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
for i in range(3, 30):
    print i, '=', cap.get(i)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



