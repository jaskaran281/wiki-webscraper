from PIL import Image
from io import BytesIO
from datetime import datetime

import requests

from GetSource import _get_source_image


## def get_source() 
#  get web content using requests 
#  parse into html
#  get image link
#  return link

WIKI_PEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"



def get_image(url):

    #* uses _get_source() to get the url to image
    #* and also retrieves the name or title for the image
    #* in form of ("src", "alt")

    result = _get_source_image(url)
    url = f"https:{result[0]}"
    image_response = requests.get(url)

    if image_response.status_code == 200:

        #* encodes the recieved data as an Image object
        image = Image.open(BytesIO(image_response.content))
        filename = f"{result[1]} {datetime.now().date()}"
        # os.chdir("../output")


        # * returns the image data and a filename to save the image 
        return (image, filename)
    else:
        print("Error ")
        return -1




def main():
    image_data = get_image(WIKI_PEDIA_MAIN_PAGE)
    print(image_data)
    image_data[0].save(f"output/{image_data[1]}.jpg")

if __name__=="__main__":
    main()
