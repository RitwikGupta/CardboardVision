# Module for stringing together images (frames) and audio file to create video

# Written by rajat mehndiratta (github/knyte)
# Edited and fixed by Ritwik Gupta (github/RitwikGupta)
# credit to Daniel Stutzbach and Richard Bronosky on StackOverflow
# as well as Peter Mortensen and ifLoop

import subprocess
import os
import os.path
import datetime
import time

def makeVideo(movieName, framePrefix, fps):
    assert(type(fps) == int)
    assert(type(movieName) == str)
    assert(type(framePrefix) == str)
    command = "ffmpeg -f image2 -r " + str(fps) + " -i " + framePrefix + "%05d.png -vcodec mpeg4 -y " + movieName + ".mp4"
    subprocess.call(command, shell=True)

def getFrameRate(framePrefix, filename, frames, directory="."):
    allFiles = [name for name in os.listdir(directory) if os.path.isfile(name)]
    prefixedFiles = [fileItem for fileItem in allFiles if framePrefix in fileItem]
    result = subprocess.Popen(["ffprobe", filename],
                              stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    duration = [x for x in result.stdout.readlines() if "Duration" in x]
    if len(duration) < 1:
        return 24
    else:
        timeLine = duration[0]
        timestr = timeLine[timeLine.index(":")+1:timeLine.index(".")]
        ftr = [3600,60,1]
        x = sum([a*b for a,b in zip(ftr, map(int,timestr.split(':')))])
        return frames/x
    return 42

def addAudio(audioFile, videoFile, destinationFile):
    assert(type(audioFile) == type(videoFile) == type(destinationFile) == str)
    command = "ffmpeg -y -i " + audioFile + ".wav -r 30 -i " + videoFile + ".mp4 -filter:a aresample=async=1 -c:a flac -c:v copy " + destinationFile + ".mp4"
    subprocess.call(command, shell=True)

print getFrameRate("test", "driving_trim.mp4", 240, ".")
