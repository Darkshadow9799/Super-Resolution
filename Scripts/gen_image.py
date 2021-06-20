import cv2
import os 
from PIL import Image
import numpy as np
 
video_path = 'Results/2.mp4'
data_path = 'data'
 
cam = cv2.VideoCapture(video_path)
try:
    if not os.path.exists(data_path):
        os.makedirs(data_path)
except OSError:
    print('Error')
 
currentframe = 0
while(True):
    ret, f = cam.read()
    if ret:
         name =data_path + '/frame' + str(currentframe) + '.png'
         cv2.imwrite(name, f)
         currentframe += 1
         #print('COUNT: ', currentframe)
    else:
         break
cam.release()
cv2.destroyAllWindows()
