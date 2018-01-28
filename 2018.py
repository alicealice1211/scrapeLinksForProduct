# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import bs4 as bs
import re
import csv
import time
allUrls=['https://javabeanplus.com/collections/signature-blends','https://javabeanplus.com/collections/signature-blends?page=2','https://javabeanplus.com/collections/signature-blends?page=3','https://javabeanplus.com/collections/world-origins','https://javabeanplus.com/collections/world-origins?page=2','https://javabeanplus.com/collections/green-coffee','https://javabeanplus.com/collections/green-coffee?page=2','https://javabeanplus.com/collections/espresso', 'https://javabeanplus.com/collections/flavored', 'https://javabeanplus.com/collections/flavored?page=2', 'https://javabeanplus.com/collections/flavored?page=3', 'https://javabeanplus.com/collections/flavored?page=4','https://javabeanplus.com/collections/organic', 'https://javabeanplus.com/collections/organic?page=2', 'https://javabeanplus.com/collections/decaf','https://javabeanplus.com/collections/tea','https://javabeanplus.com/collections/tea?page=2','https://javabeanplus.com/collections/tea?page=3','https://javabeanplus.com/collections/tea?page=4']
allNames=[]
allLinks=[]

x=0
while x<len(allUrls):
    url=allUrls[x]
    x+=1

    file_name = ('bbq'+".csv")

    headers = {'User-Agent':'Mozilla/5.0'}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code. text
    soup = bs.BeautifulSoup(plain_text, 'lxml')
    
    for coffee, link in zip (soup.find_all(class_='list-title'),soup.find_all(class_='btn')):
        coffee  = str(coffee).split('>')[2].split('<')[0]
        allNames.append(coffee)
        y= str(link)[1:]  
        link=str(link).split('href="')[1].split('>')[0]
        link='https://javabeanplus.com'+link
        allLinks.append(link)
         



rows=zip (allNames,allLinks)
with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
    links_writer=csv.writer(csvfile)
    for row in rows:
        links_writer.writerow(row)


