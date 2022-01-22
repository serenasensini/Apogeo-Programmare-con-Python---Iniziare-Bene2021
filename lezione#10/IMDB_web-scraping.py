# pip install bs4
# pip install requests


import requests
from bs4 import BeautifulSoup
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
  
# HTTP REQUEST
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
  
# GET HTTP RESPONSE  
def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return (soup)
  
  
url = "https://www.imdb.com/title/tt4901306/reviews?ref_=tt_ql_3"
  
soup = html_code(url)

# GET DATA FROM HTML
def retrieve_data(soup):
    data_str = ""
    cus_list = []
  
    for item in soup.find_all("div", {'class':['text', 'show-more__control']}):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list
  
  
data = retrieve_data(soup)

# GET REVIEWS
print(data)

# COUNT REVIEWS
len(cus_res)
