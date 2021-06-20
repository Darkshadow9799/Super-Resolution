import os
import moviepy.video.io.ImageSequenceClip
from PIL import Image
import numpy as np
from tqdm import tqdm
import glob

image_folder='D:/Test/data_clean'
#data_clean_path = 'D:/Test/data_clean'

fps=30
counter = len(glob.glob1(image_folder,"*.png"))
#image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
image_files = []
count = 0
for _ in tqdm(range(counter)):
  img = Image.open(image_folder + '/' + str(count) + '.png')
  image_files.append(np.array(img))
  count += 1
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('Results/my_video.mp4')