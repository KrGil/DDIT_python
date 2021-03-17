# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup

client_id = "ejVfXFjwwk9RSqINoSIB"
client_secret = "FOjdHPDVUQ"
encText = urllib.parse.quote("기아차")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
# else:
    # print("Error Code:" + rescode)

soup = BeautifulSoup(response_body, 'html.parser')
items = soup.select("item")

for info in items:
    title = info.title.text
    link = info.link.text
    description = info.description.text
    bloggername = info.bloggername.text
    bloggerlink = info.bloggerlink.text
    postdate = info.postdate.text
    
    print(title, end="\t")
    print(link, end="\t")
    print(description, end="\t")
    print(bloggername, end="\t")
    print(bloggerlink, end="\t")
    print(postdate, end="\n")
# 태그 text 들고오기
