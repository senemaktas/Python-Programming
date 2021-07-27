!pip install -q youtube-dl

""" Run youtube-dl -F URL to get a list of available formats for video/audio, then choose the one you want and get it using 
youtube-dl -f [format-number] URL like: youtube-dl -f 43 URL """

# get format number from list 
!youtube-dl -F https://www.youtube.com/watch?v=jKLrV2pfpoU&list=PL7WS8odYod9ztsoA0xy7pebmfHs23cq_N

# importing module
import youtube_dl
  
!youtube-dl -f 'bestvideo[ext=mp4]' --output "youtube.%(ext)s" https://www.youtube.com/watch?v=8Rhimam6FgQ=$YOUTUBE_ID
