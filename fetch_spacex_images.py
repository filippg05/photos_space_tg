import requests
import os
import argparse
from help_for_nasa_api import get_extension
from help_for_nasa_api import upload_images



def fetch_spacex_last_launch ():
    parser = argparse.ArgumentParser(
        description='Скачать изображения с последнего запуска SpaceX.'
    )   
    parser.add_argument(
        'launch',
        help='ID запуска. Если не задано, будет использован ID последнего запуска.',
        nargs='?',
        default=None
        )
    args = parser.parse_args()
    if args.launch is None:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        response.raise_for_status()
    else:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{args.launch}')
        response.raise_for_status()
    url_images = response.json()['links']['flickr']['original']
    for i, url_image in enumerate(url_images):
        filename = f'space_{i+1}{get_extension(url_image)}'
        filepath = os.path.join('images', filename)
        upload_images(url_image, filepath)