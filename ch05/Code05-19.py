inFp = None 
inList = ""    

inFp = open("C:/Temp/data3.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
print(type(inList))
print(inList)

inFp.close()
