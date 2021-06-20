import moviepy.editor as mp

audio_path = 'Results/audio.mp3'
video_path = 'Results/2.mp4'

clip = mp.VideoFileClip(video_path)

clip.audio.write_audiofile(audio_path)
print("SUCCESS")
