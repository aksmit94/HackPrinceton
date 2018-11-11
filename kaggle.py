import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def get_data(keyword):

    keyword = ' '.join(keyword.split())
    keyword = "kaggle corpus "+keyword
    url = "https://www.google.com/search?q=" + keyword
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    s = str(soup)

    s = s.replace("<b>","")
    s = s.replace("</b>","")

    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s)

    link = ""
    flag = 0
    for i in url:
        if "www.kaggle.com" in i:
            link = i
            tmp = ""
            for j in link:
                if j=='&':
                    break
                tmp += j
            flag = 1
            link = tmp
        if flag == 1:
            break
        
    return link + '/data'

print (get_data(str(input())))
