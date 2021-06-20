import numpy as np
from PIL import Image
import os
import glob
from tqdm import tqdm
from ISR.models import RDN, RRDN
 
''' ============================================================================ '''
#model = RRDN(weights='gans')
model = RDN(weights='psnr-small')

data_path = 'D:/Test/data'
data_clean_path = 'D:/Test/data_clean'

''' ============================================================================ '''

try:
    if not os.path.exists(data_clean_path):
        os.makedirs(data_clean_path)
except OSError:
    print('Error')

''' ============================================================================ '''
counter = len(glob.glob1(data_path,"*.png"))
#count = 0
#for img in os.listdir('D:/Test/data'):
for _ in tqdm(range(counter)):
  #print('COUNT: ', count)
  img = Image.open(data_path + '/frame'+ str(count) + '.png')
  img = img.resize((480, 270))
  #sr_img = model.predict(np.array(img), by_patch_of_size=50)
  sr_img = model.predict(np.array(img))
  sr_img = Image.fromarray(sr_img)
  sr_img.save(data_clean_path + '/' + str(count) + '.png')
  '''
  count += 1
  if count > 200:
    break
  '''

