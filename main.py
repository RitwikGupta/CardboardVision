# Main file for Popboard Python functions

import sys
from videoConvert import *
from constructImage import *
from makeMask import *
from makeVideo import *
from videoCapture import *
from videoConvert import *

"""for x in xrange(1,240):
    lastFew = 5 - len(str(x))
    nameEnd = "0" * lastFew + str(x)
    name = "test" + nameEnd + ".png"
#     addBars(name)
    maskName = "mask" + nameEnd + ".png"
    addLayer(name, "p" + name, maskName)"""
makeVideo("demovid2", "gptest", 24)

