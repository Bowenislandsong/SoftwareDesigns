import io
import os
from PIL import Image
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GoogleAPISecretes.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()



# The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'DOrem88W4AU2PpD.jpg')
def labels(jpgfile,pref):
	file, ext = os.path.splitext(jpgfile)
# Loads the image into memory
	with io.open(jpgfile, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations
	labelsonly = []
	for label in labels:
		print(label.description)
		labelsonly.append(label.description)
	if (pref != '' ):
		if (pref not in labelsonly):
			os.remove(jpgfile)
			return False
	
	return labelsonly






			



