import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum_0628.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # 만약, 헤더가 다르다면, 양식이 다르면, 출력할 헤더를 정해서
            # 해당 인덱스로 필터링하기. 
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')