#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:01:53 2017

@author: ross
"""

import requests
from bs4 import BeautifulSoup
results_url = "https://www.swimmingresults.org/biogs/biogs_details.php"
url = "https://www.swimmingresults.org/individualbest/personal_best.php?tiref=1197501&mode=A&back=biogs"
url2 = "https://www.swimmingresults.org/biogs/biogs_details.php?tiref=1197501"
result = requests.get(url2)   #grab a copy of content at url using request library
html = result.content        #use bytes conversion as opposed to text 
soup = BeautifulSoup(html, "lxml")  #create the soup using lxml parser
#instansiate the lists
times_list = []
races_list = []
for races1 in soup.find_all("td"):
    print(races1.get.text())