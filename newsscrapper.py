from bs4 import BeautifulSoup
import requests
from requests.api import request

def scrapNDTV():
    data = requests.get('https://www.ndtv.com/top-stories')
    if data.status_code == 200:
        print('success')
    elif data.status_code == 404:
        print('page not found')
    elif data.status_code == 500:
        print('server error')

    soup = BeautifulSoup(data.text)

    rows = soup.findAll('div', { 'class' : 'news_Itm' })
    newsdata = []
    for row in rows:
        if 'adBg' not in row.attrs.get('class'):
            detail = {}
            detail['heading'] = row.find('h2',{'class':'newsHdng'}).text
            detail['image'] = row.find('img').attrs.get('src')
            detail['summary'] = row.find('p',{'class':'newsCont'}).text
            newsdata.append(detail)

    return newsdata
    

def scrapIndiatoday():

    data=requests.get("https://www.indiatoday.in/top-stories")

    if data.status_code == 200:
        print('success')
    elif data.status_code == 404:
        print('page not found')
    elif data.status_code == 500:
        print('server error')

    soup=BeautifulSoup(data.text)  

    rows =soup.findAll('div', { 'class' : 'catagory-listing' }) 
    newsdata=[]
    for row in rows:
        details={}
        details['heading']=row.find('a')
        details['image']=row.find('img').attrs.get('src')
        details['summary']=row.find('p')
        
        newsdata.append(details)

    return newsdata