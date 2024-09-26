import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from help_for_nasa_api import upload_images

def fetch_nasa_epic():
    load_dotenv()
    params ={
            'api_key': os.getenv("API_KEY"),
        }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/', params=params)
    response.raise_for_status()
    for i in range (0,5):
        date_string = response.json()[i]['date']
        date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        formatted_date = date_obj.strftime("%Y/%m/%d")
        image = response.json()[i]['image']
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image}.png?api_key=DEMO_KEY'
        filename = f'EPIC{i+1}.png'
        filepath = os.path.join('images', filename)
        upload_images(url_image, filepath)

