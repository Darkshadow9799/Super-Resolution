from moviepy.editor import *

audio_path = 'Results/audio.mp3'
created_video_path = 'Results/my_video.mp4'
final_video = 'Results/my_video2.mp4'
clip = VideoFileClip(created_video_path)
audio_file = AudioFileClip(audio_path)

final_clip = clip.set_audio(audio_file)
final_clip.write_videofile(final_video)
print("SUCCESS")
