import requests
import bs4
import collections
import webbrowser

def main():
    scraping()

def scraping():
    #sample: https://www.zstiojar.edu.pl/plan/zastepstwa/03-10/plany/o26.html
    url = 'https://www.zstiojar.edu.pl/plan-lekcji/zastepstwa'
    zas = get_all(get_raw_text(url))


def get_raw_text(url):
    response = requests.get(url)
    return response.text

def get_all(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    zast = soup.find_all('a')
    for x in zast:
    print(x)





if __name__ == '__main__':
    main()
