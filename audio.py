import moviepy.editor #pip install moviepy

video = moviepy.editor.VideoFileClip("channel-intro.mp4")

audio = video.audio

audio.write_audiofile("channel-intro.mp3")