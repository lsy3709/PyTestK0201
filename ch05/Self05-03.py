inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열
lineNum = 1 # 상태변수, -> 디자인패턴 상태 패턴.

inFp = open("C:/Temp/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print("%d : %s" %(lineNum, inStr), end="")
    lineNum += 1

inFp.close()
