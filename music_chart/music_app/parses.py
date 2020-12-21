import requests

from bs4 import BeautifulSoup


URL = r'https://unistar.by/music/top20/'


class Parser:
    def __init__(self):
        self.session = requests.session()

    def get_chart(self):
        response = self.session.get(URL)
        return response.text

    @staticmethod
    def _parse_chart(songs: list, authors: list):
        response = []
        for song, author in zip(songs, authors):
            data = {'song': song.string, 'author': author.string}
            response.append(data)
        return response

    def parse_chart(self):
        content = self.get_chart()
        soup = BeautifulSoup(content, 'html.parser')
        song_class = 'top20-content__subtitle'
        author_class = 'top20-content__title'
        songs = soup.find_all('div', {'class': song_class})
        authors = soup.find_all('div', {'class': author_class})
        return self._parse_chart(songs, authors)





