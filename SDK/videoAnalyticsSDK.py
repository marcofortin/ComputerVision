# Imports
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import cv2

# Add your Computer Vision subscription key to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# Add your Computer Vision endpoint to your environment variables.
if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

# Instantiate client with endpoint and key
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Select video
vidcap = cv2.VideoCapture('./testVideo.MOV')

# Definition of function
def analyseFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        imageUrl = "image"+str(count)+".jpg"
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
        print("Detecting faces on image #{}".format(count))
        # Select the visual feature(s) you want.
        remote_image_features = ["faces"]
        # Call the API with remote URL and features
        detect_faces_results_remote = computervision_client.analyze_image("https://ak0.picdn.net/shutterstock/videos/21658720/thumb/1.jpg", remote_image_features)

        # Print the results with gender, age, and bounding box
        #print("Faces in the remote image : {}".format(image["label"]))
        if (len(detect_faces_results_remote.faces) == 0):
            print("No faces detected.")
        else:
            for face in detect_faces_results_remote.faces:
                print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
                face.face_rectangle.left, face.face_rectangle.top, \
                face.face_rectangle.left + face.face_rectangle.width, \
                face.face_rectangle.top + face.face_rectangle.height))
        print("\n")
    return hasFrames

sec = 0
frameRate = 1 # Captures image every second
count = 1
success = analyseFrame(sec)
while success:
    print("here")
    count += 1
    sec += frameRate
    sec = round(sec, 2)
    success = analyseFrame(sec)    