import cv2

vid_num = 1 # degistir
input_video_file = "./1df965cd977c4adaa0a57ef650df6c25.mp4"
output_folder = "./reflective_coveralls/"

cap=cv2.VideoCapture(input_video_file, cv2.CAP_FFMPEG)
fps = cap.get(cv2.CAP_PROP_FPS)

# video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

frame_num = 0

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        frame_num += 1

        # Create ROI coordinates
        topLeft = (21, 331)
        bottomRight = (1831,1629)

        # kırmızı yer olan alanın
        # topLeft = (595, 739)
        # bottomRight = (2519,1901)

        x, y = topLeft[0], topLeft[1]
        w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

        # Grab ROI with Numpy slicing
        ROI = frame[y:y + h, x:x + w]

        """
         INTER_NEAREST – a nearest-neighbor interpolation 
         INTER_LINEAR – a bilinear interpolation (used by default) 
         
         INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation,
         as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method. 
          
         INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood 
         INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood
         """

        frame = cv2.resize(ROI, (416, 416), interpolation=cv2.INTER_AREA) # obj detections!!!!
        # height, width, layers = frame.shape
        # dh, dw, _ = frame.shape
        # img_size = (width, height)
        print('Frame #: ', frame_num)

        filename= str(output_folder) + "reflective_coveralls_" + str(vid_num) + "_%d.jpg" % frame_num;
        cv2.imwrite(filename,frame)

    if(ret != True):
        break

cap.release()
print("Done!")