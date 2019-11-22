import requests
from bs4 import BeautifulSoup
class CinemaParser:
  def __init__(self, city='msk'):
    if city == 'msk':
      self.url = 'https://msk.subscity.ru'
    else:
      self.url = 'https://spb.subscity.ru'
    self.city=city
  def extract_raw_content(self):
    resp=requests.get(self.url)
    self.content=BeautifulSoup(resp.text, 'html.parser')
  def print_raw_content(self):
    self.extract_raw_content()
    print (self.content,prettify())
  def get_films_list(self):
    self.extract_raw_content()
    titles = []
    films = self.content.find_all('div', {'class': 'movie-plate'})
    for film in films:
      titles.append(film["attr-title"])
    return titles
msk_parser = CinemaParser()
print(msk_parser.get_films_list())
spb_parser = CinemaParser('spb')
print(spb_parser.get_films_list())
