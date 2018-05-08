from lib import getTitle
import requests
from bs4 import BeautifulSoup
# import re

# url = 'https://www.pythonscraping.com/pages/warandpeace.html'
#
#
# r = requests.get(url)
# bs = BeautifulSoup(r.text, 'html.parser')
# nameList = bs.find_all('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())
#

url = 'http://www.pythonscraping.com/pages/page3.html'

r = requests.get(url)
bs = BeautifulSoup(r.text, 'html.parser')

# for child in bs.find('table', {'id': 'giftList'}).children:
#     print(child)

# for descendant in bs.find('table', {'id': 'giftList'}).descendants:
#     print(descendant)

# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)


# images = bs.find_all('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])


# tags_two_attrs = bs.find_all(lambda tag: len(tag.attrs) == 2)
# for tag in tags_two_attrs:
#     print(tag)

tags_two_attrs = bs.find_all(lambda tag: 'Totally' in tag.get_text())
print(tags_two_attrs)
