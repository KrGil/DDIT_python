import requests
from bs4 import BeautifulSoup
 
response = requests.get('http://localhost/MYSERVER/secret.html')
 
txt = response.text
 
# print(txt)

soup = BeautifulSoup(txt, 'html.parser')
 
for info in soup.select('td'):
    print(info.text)
