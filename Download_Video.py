!pip install -q youtube-dl

""" Run youtube-dl -F URL to get a list of available formats for video/audio, then choose the one you want and get it using 
youtube-dl -f [format-number] URL like: youtube-dl -f 43 URL """

# get format number from list 
!youtube-dl -F https://www.youtube.com/watch?v=jKLrV2pfpoU&list=PL7WS8odYod9ztsoA0xy7pebmfHs23cq_N

# importing module
import youtube_dl
  
!youtube-dl -f 'bestvideo[ext=mp4]' --output "youtube.%(ext)s" https://www.youtube.com/watch?v=8Rhimam6FgQ=$YOUTUBE_ID

  # show video on colab
def show_local_mp4_video(file_name, width=640, height=480):
  import io
  import base64
  from IPython.display import HTML
  video_encoded = base64.b64encode(io.open(file_name, 'rb').read())
  return HTML(data='''<video width="{0}" height="{1}" alt="test" controls>
                        <source src="data:video/mp4;base64,{2}" type="video/mp4" />
                      </video>'''.format(width, height, video_encoded.decode('ascii')))

show_local_mp4_video('50_Ways_to_Fall.mp4', width=960, height=720)
