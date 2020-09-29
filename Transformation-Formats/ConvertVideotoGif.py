# https://www.codespeedy.com/conversion-of-video-to-gif-using-python/

from moviepy.editor import *

clip = (VideoFileClip("/home/..../video.mp4"))
clip.write_gif("/home/..../video.gif")
