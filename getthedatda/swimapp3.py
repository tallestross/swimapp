#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:55:42 2017

@author: ross
"""
from bs4 import BeautifulSoup
import requests
from lxml import html
import re
from urlparse import urljoin

URL2 = "https://www.swimmingresults.org/individualbest/personal_best.php?tiref=1197501&mode=A&back=biogs"
URL = "https://www.swimmingresults.org/biogs/biogs_details.php?tiref=1197501"
BASE_URL = "https://www.swimmingresults.org/biogs"
session = requests.Session()
response = session.get(URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
print(response)
print(session)
# get frame links
soup = BeautifulSoup(response.text)
frames = soup.find_all('frame')

print(frames)
header_link, document_link = [urljoin(BASE_URL, frame.get('src')) for frame in frames]

# get header
session.get(header_link, headers={'Referer': URL})

# get document html url
response = session.get(document_link, headers={'Referer': URL})
soup = BeautifulSoup(response.text, "lxml")

content = soup.find('meta', content=re.compile('URL='))['content']
document_html_link = re.search('URL=(.*)', content).group(1)
#document_html_link = urljoin(BASE_ACCESS_URL, document_html_link)
print(content)
# follow html link and get the pdf link
response = session.get(document_html_link)
soup = BeautifulSoup(response.text)

# get the real document link
content = soup.find('meta', content=re.compile('URL='))['content']
document_link = re.search('URL=(.*)', content).group(1)
#document_link = urljoin(BASE_ACCESS_URL, document_link)
print document_link

# follow the frame link with login and password first - would set the important cookie
auth_link = soup.find('frame', {'name': 'footer'})['src']
session.get(auth_link)

# download file
with open('document.pdf', 'wb') as handle:
    response = session.get(document_link, stream=True)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
