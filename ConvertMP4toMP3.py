# Extract mp3 files from an mp4 video
# 1- install : pip/pip3 install pydub  2- install : sudo apt install ffmpeg

''' AudioSegment is the container to load, transform, and save audio files.
Python’s pydub module lets you to audio processing tasks that range from video 
conversion to straight out mixing different files. '''
from pydub import AudioSegment

AudioSegment.from_file("/home/.../inputVideo.mp4").export("/home/.../output.mp3", format="mp3")
