# Convert local video into frames/images

# Imports
import cv2

# Select video
vidcap = cv2.VideoCapture('./testVideo.MOV')

# getFrame(sec) gets the frame from selected video at the given sec
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

sec = 0
frameRate = 1 # Captures image every second
count = 1
success = getFrame(sec)
while success:
    print("here")
    count += 1
    sec += frameRate
    sec = round(sec, 2)
    success = getFrame(sec)