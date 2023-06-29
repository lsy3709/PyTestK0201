import xlwt
import csv
import os

csvFileList = ["C:/CookAnalysis/CSV/singerA.csv", "C:/CookAnalysis/CSV/singerB.csv"]
#csv 2개 -> 하나의 엑셀파일로 만들기 위해서, 전역 설정. 
outWorkbook = xlwt.Workbook()

# csv2개 -> 각각 엑셀 파일 만들기 위해서, 쓰는 작업 2번. 

for csvFileName in csvFileList :
    rowCount = 0
    with open(csvFileName, "r") as inFp:
        csvReader = csv.reader(inFp)
        header_list = next(csvReader)
        print(header_list)
        
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
        print(os.path.basename(csvFileName))
        
        for col in range(len(header_list)) :
            outSheet.write(rowCount, col, header_list[col])
            #실제 데이터 입력부분.
        for row_list in csvReader:
            rowCount += 1
            for col in range(len(row_list)):
                if row_list[col].isnumeric() :
                    outSheet.write(rowCount, col, float(row_list[col]))
                else :
                    outSheet.write(rowCount, col, row_list[col])

outWorkbook.save('c:/CookAnalysis/Excel/singerCSV_0628.xls')
print("Save. OK~")