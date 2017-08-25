#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:01:29 2017

@author: ross
"""

import requests
from bs4 import BeautifulSoup
races = ["50m Freestyle", "100m Freestyle", "200m Freestyle", "400m Freestyle", "800m Freestyle", "1500m Freestyle", "50m Backstroke", "100m Backstroke", "200m Backstroke", "100m Individual Medley"]
results_url = "https://www.swimmingresults.org/biogs/biogs_details.php"
url = "https://www.swimmingresults.org/individualbest/personal_best.php?tiref=1197501&mode=A&back=biogs"
url2 = "https://www.swimmingresults.org/biogs/biogs_details.php?tiref=1197501"
url3 = "https://www.swimmingresults.org/individualbest/personal_best.php?tiref=1197501&mode=A&back=biogs"
result = requests.get(url3)   #grab a copy of content at url using request library
html = result.content        #use bytes conversion as opposed to text 
soup = BeautifulSoup(html, "lxml")  #create the soup using lxml parser
#swimmer = soup.find("td", text="Name").find_next_sibling("td").text
#print(swimmer)
print("Long Course Times")

bk50lc = soup.find("td", text="50 Backstroke").find_next_sibling("td").text
print(bk50lc)
print(soup.find_all("td", text="50 Backstroke"))
print(soup.find_all("tscourse=L"))
#instansiate the lists
times_list = []
races_list = []
#50breast = soup.find("td", text="50m Breaststroke").find_next_sibling("td").text
print("Short Course Times")
#for race in races:
#    print(race, soup.find("td", text=(soup.find("td", text=race).find_next_sibling("td").text)).find_next_sibling("td").text)
#print("End")
#races_list.append(soup.find("td", text=(soup.find("td", text=(soup.find("td", text="50m Breaststroke").find_next_sibling("td").text)).find_next_sibling("td").text)).find_next_sibling("td").text)
#rint(races_list)
#BR50SC = races_list[0]

#print(race," : ", BR50SC)

