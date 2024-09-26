import requests
import os
from dotenv import load_dotenv
from help_for_nasa_api import get_extension
from help_for_nasa_api import upload_images

def fetch_nasa_apod ():
    load_dotenv()
    params ={
        'api_key': os.getenv("API_KEY"),
        'count': 30
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    url_images = response.json()
    for i in range(params['count']):
        url_image = url_images[i]['url']
        filename = f'nasa_{i+1}{get_extension(url_image)}'
        filepath = os.path.join('images', filename)
        upload_images(url_image, filepath)