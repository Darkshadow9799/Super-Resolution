from ISR.models import RDN, RRDN
import cv2
import os 
from PIL import Image
import numpy as np

''' -----------------------------------------------------------------------------------'''
 
model = RRDN(weights='gans')

''' -----------------------------------------------------------------------------------'''

video_path = 'Results/2.mp4'
data_path = 'Test/data'
data_clean_path = 'data_clean'

''' -----------------------------------------------------------------------------------'''

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
         name = data_path+ '/frame' + str(currentframe) + '.png'
         cv2.imwrite(name, f)
         currentframe += 1
    else:
         break
cam.release()
cv2.destroyAllWindows()

''' -----------------------------------------------------------------------------------'''

try:
    if not os.path.exists(data_clean_path):
        os.makedirs(data_clean_path)
except OSError:
    print('Error')

count = 0

for img in os.listdir(data_path):
  print('COUNT: ', count)
  img = Image.open(os.path.join(data_path, img))
  img = img.resize((480, 270))
  sr_img = model.predict(np.array(img))
  sr_img = Image.fromarray(sr_img)
  sr_img.save(data_clean_path + '/' + str(count) + '.png')
  count += 1
  if count > 200:
    break

