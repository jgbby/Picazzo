from bs4 import BeautifulSoup
import requests
import sys


def scrape(content):
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup.prettify())
    html = list(soup.children)[2]
    divs = soup.find_all('div')
    for div in divs:
        if div.get

    imgs = soup.find_all('img', class_='')
    for img in imgs:
        title = img.get('title')
        print(title)


def main():
    url = sys.argv[1]
    page = requests.get(url)
    if page.status_code == 200:
        scrape(page.content) 
    
if __name__ == "__main__":
    main()
