# Module for taking a locally saved video and extracting audio and frames

# written by rajat mehndiratta (github/knyte) at TartanHacks w2015
# tested and fixed by Ritwik Gupta (github/RitwikGupta)
# credit to Ayub Khan @ StackOverflow

import subprocess
import cv2

def getAudio(videoFile, audioName):
    assert(type(videoFile) == type(audioName) == str)
    command = "ffmpeg -i " + videoFile + "- ab 160k ac 2 -ar 44100 -vn " + audioName + ".wav"
    subprocess.call(command, shell=True)

def getFrames(videoFile, namePrefix):
    assert(type(videoFile) == str)
    vc = cv2.VideoCapture(videoFile)
    c = 1

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        length = 5 -len(str(c))
        cv2.imwrite(str(namePrefix + "0"*length + str(c)) + ".png", frame)
        c += 1
        cv2.waitKey(1)

    vc.release()
    return c
getFrames("driving_trim.mp4", "test")
