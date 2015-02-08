# Module for constructing new frame and storing it in a new directory

import PIL
import Image
import colorsys
# Written by Al Basyoni and rajat mehndiratta (github/knyte) at TartanHacks s2015

def addBars(imageFile):
    ## imageFile is a path
    ## the output is going to be an image, not a path
    im = Image.open(imageFile)
    mode = im.mode
    size = im.size
    (width, height) = size

    width1 = width/3
    width2 = 2*width/3
    length = 15 
    
    box1 = (width1-length, 0, width1+length, height)
    box2 = (width2-length, 0, width2+length, height)

    newName = "p" + imageFile
    imCopy = im.copy()
    imCopy.paste("white", box1)
    imCopy.paste("white", box2)
    imCopy.save(newName)

    return newName
    

def addLayer(initialImage, imageFile, mask):
    
    im = Image.open(imageFile)
    (width, height) = im.size
    sequence = im.load()

    IM = Image.open(initialImage)
    SEQUENCE = IM.load()
    
    Maskim = Image.open(mask).convert('RGB')
    Masksequence = Maskim.load()
    for i in xrange(width/3 -15, width/3 + 15):
        for j in xrange(height):
            if toPrint(Masksequence, i, j):
                sequence[i, j] = SEQUENCE[i,j]
           
    for i in xrange(2*width/3 - 15, 2*width/3 + 15):
        for j in xrange(height):
            if toPrint(Masksequence, i ,j):
                sequence[i, j] = SEQUENCE[i, j]

    newName = "g" + imageFile
    im.save(newName)
        
    return newName

def toPrint(sequence, i, j):
    M = sequence[i, j]
    R = M[0]
    G = M[1]
    B = M[2]
    threshold = 0
    # if determinant(R, G, B) > threshold or R > 127 \
    #   and G > 127 and B > 127:
    if meetsConditions(R, G, B):
        return True
    return False

def determinant(R, G, B):
    return abs(R-G) + abs(G-B) + abs(R-B)

def meetsConditions(R, G, B):
    Rnot = float(R)/float(255)
    Gnot = float(G)/float(255)
    Bnot = float(B)/float(255)
    H, S, V = colorsys.rgb_to_hsv(R, G, B)
    if V > 65: return True
    else: return False


    
