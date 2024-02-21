from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path


## def get_source() 
#  get web content using requests 
#  parse into html
#  get image link
#  return link

WIKI_PEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"

def _get_source(url):

    response = requests.get(url)

    if response.status_code == 200:

        html_raw = BeautifulSoup(response.text, 'html.parser')
        container = html_raw.find(id="mp-tfa-img")
        img = container.find(class_="thumbinner").find("span").find("a").find("img")
        get_list = ("src", "alt")
        result = []

        for ls in get_list:
            result.append(img.get(ls))
        

        return result
    
    else:
        
        print("error")
        return -1

def get_image():
    result = _get_source(WIKI_PEDIA_MAIN_PAGE)
    url = f"https:{result[0]}"
    image_response = requests.get(url)

    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        filename = f"{result[1]} {datetime.now().date()}"
        # os.chdir("../output")

        return (image, filename)
    else:
        print("Error ")
        return -1

# def main():
#     image_data = get_image()
#     image_data[0].save(f"output/{image_data[1]}.jpg")

# if __name__=="__main__":
#     main()
