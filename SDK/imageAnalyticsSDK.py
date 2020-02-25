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

# Reference to images to analyze
#remote_image_url = "https://us.123rf.com/450wm/fotoluminate/fotoluminate1602/fotoluminate160200097/52651446-elderly-eighty-plus-year-old-man-with-granddaughter-in-a-home-setting-.jpg?ver=6"
remote_image_url = [
    {"label":"Old man & young woman", "link":"https://us.123rf.com/450wm/fotoluminate/fotoluminate1602/fotoluminate160200097/52651446-elderly-eighty-plus-year-old-man-with-granddaughter-in-a-home-setting-.jpg?ver=6"},
    {"label":"Family", "link":"https://image.shutterstock.com/image-photo/family-relaxing-on-sofa-260nw-278188052.jpg"},
    {"label":"People walking on the street", "link":"https://walksf.org/wp-content/uploads/2018/10/6th-street-2500x750.jpg"},
    {"label":"Woman at cashier", "link":"https://ak0.picdn.net/shutterstock/videos/21658720/thumb/1.jpg"},
    {"label":"Train station", "link":"https://dispatcheseurope.com/wp-content/uploads/2018/04/people-waiting-train-station-breda-netherlands-30160143.jpg"},
]

'''
Detect Faces from list of images
This example detects faces in a remote image, gets their gender and age, 
and marks them with a bounding box.
'''
for i, image in enumerate(remote_image_url):
    print("Detecting faces on image #{}".format(i))
    # Select the visual feature(s) you want.
    remote_image_features = ["faces"]
    # Call the API with remote URL and features
    detect_faces_results_remote = computervision_client.analyze_image(image["link"], remote_image_features)

    # Print the results with gender, age, and bounding box
    print("Faces in the remote image : {}".format(image["label"]))
    if (len(detect_faces_results_remote.faces) == 0):
        print("No faces detected.")
    else:
        for face in detect_faces_results_remote.faces:
            print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
            face.face_rectangle.left, face.face_rectangle.top, \
            face.face_rectangle.left + face.face_rectangle.width, \
            face.face_rectangle.top + face.face_rectangle.height))
    print("\n")

