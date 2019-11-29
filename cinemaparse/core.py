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
    print (self.content.prettify())
  def get_films_list(self):
    self.extract_raw_content()
    titles = []
    films = self.content.find_all('div', {'class': 'movie-plate'})
    for film in films:
      titles.append(film["attr-title"])
    return titles
  def get_nearest_film_session(self, film):
    self.extract_raw_content()
    films = self.content.find_all('div', {'class': 'movie-plate'})
    x = self.content.find('div', {'attr-title': film})
    a= x.find('div',{'class':'movie-next-screening'}).find('span',{'class':'label label-bg label-default normal-font'}).text
    if a == ' сегодня': 
      href = x.find('div',{'class': 'text-center movie-poster-mobile'}).find('a').get('href')
      newurl = self.url + href
      content= requests.get(newurl)
      content=BeautifulSoup(content.text, 'html.parser')
      y=content.find('table',{'class':'table table-bordered table-condensed table-curved table-striped table-no-inside-borders'}).find('div',{'class':'cinema-name'}).find('a',{'class':'underdashed'})
      print(y.text)
      z=content.find('table',{'class':'table table-bordered table-condensed table-curved table-striped table-no-inside-borders'}).find('a',{'class':'btn btn-default navbar-btn price-button cell-screening-desktop'}).text
    else:
      z=(None, None)
    return z
msk_parser = CinemaParser()
print(msk_parser.get_films_list())
spb_parser = CinemaParser('spb')
print(spb_parser.get_films_list())
print(msk_parser.get_nearest_film_session('Джокер'))
