#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 09:22:51 2017

@author: ross
"""

import requests
from bs4 import BeautifulSoup
results_url = "https://www.swimmingresults.org/biogs/biogs_details.php"
url = "https://www.swimmingresults.org/individualbest/personal_best.php?tiref=1197501&mode=A&back=biogs"
url2 = "https://www.swimmingresults.org/biogs/biogs_details.php?tiref=1197501"
page_data = requests.get(url)   #grab a copy of content at url using request library
html = page_data.content        #use bytes conversion as opposed to text 
soup = BeautifulSoup(html, "lxml")  #create the soup using lxml parser
#instansiate the lists

races_list = []

table_count = 0
for table in soup.find_all("table", id="rankTable"):   #Find the tables in 
    table_count = table_count + 1
    for row in table.find_all("tr"):   #Find the rows in each table
        colnum = 0
        for col in row.find_all("td", class_="tdrank_left"):  #Find the cells in each row
            race = col                #Text of race name is in first cell
            time = race.nextSibling   #Use nextSibling to get the next across
            if table_count == 1:
                race_list =  race.text + " LC"
                race_time = time.text
                result = race_list, race_time
                races_list.append(result) #identify long course times
            elif table_count == 2:
                race_list =  race.text + " SC"
                race_time = time.text
                result = race_list, race_time #identify short course times
                races_list.append(result) #identify short course times
print(races_list[0::3])    #we only wanted the first line returned


   ###     
           
       # for col in row.findAll('td', attrs={'class':'tdrank_left'}):
          #  race = col
           # time = race.nextSibling
