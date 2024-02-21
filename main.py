#TODO: solve the import error 

from source import GetImageData
from source import GetTextData

import pdfkit
import datetime
from pathlib import Path

WIKI_PEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"
def main():
    date = datetime.datetime.now().date()
    image, filename = GetImageData.get_image(WIKI_PEDIA_MAIN_PAGE)
    url , title = GetTextData.get_source(WIKI_PEDIA_MAIN_PAGE)

    out_dir_path = Path(f"output/{title} {date}")
    out_dir_path.mkdir(exist_ok=True)

    image.save(f"{out_dir_path}/{filename}.jpg")
    pdfkit.from_url(url,  f"{out_dir_path}/{title}{date}.pdf")
    
    return 0


if __name__ == "__main__":
    main()