from moviepy.editor import VideoFileClip
from tkinter.filedialog import *
import os

# Accept only .mov and .mp4 files. Feel free to change.
accepted_files = [("Mov files", "*.mov"), ("MP4 files", "*.mp4")]

# Select a video which is one of the accepted file types from your machine
video_file = askopenfilename(filetypes=accepted_files)

# Create a video clip instance
clip = VideoFileClip(video_file)

# Get the video file name. E.g. 'path/to/video.mov' --> 'video.mov'
video_file_name = os.path.basename(video_file)

# Split video name to parts. E.g. 'video.mov' --> ('video', 'mov')
parts = os.path.splitext(video_file_name)

# Get the name of the video from the parts and add a .gif to the end.
gif_name = parts[0] + ".gif"

# Create a gif with the same name as the original video.
clip.write_gif(gif_name, fps=30)


INPUT_MOV_FILENAME = "../1-extra_stuff/datasets/Cognitiwe_ornek_video_kisitli_alan.mov"

OUTPUT_GIF_FILENAME = "./output.gif"