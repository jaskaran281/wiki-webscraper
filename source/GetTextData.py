
import requests
from bs4 import BeautifulSoup

WIKI_PEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"

def get_source_text(url):
    response = requests.get(url)

    if response.status_code == 200:

        raw_html = BeautifulSoup(response.text, "html.parser")
        main_page_tfa = raw_html.find(id="mp-tfa").find("p")
        link_tag = main_page_tfa.find("b").find("a")
        href = link_tag.get("href")
        # print(href)
        url_page = str(f"https://en.wikipedia.org/{href}?printable=yes").strip()
        
        print(url_page)
        print(link_tag.get("title"))

        return (url_page, link_tag.get("title"))
    else:
        print("error")
        return -1
    




if __name__ == "__main__":

    get_source_text(WIKI_PEDIA_MAIN_PAGE)

