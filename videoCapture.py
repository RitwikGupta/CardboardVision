# Module to take a YouTube video URL and download that video to a local directory within this folder

# created by rajat mehndiratta (github/knyte)

#!/usr/bin/env python2

from pytube import YouTube
from __future__ import print_function

def getVideo(URL, sourceObject):
    filetypes = ['mp4', 'flv', 'webm', '3gp']
    resolutions = ['480p', '360p', '240p', '720p', '1080p', '144p']
    for x in xrange(filetypes):
        for y in xrange(resolutions):
            try:
                video = sourceObject.get(x, y)
                return video
            except: pass
    return None

def saveVideo(URL, directory, filename):
    yt = YouTube()
    yt.url = URL
    yt.filename = filename
    video = getVideo(URL)
    if type(video) != None:
        video.download(directory)
    else:
        print "Pick another video! This one didn't work :("
