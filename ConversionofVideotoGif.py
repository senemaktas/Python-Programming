# https://www.codespeedy.com/conversion-of-video-to-gif-using-python/

from moviepy.editor import *

clip = (VideoFileClip("/home/sidney/Desktop/yazi/attention_process.mp4"))
clip.write_gif("/home/sidney/Desktop/yazi/attention_process.gif")