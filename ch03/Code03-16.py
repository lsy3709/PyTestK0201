#전역변수 사용됨.
i, k = 0, 0

#따로 메인 함수가 없음. 코드가 짧아서, 단순, 순차적으로실행.
# 코드가 복잡해지면, 임의로 우리가 메인 함수부분을 
#설정을 해서, 호출부분을 따로 정할 예정. 

for i in range(2, 10, 1) :
     print("%d 단 " % i)
     for k in range(1, 10, 1) : # 바같 for 문에서 순서1
          print("%d X %d = %2d" %(i, k, i * k))
     print("")	 # 바같 for 문에서 순서2
