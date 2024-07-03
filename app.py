import requests 
from bs4 import BeautifulSoup as bs
website_url = input('Enter Website Url:')
url = website_url
r =requests.get(url)
soup = bs(r.content,'html.parser')
logo = soup.find('img',)['src']
print(logo)