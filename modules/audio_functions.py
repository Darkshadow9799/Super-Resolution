import moviepy.editor as mp


def extraction(audio_path, video_path):
    try:
        clip = mp.VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path)
        print("Audio Extraction Success")
    except:
        print("Audio Extraction Failure")

def merger(audio_path, result_video_path, final_video_path):
    try:
        clip = mp.VideoFileClip(result_video_path)
        audio_file = mp.AudioFileClip(audio_path)

        final_clip = clip.set_audio(audio_file)
        final_clip.write_videofile(final_video_path)
        print("Audio Merging Success")
    except:
        print("Audio Merging Failure")
