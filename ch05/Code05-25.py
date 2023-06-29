from tkinter import *

## 함수 선언 부분 ##
def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE) :
        tmpList = [] #순서1
        for k in range(0, YSIZE) : #순서2
            data = int(ord(fp.read(1)))
            # print(fp.read(1))
            #ord 유니코드의 한 문자의 값을 정수로 표현. 
            # print(ord(fp.read(1)))
            tmpList.append(data)
            # print(tmpList)
        inImage.append(tmpList) #순서3
        #inImage = [ [요소1(256)], [요소2(256)], [요소3(256)], ... [요소256(256)]   ] : 요소로 256개 있습니다. 

    fp.close()

def displayImage(image) : #image = inImage 이중 배열. 
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = "" # 순서1
        for k in range(0, YSIZE) : # 순서2
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백
            # print(tmpString)
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백  # 순서3
        # print(rgbString)
    paper.put(rgbString)

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE=256,256
inImage=[] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# 파일 --> 메모리 : 결과 전역 변수인 inImage 배열에 담아져 있음. 
filename = 'RAW/tree.raw'  # C:/CookAnalysis/RAW/tree.raw
loadImage(filename)

# 메모리(inImage 배열 ) --> 화면 
displayImage(inImage)

canvas.pack()
window.mainloop()
