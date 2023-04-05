import subprocess
import re


def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def crop_video(video_read_path, video_write_path, start_time, end_time):
    """Crop a video given start and end time.

    :param video_read_path: Full path of the video to read.
    :param video_write_path: Full path of the video to write.
    :param start_time: String of format "hh:mm:ss" indicating crop start.
    :param end_time: String of format "hh:mm:ss" indicating crop end.
    :return: None.
    """
    # video file path
    video_path = video_read_path

    # ffprobe command
    command = f'ffprobe -i {video_path} -show_entries format=duration -v quiet -of csv="p=0"'

    # run command
    output = subprocess.check_output(command, shell=True).decode('utf-8').strip()

    # float video duration
    duration = float(output)

    # input video file path
    input_file = video_read_path

    # start and end times
    start_time = get_sec(start_time)
    end_time = get_sec(end_time)

    # ffmpeg command
    command = f'ffmpeg -i {input_file} -ss {start_time} -to {end_time} -c:v copy -c:a copy {video_write_path}'

    # call command using subprocess module
    subprocess.call(command, shell=True)
