outFp = None 
outStr = ""

#encoding 기본값 ANSI 되어 있다. 
# outFp = open("C:/Temp/data3d.txt", "w",encoding="utf-8")
with open("C:/Temp/data4.txt", "w",encoding="utf-8") as outFp :
    while True:
        outStr = input("내용 입력 : ")
        if outStr != "" :
             outFp.writelines(outStr + "\n")
        else :
            break


print("--- 정상적으로 파일에 씀 ---")
