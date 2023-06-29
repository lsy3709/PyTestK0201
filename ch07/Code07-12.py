from tkinter import *
import xlsxwriter
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()

photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b
# 이미지의 각 픽셀의 RGB 의 색깔 코드를 가져오는 작업, 이미지 -> 메모리 :입력

# 여기 절대경로에 엑셀 파일 형식으로 쓰기 작업 , 메모리 -> 파일 : 출력
workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/pic7_0629.xlsx')
# 워크시트 3개
worksheetR = workbook.add_worksheet('photoR')
worksheetG = workbook.add_worksheet('photoG')
worksheetB = workbook.add_worksheet('photoB')

for i in range(w) :
    for k in range(h) :
        worksheetR.write(i, k, photoR[i][k])
        worksheetG.write(i, k, photoG[i][k])
        worksheetB.write(i, k, photoB[i][k])

workbook.close()
print('Save. OK~')