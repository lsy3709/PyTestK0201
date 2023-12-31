import bs4
import urllib.request

import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

nateUrl = "https://news.nate.com"
htmlObject = urllib.request.urlopen(nateUrl,context=ssl_context)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

#뉴스 카테고리 메뉴 
tag = bsObject.find('div', {'class':'snbArea'})

print('## 네이트 뉴스의 메뉴 목록 ##')
li_list = tag.findAll('li')
for li in li_list :
    print(li.text, end='  ' )