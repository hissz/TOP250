import requests
from bs4 import BeautifulSoup

def get_book(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title_list = soup.select('h1 > span')
    title = title_list[0].text
    author_list = soup.select('div#info > a')
    author = author_list[0].text.replace(" ", "").replace("\n", "")
    score_list = soup.select('strong.ll.rating_num')
    score = score_list[0].text

    data = {
        'title':title,
        'score':score,
        'author':author,
    }

    print(data)


def get_all_book():
    for i in range(0,250,25):
        url = 'https://book.douban.com/top250?start=' + str(i)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        href_list = soup.select('div.pl2 > a')
        for href in href_list:
            link = href.get('href')
            get_book(link)

get_all_book()


