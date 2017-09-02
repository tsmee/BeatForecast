import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.discogs.com/Not-Waving-Animals/release/8092763")
soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find('ul', class_='last')

z = str(a.get_text())

zz = z.split("\n")
xx = []
for n in zz:
    xx.append(n.lstrip())
xx = [x for x in xx if x]

print (xx)
