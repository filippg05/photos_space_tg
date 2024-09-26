import requests
import os

def upload_images (url_image, filepath):
    os.makedirs("images", exist_ok=True)
    response = requests.get(url_image)
    response.raise_for_status()
    with open(filepath, 'wb') as file:  
        file.write(response.content)


def get_extension (url_image):
    extension = os.path.splitext(url_image)[1]
    return extension