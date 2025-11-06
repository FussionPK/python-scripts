#spider
#https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()
def spider_url(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed for {url}")
        return
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        a_tags = soup.find_all('a')
        urls = []
        for a_tag in a_tags:
            href = a_tag.get('href')
            if href is not None and href != "":
                urls.append(href)

        for i in urls:
            if i not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, i)
                if keyword in url_join:
                    print(url_join)
                    spider_url(url_join, keyword)
            else:
                pass

url = input("What URL are we scraping today? ")
keyword = input("What keyword are we scraping today? ")

spider_url(url, keyword)
