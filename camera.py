#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2 as cv
#from imutils.video.pivideostream import PiVideoStream
#from imutils.video.pivideostream import WebcamVideoStream
import imutils
import time
from datetime import datetime
import numpy as np

class VideoCamera(object):
    def __init__(self, flip = False, file_type  = ".jpg", photo_string= "stream_photo"):
        #self.vs = PiVideoStream(resolution=(1920, 1080), framerate=30).start()
        #self.vs = WebcamVideoStream().start()
        self.vs = cv.VideoCapture(0)
        self.flip = flip # Flip frame vertically
        self.file_type = file_type # image type i.e. .jpg
        self.photo_string = photo_string # Name to save the photo
        time.sleep(2.0)

    def __del__(self):
        self.vs.release()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        success, frame = self.vs.read()
        #frame = self.vs
        if frame is not None:
            ret, jpeg = cv.imencode(".jpg",frame)
        else:
            print("frame is None")
        self.previous_frame = jpeg
        return jpeg.tobytes()

    # Take a photo, called by camera button
    def take_picture(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, image = cv.imencode(self.file_type, frame)
        today_date = datetime.now().strftime("%m%d%Y-%H%M%S") # get current time
        cv.imwrite(str(self.photo_string + "_" + today_date + self.file_type), frame)
