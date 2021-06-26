import cv2
import os 
from PIL import Image
import numpy as np
import glob
from tqdm import tqdm
import moviepy.video.io.ImageSequenceClip

def gen_image(video_path, data_path):
    try:
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
        print("Generate Image Success")
    except:
        print("Generate Image Failure")

def predict_gen_image(model, data_path, data_clean_path):
    try:
        if not os.path.exists(data_clean_path):
            os.makedirs(data_clean_path)
    except OSError:
        print('Error')
    try:    
        counter = len(glob.glob1(data_path,"*.png"))
        count = 0
        # print("STARTED")
        # for img in os.listdir('D:/Test/data'):
        for _ in tqdm(range(counter)):
            #print('COUNT: ', count)
            img = Image.open(data_path + '/frame'+ str(count) + '.png')
            img = img.resize((480, 270))
            sr_img = model.predict(np.array(img), by_patch_of_size=50)
            sr_img = Image.fromarray(sr_img)
            sr_img.save(data_clean_path + '/' + str(count) + '.png')
            count += 1
            # if count > 200:
                # break
        print("Predict Generated Images Success")
    except:
        print("Predict Generated Images Failure")

def video_result(data_clean_path, result_video_path):
    try:
        fps=30
        counter = len(glob.glob1(data_clean_path,"*.png"))
        print(counter)
        #image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
        image_files = []
        count = 0
        for _ in tqdm(range(counter)):
            img = Image.open(data_clean_path + '/' + str(count) + '.png')
            image_files.append(np.array(img))
            count += 1
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
        clip.write_videofile(result_video_path)
        print("Video Result Success")
    except:
        print("Video Result_Failure")