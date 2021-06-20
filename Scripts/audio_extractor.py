import moviepy.editor as mp

audio_path = 'D:/Test/Results/audio.mp3'
video_path = 'D:/Test/Results/2.mp4'

clip = mp.VideoFileClip(video_path)

clip.audio.write_audiofile(audio_path)
print("SUCCESS")
