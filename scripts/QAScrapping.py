import requests
from bs4 import BeautifulSoup
import json


def getAnswers(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, "html.parser")
    tp = soup.find_all('div', class_="user-content clearfix")
    li = []
    for i in tp:
        vt = i.get_text(strip=True)
        li.append(vt)
    return li

def refined(d):
    d3={}
    for key in d:
        s = key.lower()
        if 'where' in s:
            continue
        else:
            d3[key] = d[key]
    return d3

def getQuestionAnswers():
    url = 'https://www.blurtit.com/Fashion/?page='
    d = {}
    for i in range(1,55):
        u = url+ str(i)
        response = requests.get(u)
        soup = BeautifulSoup(response.content, "html.parser")
        tp = soup.find_all('div', class_='feed-item-title clearfix')
        a=0
        for item in tp:
            qa = item.get_text(strip=True)
            href_link = item.find('a')['href']
            d[qa] = getAnswers('https:'+href_link)
            print(a)
            a=a+1
        print(" ")
        print(i)
        print(" ")
    return refined(d)


            