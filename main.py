'''
Steps:

1. Seperate audio and video.
2. Process video and create images.
3. Take images and predict.
4. Take predicted images and create the video.
5. Add audio to video.

1. Seperate audio and video:
    -> File name: audio_functions.py.
    -> Function: extraction
    -> Inputs required: 
        a. audio_path (Path where audio is to be saved)
        b. video_path (Path where video is present)

2. Process video and create images.
    -> File name: video_functions.py.
    -> Function: gen_images
    -> Inputs required: 
        a. video_path (Path where video is present)
        b. data_path (Path to save the images/frames)

3. Take images and predict.
    -> File name: video_functions.py.
    -> Function: predict_gen_images
    -> Inputs required:
        a. data_path (Path to save the images/frames)
        b. data_clean_path (Path to save the predicted images/frames)

4. Take predicted images and create the video.
    -> File name: video_functions.py.
    -> Function: video_result
    -> Inputs required:
        a. data_clean_path or image_path (Path to save the predicted images/frames)
        b. result_video_path

5. Add audio to video.
    -> File name: audio_function.py
    -> Function: merger
    -> Inputs required:
        a. audio_path
        b. result_video_path
        c. final_video_path
    
'''

from ISR.models import RDN, RRDN
from modules import audio_functions, video_functions
# All path files input:
video_path = './Results/1.mp4' # input()
final_video_path = './Results/final.mp4' # input()
audio_path = './Results/extrated_audio.mp3'
data_path = './data3'
data_clean_path = './data_clean3'
result_video_path = './Results/video.mp4'

model = RDN(weights='psnr-small')
audio_functions.extraction(audio_path, video_path)
video_functions.gen_image(video_path, data_path)
video_functions.predict_gen_image(model, data_path, data_clean_path)
video_functions.video_result(data_clean_path, result_video_path)
audio_functions.merger(audio_path, result_video_path, final_video_path)