import requests
import bs4
import collections
import webbrowser
from urllib.parse import urlencode
from urllib.request import urlretrieve

#zast == zastepstwo == substitude

def main():
    url = 'https://www.zstiojar.edu.pl/plan-lekcji/zastepstwa'
    html = get_zast_page(url)
    choicses = available_zast(html)
    day_url = choice_day(choicses,'https://www.zstiojar.edu.pl')
    params = urlencode({"url": day_url, "access_key": "f626c08d073b451884f90e7477a878c7"})
    urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")


def get_zast_page(url):
    response = requests.get(url)
    return response.text


def available_zast(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    zasts = soup.find(class_='list-title')
    return zasts


def choice_day(choicses,url):
    link=choicses.find('a', href=True)
    link=link['href']
    day_url=url+link
    html = get_zast_page(day_url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    link = soup.find(class_='ls-article__content').find('p').find('a', href=True)
    link=link['href']
    final_link=url+link+'/plany/o26.html'
    return final_link

if __name__ == '__main__':
    main()
