import requests
from bs4 import BeautifulSoup

#** No problem here **#


def get_source_text(url):
    response = requests.get(url)

    if response.status_code == 200:

        raw_html = BeautifulSoup(response.text, "html.parser")
        main_page_tfa = raw_html.find(id="mp-tfa").find("p")
        link_tag = main_page_tfa.find("b").find("a")
        href = link_tag.get("href")
        # print(href)
        url_page = f"https://en.wikipedia.org/wiki{href}?printable=yes"
        
        # print(url_page)
        # print(link_tag.get("title"))

        return (url_page, link_tag.get("title"))
    else:
        print("error")
        return -1
    

def _get_source_image(url):

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
    

if __name__ == "__main__":
    WIKI_PEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"
    image = _get_source_image(WIKI_PEDIA_MAIN_PAGE)

    text = get_source_text(WIKI_PEDIA_MAIN_PAGE)
    print(image)
    print(text)