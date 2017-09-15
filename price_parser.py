import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.discogs.com/Consumer-Electronics-Repetition-Reinforcement-/release/6724351")
soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find('ul', class_='last')

z = str(a.get_text())

zz = z.split("\n")

#после удаления \n в списке остаются элементы из одних пробелов и пустые элементы. удаляем их.
zzz = [x.strip() for x in zz if not all(c == ' ' for c in x)]






