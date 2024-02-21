#TODO: solve the import error 

from source import GetImageData
from source import GetTextData

WIKI_PEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"

def main():
    image_data = GetImageData.get_image(WIKI_PEDIA_MAIN_PAGE)
    image_data[0].save(f"output/{image_data[1]}.jpg")
    GetTextData.test(WIKI_PEDIA_MAIN_PAGE)

if __name__ == "__main__":
    main()