## 함수 선언 부분 ##
def multi(v1, v2) :
     # retList=[]       # 반환할 리스트
     res1 = v1 + v2
     res2 = v1 - v2
     # retList.append(res1)
     # retList.append(res2)
     # return retList
     return res1, res2
	
## 전역 변수 선언 부분 ##
myList = []
hap, sub = 0, 0

## 메인 코드 부분 ##
#방법1 : 결과 반환값 리스트로 , 해당 리스트에서 요소를 하나씩 꺼내서 담았음. 
# myList = multi(100, 200)
# hap = myList[0]
# sub = myList[1]
#방법2
hap, sub = multi(100,200)
print(type(multi(100,200)))
print("multi()에서 돌려준 값 ==> %d, %d" % (hap, sub))
