# For the sake of time we will extract the following URL only
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import sys

def toolkits(keyword):


    keyword = ' '.join(keyword.split())

    url = "https://devpost.com/software/search?query=" + keyword
    
    
    response = requests.get(url)
   

    soup = BeautifulSoup(response.text, 'html.parser')
#    print (type(soup))
#    print (soup.prettify())

    results = str(soup)
    
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', results)

    urls = []
    for i in url:
        if "png" not in i and "jpeg" not in i and "jpg" not in i:
            urls.append(i)



    website = ['https://devpost.com/software/hacknjit18-self-driving-car',
               'https://devpost.com/software/ride-fyi',
               'https://devpost.com/software/sensethepoce-orw0qu',
              'https://devpost.com/software/arc-p2rjuo']
    website = urls
    A = []
    B = []
    for m in website:

        quote_page = m
        page = requests.get(quote_page)
        soup = BeautifulSoup(page.text, 'html.parser')
        technology = soup.find(class_='no-bullet inline-list')
        try:
            technology_item1 = technology.find_all('a')
        except:
            print("Not Found! :( ")
            sys.exit()
        for i in technology_item1:
    #         print (i.contents[0])s
            A.append (i.contents[0])

        remove = soup.find_all(class_='cp-tag recognized-tag')
        for j in remove:
            j.decompose()

        technology_item2 = technology.find_all('span')
        for k in technology_item2:
    #         print (k.contents[0])
            B.append(k.contents[0])

    Final = Counter(A+B)
    return (Final)

print (toolkits("VGG"))



