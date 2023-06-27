 # data = []
# i,k = 0,0 

# if __name__ == "__main__" :
#   for i in range(0,10) :
#     tmp = hex(random.randrange(0,100000))
#     data.append(tmp)
    
#   print('정렬 전 데이터 : ', end = ' ')
#   [print(num, end=" ") for num in data]
  
#   for i in range(0, len(data)-1):
#     for k in range(i + 1, len(data)):
#       # int(data[i],16) 식은 16진법(16진수) 표현을 사용하여 
#       # 16진수 문자열 data[i]를 정수로 변환합니다.
#       if int(data[i],16) > int(data[k],16):
#         tmp = data[i]
#         data[i] = data[k]
#         data[k] = tmp 
        
#   print('\n 정렬 후 데이터 : ', end=" ")
#   [print(num, end=" ") for num in data]
  
  
  
  
import random

def getNumber(strData):
  numStr = ""
  for ch in strData:
    if ch.isdigit():
      numStr += ch 
  return int(numStr)

data = []
i,k = 0,0 

if __name__ == "__main__" :
  for i in range(0,10):
    tmp = hex(random.randrange(0,100000))
    tmp = tmp[2:]
    data.append(tmp)
  
  print("정렬 전 데이터 : ", end="")
  [print(num, end = " ") for num in data]
  
  for i in range(0, len(data)-1):
    for k in range(i + 1, len(data)) :
      if getNumber(data[i]) > getNumber(data[k]):
        tmp = data[i]
        data[i] = data[k]
        data[k] = tmp 
  
  print("\n 정렬 후 데이터 : ", end="")
  [print(num, end=" ") for num in data]