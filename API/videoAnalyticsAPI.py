# Imports
import cv2
import os
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

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

analyze_url = endpoint + "vision/v2.1/analyze"

# Select video
vidcap = cv2.VideoCapture('./asset/testVideo5.MOV')

# analyzeFrame(sec) analysis the frame at the given sec from the selected video.
# Analyzed factors: Faces(age & gender).
def analyzeFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()   # Get the frame.
    if hasFrames:   # If frame exists.
        image_path = "./asset/tempImage" + str(count) + ".jpg"  # Set the local path of frame to analyze.
        cv2.imwrite(image_path, image)     # Save frame as JPG file.
        print("Detecting faces on image #{}".format(count))

        # Select the visual feature(s) wanted : Faces(age & gender).
        remote_image_features = ["faces"]

        # Call the API.
        image_data = open(image_path, "rb").read()  # Read the image into a byte array
        headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Faces'}
        response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status()

        # The 'analysis' object contains various fields that describe the image.
        analysis = response.json()
        # We are interested in the faces.
        if (len(analysis["faces"]) == 0):
            print("No faces detected.")
        else:
            for face in analysis["faces"]:
                # Print the results with gender, age
                results.append({"age":face["age"],"gender":face["gender"]})
                print("New face of age {} and gender {}".format(face["age"], face["gender"]))
        print()
        #os.remove(image_path)   # delete frame
        
    return hasFrames

sec = 0
frameRate = 1   # Captures image every second
count = 1   # Used to track the number of frames analyzed
results = []
success = analyzeFrame(sec)
while success:  # Keep analyzing frames until the end of the video has been reached
    count += 1
    sec += frameRate
    success = analyzeFrame(sec)

# Print analysis
print("Here is what we have detected overall:")
for result in results:
    print("{} of {} years old".format(result["gender"], result["age"])) 