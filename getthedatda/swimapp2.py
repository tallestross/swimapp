# -*- coding: utf-8 -*-
from lxml import html
from bs4 import BeautifulSoup
import requests


url2 = "https://www.swimmingresults.org/individualbest/personal_best.php?tiref=1197501&mode=A&back=biogs"
url = "https://www.swimmingresults.org/biogs/biogs_details.php?tiref=1197501"
page = requests.get(url)
tree = html.fromstring(page.content)
soup = BeautifulSoup(page.text, "lxml")
free = tree.xpath('//*[@id="rankTable"]')
soup
#
#long_course = tree.xpath('//*[@id="rankTable"]')
#50free = tree.xpath('//table[@id="rankTable"]//tr')
#print('Long_Course: ', long_course)
#print('50free: ', 50free)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
divs = soup.div
print(divs)


session = requests.Session()
response = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})