import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class Scrapper:

    def find_news_by_coin(self, currency: str):
        headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
        link = "https://www.google.com/search?hl=en&q=after:" + str((datetime.now() - timedelta(days=30)).date()) + \
               "+site%3Acoinmarketcap.com/headlines/news/+" + currency
        site_text = requests.get(link, headers=headers).text
        soup = BeautifulSoup(site_text, "html.parser")
        g = soup.find('div', class_='main')
        anchors = g.find_all('a')
        if anchors:
            for link in anchors:
                try:
                    description = link.parent.parent.find_all('div', recursive=False)[1].find("div", recursive=False).text
                    title = link.find('h3').text
                    print(title)
                    print(link['href'])
                    print(description + "\n")
                except (AttributeError, IndexError):
                    pass

scrapper = Scrapper()

scrapper.find_news_by_coin('cardano')