#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:50:19 2017

@author: rossmaude
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
for table in soup.findAll('table', attrs = {'id':'"rankTable"'}):
    print(table)
for cell in soup.findAll('td', attrs = {'class':'"tdrank_right"'}):
    print("TD CELLS in loop")
    print("TD CELL", cell)
#for table in soup.findAll('table', attrs = {'id':'"rankTable"'}):
 #   print(table)
    #for row in table.findAll('tr',attrs={'class':'oddRow'}):
       # for col in row.findAll('td', attrs={'class':'tdrank_left'}):
          #  race = col
           # time = race.nextSibling
           # print(race.text.strip(), time.strip())
           
           
           
            
            
            
            
            
         