import os
# サービスアカウントキーのパス
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hait-primary-a-7416c5c3bb75.json" 

from google.cloud import vision
from google.cloud.vision import types
import io


def text_detection(img_path):
    client = vision.ImageAnnotatorClient()
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    
    return response.text_annotations[0].description.split("\n")