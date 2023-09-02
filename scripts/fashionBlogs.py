import requests
from bs4 import BeautifulSoup
import json

def getLinks():
    main_url = "https://www.bloglovin.com/blogs/le-fashion-39894"
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, "html.parser")
    script_tags = soup.find_all('script', type='text/javascript')

    javascript_code = []
    
    for script_tag in script_tags:
        if script_tag.string:  # Check if the tag contains script content
            javascript_code.append(script_tag.string.strip())
    i = 0
    st = javascript_code[1][123:len(javascript_code[1])-1]
    json_dict = json.loads(st)
    l=[]
    for key in json_dict['postGridData']['meta']['resolved']['smallpost']:
        l.append(json_dict['postGridData']['meta']['resolved']['smallpost'][key]['link'])
    li=[]
    for link in l:
        if "lefashion" in link:
            li.append(link)
    return li

def getPara(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, "html.parser")
    top_product_elements = soup.find('div', class_="post-body entry-content")
    visible_text = top_product_elements.get_text(strip=True)
    return visible_text

def getTrendingPara():
    li =[]
    l = getLinks()
    print('done')
    c=0
    for link in l:
        a = getPara(link)
        print(c)
        c=c+1
        li.append(a)
    return li

def getKeyWords():
    links = getLinks()
    li = []
    c=0
    for main_url in links:
        print(c)
        response = requests.get(main_url)
        soup = BeautifulSoup(response.content, "html.parser")
        top_product_elements = soup.find('span', class_="post-labels")
        s = top_product_elements.get_text(strip=True)
        list1 = s[7:].split(',')
        li.extend(list1)
        c=c+1
    return li