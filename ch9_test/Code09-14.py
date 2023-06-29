import bs4
import urllib.request
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

## 함수 선언부
def getBookInfo(book_tag) :
    #부모 태그 -> 자식 태그 참조부분.
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text
    
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

## 전역 변수부
bookUrl = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber=1"

## 메인 코드부
htmlObject = urllib.request.urlopen(bookUrl,context=ssl_context)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

#부모태그 순서1
tag = bsObject.find('ul', {'class': 'clearfix'})
#부모태그 하위의 상품의 정보 조회.(자식태그) 순서2 
all_books = tag.findAll('div', {'class': 'goods_info'})

#goods_info 라는 상품이 20개가 수집
# 이중에서 하나의 상품을 선택하고, 여기서 , 관련 도서 정보를 가져오는 작업. 
for book in all_books :
    print(getBookInfo(book))