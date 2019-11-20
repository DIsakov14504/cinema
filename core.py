import requests
from bs4 import BeafutifulSoup
class CinemaParser:
  def _init_(self,city):
    self.city=city
  def extract_raw_content(self):
    resp=requests.get(https://msk.subscity.ru)
    soup=BeautifulSoup(resp.text, 'html.parser')
    return soup
  def print_raw_content(self):
    self.extract_raw_content()
    return (extract_raw_content(self),prettify())
  def get_films_list():
    
